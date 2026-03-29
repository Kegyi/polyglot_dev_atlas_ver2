import os
import json
import time
import argparse
import threading
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
from typing import Any

@dataclass
class Page:
    id: str
    group: str
    group_title: str
    view: str
    title: str
    description: str
    insight: str
    code_snippets: Dict[str, str]
    sub_contents: List[Dict]

def load_mock_data():
    content_root = os.path.join(os.path.dirname(__file__), "content")
    # shared cache for resolved files to avoid re-reading/parsing
    cache: Dict[str, Any] = {}
    data_json_path = os.path.join(content_root, "data", "data.json")
    view_categories = {}
    languages = []

    if os.path.isfile(data_json_path):
        try:
            with open(data_json_path, 'r', encoding='utf-8') as df:
                data_obj = json.load(df)
            vc = data_obj.get('view_categories') or {}
            new_vc = {k: (v.get('views', []) if isinstance(v, dict) else v) for k, v in vc.items()}
            if new_vc: view_categories = new_vc

            lang_obj = data_obj.get('languages', {})
            order = lang_obj.get('order') if isinstance(lang_obj, dict) else None
            if order:
                seen = set()
                for l in order:
                    out = 'scala' if l.startswith('scala') else l
                    if out not in seen:
                        languages.append(out)
                        seen.add(out)
        except Exception: pass

    pages = []
    base_dir = os.path.join(content_root, "pages")
    views_flat = [v for vals in view_categories.values() for v in vals]
    views_map = {v.lower(): v for v in views_flat}

    if os.path.isdir(base_dir):
        for fname in sorted(os.listdir(base_dir)):
            if not fname.endswith('.page.json'): continue
            key = fname[:-len('.page.json')]
            match_view = views_map.get(key.lower())
            page_path = os.path.join(base_dir, fname)
            with open(page_path, 'r', encoding='utf-8') as f:
                try:
                    obj = json.load(f)
                except Exception:
                    continue

            # Resolve $ref and external aliases in the loaded page JSON
            try:
                resolve_refs(obj, content_root)
            except Exception:
                pass

            # (validation moved to top-level --lint handling)

            groups_map = {k: v.get('title', k) for k, v in obj.get('groups', {}).items()}
            for slug, item in obj.get('content', {}).items():
                group_key = item.get('group', 'groupTitle')
                insight = item['points'][0] if item.get('points') else (item['notes'][0] if item.get('notes') else '')
                sub_contents = []
                if item.get('points'): sub_contents.append({"title": "Points", "text": "\n".join(item.get('points', []))})
                if item.get('notes'): sub_contents.append({"title": "Notes", "text": "\n".join(item.get('notes', []))})

                # Materialize code snippet file references if any
                def _materialize_snippets(snips, page_dir):
                    out = {}
                    if not isinstance(snips, dict):
                        return snips
                    for k, v in snips.items():
                        if isinstance(v, str):
                            candidate = v
                            # map alias or relative to page dir
                            if candidate.startswith('@'):
                                candidate_path = _map_alias_path(candidate, content_root)
                            else:
                                candidate_path = os.path.join(page_dir, candidate)
                                if not os.path.isfile(candidate_path):
                                    # fallback to content root
                                    candidate_path = os.path.join(content_root, candidate)

                            if os.path.isfile(candidate_path):
                                try:
                                    with open(candidate_path, 'r', encoding='utf-8') as cf:
                                        out[k] = cf.read()
                                        continue
                                except Exception:
                                    pass
                        out[k] = v
                    return out

                page_dir = os.path.dirname(page_path)

                # materialize blocks: resolve any @-prefixed data pointers into parsed JSON or raw text
                def _materialize_blocks(blocks):
                    out_blocks = []
                    if not isinstance(blocks, list):
                        return blocks
                    for b in blocks:
                        if isinstance(b, dict):
                            d = b.get('data')
                            if isinstance(d, str) and d.startswith('@'):
                                try:
                                    resolved = _resolve_ref_string(d, content_root, cache)
                                    # if resolved is dict/list, use it directly; otherwise keep raw string
                                    b['data'] = resolved
                                except Exception:
                                    # fallback: map a few common aliases locally
                                    if d.startswith('@snippets/'):
                                        p = os.path.join(content_root, 'snippets', d[len('@snippets/'):])
                                    elif d.startswith('@images/'):
                                        p = os.path.join(content_root, 'images', d[len('@images/'):])
                                    elif d.startswith('@core/'):
                                        p = os.path.join(content_root, 'core', d[len('@core/'):])
                                    else:
                                        p = os.path.join(content_root, d.lstrip('./'))
                                    if os.path.isfile(p):
                                        try:
                                            with open(p, 'r', encoding='utf-8') as fh:
                                                # attempt JSON parse, fallback to raw
                                                try:
                                                    b['data'] = json.load(fh)
                                                except Exception:
                                                    fh.seek(0)
                                                    b['data'] = fh.read()
                                        except Exception:
                                            pass
                        out_blocks.append(b)
                    return out_blocks

                pages.append({
                    "id": f"{key}_{slug}", "group": group_key, "group_title": groups_map.get(group_key, group_key),
                    "view": match_view or obj.get('page') or key, "title": item.get('title', ''),
                    "description": item.get('description', ''), "insight": insight,
                    "code_snippets": _materialize_snippets(item.get('code_snippets', {}) or item.get('code', {}), page_dir),
                    "blocks": _materialize_blocks(item.get('blocks', [])),
                    "sub_contents": sub_contents
                })

    if not pages:
        pages = [{"id": "p1", "group": "mem", "group_title": "System", "view": "Architecture", "title": "Welcome", "description": "No content found.", "insight": "Check content/pages/", "code_snippets": {}, "sub_contents": []}]
    if not languages: languages = ["cpp", "python", "js"]
    if not view_categories: view_categories = {"atlas": ["Architecture"], "learning": []}

    return {"view_categories": view_categories, "languages": languages, "pages": pages}

def generate_styles():
    return """
    :root {
        /* Surface Colors (Dark Default) */
        --bg: #0f172a; --panel: #1e293b; --sidebar: #0f172a; --border: rgba(255,255,255,0.08);
        --text: #f1f5f9; --text-m: #94a3b8;
        /* Accents (Amethyst Default) */
        --accent: #818cf8; --accent-sec: #2dd4bf; --sidebar-w: 280px;
    }
    
    /* Global Light Mode Overrides - Apply to all styles */
    body.light { 
        --bg: #f8fafc; --panel: #ffffff; --sidebar: #f1f5f9; 
        --text: #1e293b; --text-m: #64748b; --border: rgba(0,0,0,0.1); 
    }

    /* Style Palettes (Accents Only) */
    body[data-style="ocean"] { --accent: #38bdf8; --accent-sec: #fb7185; }
    body:not(.light)[data-style="ocean"] { --bg: #0b1217; --panel: #17212b; --sidebar: #0b1217; }
    
    body[data-style="sunset"] { --accent: #fbbf24; --accent-sec: #f472b6; }
    body:not(.light)[data-style="sunset"] { --bg: #18141b; --panel: #241e29; --sidebar: #18141b; }

    body { font-family: 'Inter', system-ui, sans-serif; margin: 0; background: var(--bg); color: var(--text); overflow: hidden; }
    .app-layout { display: grid; grid-template-columns: var(--sidebar-w) 1fr; height: 100vh; transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
    .app-layout.sidebar-hidden { grid-template-columns: 0px 1fr; }

    .sidebar { background: var(--sidebar); border-right: 1px solid var(--border); overflow-x: hidden; display: flex; flex-direction: column; }
    .sidebar-content { width: var(--sidebar-w); flex-shrink: 0; }
    .main { display: flex; flex-direction: column; overflow: hidden; position: relative; }
    .topbar { padding: 16px 24px; background: var(--panel); border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: flex-start; z-index: 10; }
    .stack-left, .stack-right { display: flex; flex-direction: column; gap: 12px; }
    .stack-right { align-items: flex-end; }
    .row { display: flex; align-items: center; gap: 8px; }

    .scroll-area { flex: 1; overflow-y: auto; scroll-behavior: smooth; }
    .content-wrap { max-width: 1000px; margin: 0 auto; padding: 40px 24px; }

    .btn { background: transparent; border: 1px solid var(--border); color: var(--text-m); padding: 6px 12px; border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: 500; transition: 0.2s; user-select: none; }
    .btn:hover { border-color: var(--accent); color: var(--text); }
    .btn.active-left { background: var(--accent); color: white; border-color: var(--accent); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .btn.active-right { background: var(--accent-sec); color: #000; border-color: var(--accent-sec); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .btn.selected { border-color: var(--accent); color: var(--accent); background: rgba(129,140,248,0.05); }
    
    .code-grid { display: grid; gap: 20px; margin: 32px 0; grid-template-columns: 1fr; min-height: 100px; }
    .code-grid.split { grid-template-columns: 1fr 1fr; }
    .code-box { background: #000; border-radius: 12px; border: 1px solid var(--border); overflow: hidden; }
    .code-label { background: rgba(255,255,255,0.05); padding: 6px 12px; font-size: 10px; font-weight: 800; text-transform: uppercase; color: var(--text-m); border-bottom: 1px solid var(--border); }
    pre { margin: 0; padding: 20px; overflow-x: auto; font-family: 'Fira Code', monospace; font-size: 13px; color: #e2e8f0; line-height: 1.5; }

    .nav-item { padding: 10px 12px; border-radius: 6px; cursor: pointer; font-size: 14px; margin-bottom: 2px; color: var(--text-m); transition: 0.2s; }
    .nav-item:hover { background: rgba(255,255,255,0.05); color: var(--text); }
    .nav-item.active { background: var(--accent); color: white; font-weight: 600; }
    .empty-state { text-align: center; padding: 100px 24px; color: var(--text-m); }
    .hidden { display: none; }
    """

def generate_scripts():
    return """
    (() => {
        const data = window.__DATA__;
        const state = { 
            primary: data.languages[0], secondary: null, pageId: null, 
            style: 'default', compare: false, course: false, sidebarVisible: true,
            view: null, lastAtlasView: null, lastCourseView: null
        };

        // Renderer Registry: map block types to renderer functions
        const Renderers = {
            sheet: (block) => {
                const data = block.data || [];
                // Improved language detection: prefer explicit `options.lang`, then id/title, then data heuristics
                let blockLang = null;
                try{
                    // 1) explicit option
                    if(block && block.options){
                        const opt = block.options.lang || block.options.language || block.options.lang_code;
                        if(opt){ const s = String(opt).toLowerCase(); if(s==='py') blockLang='python'; else if(s==='c++') blockLang='cpp'; else blockLang = s; }
                    }

                    // 2) infer from id/title if not explicit
                    if(!blockLang && block && block.id){
                        const m = String(block.id).match(/-([a-zA-Z0-9_+-]+)$/);
                        if(m && m[1]){
                            const suffix = m[1].toLowerCase();
                            if(suffix === 'py' || suffix === 'python') blockLang = 'python';
                            else if(suffix === 'cpp' || suffix === 'c++') blockLang = 'cpp';
                            else blockLang = suffix;
                        }
                    }
                    if(!blockLang && block && block.title){
                        const t = String(block.title).toLowerCase();
                        if(t.includes('python') || t.includes('py')) blockLang = 'python';
                        else if(t.includes('c++') || t.includes('cpp')) blockLang = 'cpp';
                        else if(t.includes('demo')) blockLang = 'demo';
                    }

                    // 3) heuristic from data: scan snippets/rows for language-specific tokens
                    if(!blockLang){
                        const detectFromText = (txt)=>{
                            if(!txt) return null;
                            const s = String(txt).toLowerCase();
                            if(s.includes('std::') || s.includes('constexpr') || s.includes('#include') || s.includes('typename') || s.includes('std::thread')) return 'cpp';
                            if(s.match(/\bdef\s+\w+\b/) || s.includes('async ') || s.includes('self') || s.includes('import ') || s.includes('yield')) return 'python';
                            if(s.includes('pub ') || s.includes('defer') || s.includes('match')) return 'demo';
                            return null;
                        };

                        const scanData = (d)=>{
                            try{
                                if(!d) return null;
                                if(Array.isArray(d)){
                                    // hierarchical sections
                                    if(d.length && typeof d[0] === 'object'){
                                        for(const sec of d){ if(sec && sec.categories){ for(const c of sec.categories){ if(c && Array.isArray(c.items)){ for(const row of c.items){ for(const cell of row){ const r = detectFromText(cell); if(r) return r; } } } } } }
                                    }
                                    // flat table rows
                                    for(const row of d){ if(Array.isArray(row)){ for(const cell of row){ const r = detectFromText(cell); if(r) return r; } } else { const r = detectFromText(row); if(r) return r; } }
                                } else if(typeof d === 'object'){
                                    return detectFromText(JSON.stringify(d));
                                } else {
                                    return detectFromText(d);
                                }
                            }catch(e){ return null; }
                            return null;
                        };

                        const maybe = scanData(data);
                        if(maybe) blockLang = maybe;
                    }
                }catch(e){ blockLang = null; }

                // If this block appears to be language-specific, only render it when that language is selected
                if(blockLang && state.primary && blockLang !== String(state.primary).toLowerCase()){
                    return '';
                }
                const tableId = 'sheet_' + (block.id || Math.random().toString(36).slice(2,8));

                const parseVersion = (s) => {
                    if(!s) return { text: '', version: null };
                    const m = s.match(/:v:(.*?):!v:/);
                    if(m){
                        const text = s.replace(m[0], '').trim();
                        return { text: text, version: m[1].trim() };
                    }
                    return { text: s, version: null };
                };

                const renderItemsTable = (items) => {
                    if(!items || !items.length) return '';
                    let html = '<div style="overflow:auto">';
                    html += `<table style="width:100%; border-collapse:collapse">`;
                    html += '<thead><tr>' + ['Keyword','Description','Header','Snippet'].map(h=>`<th style="text-align:left; padding:8px; border-bottom:1px solid rgba(0,0,0,0.08); color:var(--text)">${escapeHtml(h)}</th>`).join('') + '</tr></thead>';
                    html += '<tbody>' + items.map(row => {
                        const kw = escapeHtml(row[0]||'');
                        const parsed = parseVersion(row[1]||'');
                        let descHtml = escapeHtml(parsed.text||'');
                        if(parsed.version) descHtml += ' <span style="color:var(--text-m); font-size:12px; margin-left:6px">(' + escapeHtml(parsed.version) + ')</span>';
                        const header = escapeHtml(row[2]||'');
                        const snippet = escapeHtml(row[3]||'');
                        return '<tr>' + [`<td style="padding:8px; border-bottom:1px solid rgba(0,0,0,0.04);">${kw}</td>`, `<td style="padding:8px; border-bottom:1px solid rgba(0,0,0,0.04);">${descHtml}</td>`, `<td style="padding:8px; border-bottom:1px solid rgba(0,0,0,0.04);">${header}</td>`, `<td style="padding:8px; border-bottom:1px solid rgba(0,0,0,0.04); font-family:monospace; white-space:pre-wrap">${snippet}</td>`].join('') + '</tr>';
                    }).join('') + '</tbody>';
                    html += '</table></div>';
                    return html;
                };

                // If data is sections (objects with `section`), render hierarchical view
                if(Array.isArray(data) && data.length && typeof data[0] === 'object' && data[0].section){
                    let out = '';
                    data.forEach(sec => {
                        out += `<h2 style="margin-top:24px; margin-bottom:8px">${escapeHtml(sec.section)}</h2>`;
                        const cats = sec.categories || [];
                        cats.forEach(cat => {
                            out += `<div style="margin-bottom:12px"><h3 style="margin:8px 0">${escapeHtml(cat.category)}</h3>`;
                            out += renderItemsTable(cat.items || []);
                            out += '</div>';
                        });
                    });
                    return `<div style="margin:16px 0">${out}</div>`;
                }

                // Comparison mode: if blocks are grouped with the same compareGroup and compare is active,
                // find the matching primary/secondary blocks on the same page and render a side-by-side view.
                try{
                    if(block && block.options && block.options.compareGroup && state.compare && state.secondary){
                        const page = data.pages.find(p => p.id === state.pageId);
                        if(page){
                            const siblings = (page.blocks || []).filter(bb => bb.type === 'sheet' && bb.options && bb.options.compareGroup === block.options.compareGroup);
                            const keyFor = (bb) => (bb && bb.options && (bb.options.lang || bb.options.language || '')).toString().toLowerCase();
                            let primaryBlock = siblings.find(bb => keyFor(bb) === String(state.primary).toLowerCase());
                            let secondaryBlock = siblings.find(bb => keyFor(bb) === String(state.secondary).toLowerCase());
                            if(!primaryBlock) primaryBlock = block;
                            if(!secondaryBlock) secondaryBlock = siblings.find(bb => bb !== primaryBlock) || null;

                            if(primaryBlock && secondaryBlock){
                                const normalize = (d) => {
                                    if(!d) return [];
                                    if(Array.isArray(d)){
                                        if(d.length && typeof d[0] === 'object' && d[0].section){
                                            const out = [];
                                            d.forEach(sec => { (sec.categories || []).forEach(cat => { (cat.items || []).forEach(row => { out.push(row); }); }); });
                                            return out;
                                        }
                                        // if first row looks like a header (strings with 'keyword' or similar), drop it
                                        if(d.length && Array.isArray(d[0])){
                                            const head = d[0].map ? d[0] : d[0];
                                            const firstRowText = head.join(' ').toLowerCase();
                                            if(firstRowText.includes('keyword') || firstRowText.includes('description')){
                                                return d.slice(1);
                                            }
                                        }
                                        return d;
                                    } else if(typeof d === 'string'){
                                        return [[d,'','','']];
                                    } else if(typeof d === 'object'){
                                        return [[JSON.stringify(d),'','','']];
                                    }
                                    return [];
                                };

                                const rowsA = normalize(primaryBlock.data || []);
                                const rowsB = normalize(secondaryBlock.data || []);
                                const mapA = new Map(); rowsA.forEach(r => mapA.set(String(r[0]||'').trim(), r));
                                const mapB = new Map(); rowsB.forEach(r => mapB.set(String(r[0]||'').trim(), r));
                                const keys = Array.from(new Set([...mapA.keys(), ...mapB.keys()]));

                                let html = '<div style="overflow:auto">';
                                html += `<table style="width:100%; border-collapse:collapse">`;
                                html += '<thead><tr>' + ['Keyword', String(state.primary||'Primary'), String(state.secondary||'Secondary')].map(h=>`<th style="text-align:left; padding:8px; border-bottom:1px solid rgba(0,0,0,0.08); color:var(--text)">${escapeHtml(h)}</th>`).join('') + '</tr></thead>';
                                html += '<tbody>' + keys.map(k => {
                                    const a = mapA.get(k) || ['','','',''];
                                    const b = mapB.get(k) || ['','','',''];
                                    const aMissing = !mapA.has(k);
                                    const bMissing = !mapB.has(k);
                                    const pa = parseVersion(a[1]||'');
                                    const pb = parseVersion(b[1]||'');
                                    const descA = (pa.text||'').toString().trim();
                                    const descB = (pb.text||'').toString().trim();
                                    const headerA = (a[2]||'').toString().trim();
                                    const headerB = (b[2]||'').toString().trim();
                                    const snippetA = (a[3]||'').toString().trim();
                                    const snippetB = (b[3]||'').toString().trim();
                                    const descDiff = (!aMissing && !bMissing) && descA !== descB;
                                    const headerDiff = (!aMissing && !bMissing) && headerA !== headerB;
                                    const snippetDiff = (!aMissing && !bMissing) && snippetA !== snippetB;
                                    const makeStack = (row, missing, diffs) => {
                                        if(missing) return `<div style="color:var(--text-m); font-style:italic">(missing)</div>`;
                                        const p = parseVersion(row[1]||'');
                                        let descHtml = escapeHtml(p.text||'');
                                        if(p.version) descHtml += ' <span style="color:var(--text-m); font-size:12px; margin-left:6px">(' + escapeHtml(p.version) + ')</span>';
                                        const header = escapeHtml(row[2]||'');
                                        const snippet = escapeHtml(row[3]||'');
                                        const descStyle = diffs && diffs.desc ? 'background:rgba(255,165,0,0.06); padding:6px; border-radius:6px' : '';
                                        const headerStyle = diffs && diffs.header ? 'background:rgba(255,165,0,0.04); padding:4px; border-radius:4px' : '';
                                        const snippetStyle = diffs && diffs.snip ? 'background:rgba(255,165,0,0.04); padding:6px; border-radius:6px' : '';
                                        return `<div style="display:flex;flex-direction:column;gap:6px"><div style="font-weight:600; ${descStyle}">${descHtml}</div><div style="color:var(--text-m);font-size:12px; ${headerStyle}">${header}</div><div style="margin-top:6px; font-family:monospace; white-space:pre-wrap; ${snippetStyle}">${snippet}</div></div>`;
                                    };
                                    return '<tr>' + [`<td style="padding:8px; border-bottom:1px solid rgba(0,0,0,0.04); width:20%">${escapeHtml(k)}</td>`, `<td style="padding:8px; border-bottom:1px solid rgba(0,0,0,0.04); width:40%">${makeStack(a, aMissing, {desc: descDiff, header: headerDiff, snip: snippetDiff})}</td>`, `<td style="padding:8px; border-bottom:1px solid rgba(0,0,0,0.04); width:40%">${makeStack(b, bMissing, {desc: descDiff, header: headerDiff, snip: snippetDiff})}</td>`].join('') + '</tr>';
                                }).join('') + '</tbody>';
                                html += '</table></div>';
                                return `<div style="margin:16px 0">${html}</div>`;
                            }
                        }
                    }
                }catch(e){ /* ignore comparison errors and fall back */ }

                // fallback: assume simple rows array
                const rows = Array.isArray(data) ? data : [];
                const hasHeader = rows.length && Array.isArray(rows[0]);
                if(hasHeader){
                    // try to find language column
                    const head = rows[0];
                    const lang = (state.primary||'').toLowerCase();
                    let langCol = -1;
                    for(let i=0;i<head.length;i++){ try{ const h=String(head[i]).toLowerCase(); if(h===lang||h.includes(lang)){ langCol=i; break; } }catch(e){} }
                    const condensed = [];
                    const titleCol = head[0]||'';
                    const langTitle = (langCol>0? head[langCol] : head[1]||'');
                    condensed.push([titleCol, langTitle]);
                    rows.slice(1).forEach(r => condensed.push([r[0]||'', (langCol> -1 && r[langCol]!==undefined)? r[langCol] : (r[1]||'')]));
                    return `<div style="margin:16px 0">${renderItemsTable(condensed)}</div>`;
                }

                return `<div style="margin:16px 0">${renderItemsTable(rows)}</div>`;
            }
        };

        function escapeHtml(s){ if(s==null) return ''; return String(s).replace(/[&"'<>]/g, function(c){ if(c==='&') return '&amp;'; if(c==='<') return '&lt;'; if(c==='>') return '&gt;'; if(c==='"') return '&quot;'; if(c==="'") return '&#39;'; return c; }); }
        function transposeMatrix(m){ if(!m || !m.length) return m; const rows = Math.max(...m.map(r=>r.length)); const out = []; for(let c=0;c<rows;c++){ const row = []; for(let r=0;r<m.length;r++){ row.push(m[r][c]===undefined? '': m[r][c]); } out.push(row); } return out; }

        function renderBlock(b){
            try{
                if(!b || !b.type) return '<pre style="color:var(--text-m)">Invalid block</pre>';
                const fn = Renderers[b.type];
                if(!fn) return `<pre style="color:var(--text-m)">No renderer for type: ${escapeHtml(b.type)}</pre>`;
                return fn(b);
            }catch(e){ return `<pre style="color:var(--text-m)">${escapeHtml(String(e))}</pre>`; }
        }

        const qs = s => document.querySelector(s);
        
        let touchTimer;
        const initLangEvents = (el) => {
            el.addEventListener('touchstart', (e) => {
                touchTimer = setTimeout(() => { handleSelect(el.dataset.lang, true); touchTimer = null; }, 500);
            }, {passive: true});
            el.addEventListener('touchend', () => { if (touchTimer) { clearTimeout(touchTimer); touchTimer = null; } });
        };

        const handleSelect = (lang, isSecondary) => {
            if (isSecondary) {
                if (state.secondary === lang) { state.secondary = null; state.compare = false; }
                else if (state.primary === lang) { [state.primary, state.secondary] = [state.secondary, state.primary]; }
                else { state.secondary = lang; state.compare = true; }
            } else {
                if (state.primary === lang) { state.primary = state.secondary; state.secondary = null; state.compare = false; }
                else if (state.secondary === lang) { [state.primary, state.secondary] = [state.secondary, state.primary]; }
                else { state.primary = lang; }
            }
            if (!state.primary && state.secondary) { state.primary = state.secondary; state.secondary = null; state.compare = false; }
            syncUI();
        };

        const syncUI = () => {
            document.body.setAttribute('data-style', state.style);
            qs('#app-layout').classList.toggle('sidebar-hidden', !state.sidebarVisible);
            
            document.querySelectorAll('.btn.lang').forEach(b => {
                const l = b.dataset.lang;
                b.classList.remove('active-left', 'active-right');
                if(l === state.primary) b.classList.add('active-left');
                if(state.compare && l === state.secondary) b.classList.add('active-right');
            });

            const views = data.view_categories[state.course ? 'learning' : 'atlas'] || [];
            qs('#view-list').innerHTML = views.map(v => `<button class="btn view ${v===state.view?'selected':''}" data-view="${v}">${v}</button>`).join('');
            
            qs('#compareBtn').classList.toggle('selected', state.compare);
            qs('#swapBtn').classList.toggle('hidden', !state.compare || !state.secondary);
            qs('#courseBtn').classList.toggle('selected', state.course);
            document.querySelectorAll('.btn.style').forEach(b => b.classList.toggle('selected', b.dataset.style === state.style));
            
            renderSidebar();
            renderContent();
        };

        const renderSidebar = () => {
            if (!state.view) { qs('#sidebar-nav').innerHTML = '<div class="empty-state">Select a view</div>'; return; }
            const filtered = data.pages.filter(p => p.view === state.view);
            const groups = {};
            filtered.forEach(p => { 
                if(!groups[p.group]) groups[p.group] = {title: p.group_title, items: []}; 
                groups[p.group].items.push(p); 
            });
            qs('#sidebar-nav').innerHTML = Object.values(groups).map(g => `
                <div style="padding:20px 16px 0"><div style="font-size:10px;font-weight:800;color:var(--text-m);text-transform:uppercase;margin-bottom:10px">${g.title}</div>
                ${g.items.map(p => `<div class="nav-item ${p.id===state.pageId?'active':''}" onclick="setPage('${p.id}')">${p.title}</div>`).join('')}</div>
            `).join('');
        };

        const renderContent = () => {
            const p = data.pages.find(x => x.id === state.pageId);
            if (!state.view || !p) {
                qs('#main-content').innerHTML = `
                    <div class="empty-state">
                        <h1 style="font-size:48px; color:var(--text); margin-bottom:16px; letter-spacing:-2px">Dev Atlas</h1>
                        <p style="font-size:20px; max-width:500px; margin:0 auto">Select a category from the top bar to begin exploring architectural patterns and code implementation.</p>
                    </div>`;
                return;
            }
            // If the page uses Blocks (new schema), render them via the Renderers registry
            let blocksHtml = '';
            if (p.blocks && Array.isArray(p.blocks)) {
                blocksHtml = p.blocks.map(b => renderBlock(b)).join('\\n');
            }

            qs('#main-content').innerHTML = `
                <div class="content-wrap">
                    <h1 style="font-size:42px; margin:0; letter-spacing:-1px">${p.title}</h1>
                    <p style="font-size:18px; color:var(--text-m); margin:20px 0; line-height:1.6">${p.description}</p>
                    <div style="background:rgba(129,140,248,0.1); padding:24px; border-radius:12px; border-left:4px solid var(--accent); margin-bottom:40px">
                        <div style="font-size:10px;font-weight:800;color:var(--text-m);text-transform:uppercase;margin-bottom:8px">Core Insight</div>
                        <div style="line-height:1.5">${p.insight}</div>
                    </div>
                    ${ blocksHtml || `
                    <div class="code-grid ${state.compare?'split':''}">
                        <div class="code-box"><div class="code-label">${state.primary || 'No Language'}</div><pre><code>${state.primary ? (p.code_snippets[state.primary] || '// No snippet') : ''}</code></pre></div>
                        ${state.compare && state.secondary ? `<div class="code-box"><div class="code-label">${state.secondary}</div><pre><code>${p.code_snippets[state.secondary] || '// No snippet'}</code></pre></div>` : ''}
                    </div>
                    ` }
                    ${p.sub_contents.map(s => `
                        <div style="border:1px solid var(--border); border-radius:12px; margin-top:16px; cursor:pointer" onclick="this.lastElementChild.classList.toggle('hidden')">
                            <div style="padding:16px; display:flex; justify-content:space-between; font-size:10px; font-weight:800; color:var(--text-m); text-transform:uppercase"><span>${s.title}</span><span>▼</span></div>
                            <div class="hidden" style="padding:0 16px 16px; color:var(--text-m); line-height:1.6; white-space:pre-wrap">${s.text}</div>
                        </div>
                    `).join('')}
                </div>
            `;
        };

        window.setPage = id => { state.pageId = id; syncUI(); };
        window.toggleSidebar = () => { state.sidebarVisible = !state.sidebarVisible; syncUI(); };

        document.addEventListener('mousedown', e => {
            const b = e.target.closest('.btn.lang'); if(!b || e.button === 2) return;
            handleSelect(b.dataset.lang, false);
        });

        document.addEventListener('contextmenu', e => {
            const b = e.target.closest('.btn.lang'); if(!b) return;
            e.preventDefault(); handleSelect(b.dataset.lang, true);
        });

        document.addEventListener('click', e => {
            const b = e.target.closest('.btn'); if(!b || b.dataset.lang) return;
            if(b.dataset.view) { 
                const v = b.dataset.view; state.view = (state.view === v) ? null : v;
                if (state.course) state.lastCourseView = state.view; else state.lastAtlasView = state.view;
                state.pageId = null; 
            }
            else if(b.dataset.style) state.style = b.dataset.style;
            else if(b.id === 'compareBtn') { state.compare = !state.compare; if(state.compare && !state.secondary) state.secondary = data.languages.find(l=>l!==state.primary); }
            else if(b.id === 'swapBtn') [state.primary, state.secondary] = [state.secondary, state.primary];
            else if(b.id === 'courseBtn') { 
                state.course = !state.course; state.view = state.course ? state.lastCourseView : state.lastAtlasView;
                state.pageId = null;
            }
            else if(b.id === 'themeToggle') { document.body.classList.toggle('light'); b.textContent = document.body.classList.contains('light')?'☾':'☀'; return; }
            syncUI();
        });

        document.querySelectorAll('.btn.lang').forEach(initLangEvents);
        syncUI();
    })();
    """

def assemble_page(data):
    lang_row = "".join([f'<button class="btn lang" data-lang="{l}">{l}</button>' for l in data['languages']])
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Polyglot Dev Atlas</title>
        <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
        <style>{generate_styles()}</style>
    </head>
    <body>
        <script>window.__DATA__ = {json.dumps(data, default=asdict)};</script>
        <div class="app-layout" id="app-layout">
            <aside class="sidebar"><div class="sidebar-content">
                <div style="padding:24px; font-weight:900; color:var(--accent); border-bottom:1px solid var(--border); letter-spacing:1px">DEV ATLAS</div>
                <div id="sidebar-nav"></div>
            </div></aside>
            <main class="main">
                <header class="topbar">
                    <div class="stack-left">
                        <div class="row"><button class="btn" style="width:34px" onclick="toggleSidebar()">☰</button>{lang_row}</div>
                        <div class="row" id="view-list"></div>
                    </div>
                    <div class="stack-right">
                        <div class="row">
                            <button class="btn style" data-style="default">Amethyst</button>
                            <button class="btn style" data-style="ocean">Ocean</button>
                            <button class="btn style" data-style="sunset">Sunset</button>
                            <button id="themeToggle" class="btn" style="width:34px">☀</button>
                        </div>
                        <div class="row">
                            <button id="swapBtn" class="btn hidden">Swap</button>
                            <button id="compareBtn" class="btn">Compare</button>
                            <button id="courseBtn" class="btn">Course</button>
                        </div>
                    </div>
                </header>
                <div class="scroll-area" id="main-content"></div>
            </main>
        </div>
        <script>{generate_scripts()}</script>
    </body>
    </html>
    """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build the Polyglot Dev Atlas (index.html)')
    parser.add_argument('--watch', '-w', action='store_true', help='Watch content/ and rebuild on changes')
    parser.add_argument('--out', '-o', default='index.html', help='Output HTML filename')
    parser.add_argument('--lint', action='store_true', help='Validate all page JSON files against the schema and exit non-zero on failures')
    args = parser.parse_args()

    content_root = os.path.join(os.path.dirname(__file__), 'content')

    # If lint requested, run validation and exit with its status. If both lint and watch are provided,
    # validation must pass to continue into watch mode.
    if args.lint:
        try:
            from tools import validate_schema as _vs
            rc = _vs.validate_all(content_root)
            if rc != 0:
                print(f'Lint failed: exit {rc}')
                raise SystemExit(rc)
        except SystemExit:
            raise
        except Exception as e:
            print(f'Lint failed to run: {e}')
            raise SystemExit(2)

    def build_index() -> int:
        try:
            # If linting is enabled, validate before attempting to write output
            if args.lint:
                try:
                    from tools import validate_schema as _vs
                    rc = _vs.validate_all(content_root)
                    if rc != 0:
                        print(f'Validation failed: exit {rc}')
                        return rc
                except Exception as e:
                    print(f'Validation runner failed: {e}')
                    return 2

            content = load_mock_data()
            with open(args.out, 'w', encoding='utf-8') as f:
                f.write(assemble_page(content))
            print(f"Build complete: {args.out} at {time.strftime('%H:%M:%S')}")
            return 0
        except Exception as e:
            print(f"Build failed: {e}")
            return 1

    if not args.watch:
        rc = build_index()
        raise SystemExit(rc)

    # Watch mode
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except Exception:
        print('Watch mode requires `watchdog`. Install with: pip install watchdog')
        build_index()
        raise SystemExit(2)

    class DebounceHandler(FileSystemEventHandler):
        def __init__(self, debounce_seconds=0.5):
            super().__init__()
            self._timer = None
            self._lock = threading.Lock()
            self.debounce_seconds = debounce_seconds

        def _schedule(self):
            with self._lock:
                if self._timer:
                    self._timer.cancel()
                def _run_and_maybe_exit():
                    rc = build_index()
                    # If linting is enabled and validation failed, exit the process (CI-friendly)
                    if args.lint and rc != 0:
                        print(f'Validation failed during watch: exiting {rc}')
                        os._exit(rc)

                self._timer = threading.Timer(self.debounce_seconds, _run_and_maybe_exit)
                self._timer.daemon = True
                self._timer.start()

        def on_any_event(self, event):
            # ignore events for temporary files
            if event.src_path.endswith('~') or event.is_directory:
                return
            print(f'Change detected: {event.src_path}')
            self._schedule()

    content_root = os.path.join(os.path.dirname(__file__), 'content')
    paths_to_watch = [content_root, os.path.join(os.path.dirname(__file__), 'tools')]

    observer = Observer()
    handler = DebounceHandler(debounce_seconds=0.6)
    for p in paths_to_watch:
        if os.path.exists(p):
            observer.schedule(handler, path=p, recursive=True)

    print('Starting watch mode. Press Ctrl+C to stop.')
    build_index()
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopping watch...')
        observer.stop()
    observer.join()


def _map_alias_path(value: str, content_root: str) -> str:
    # Support a few helpful aliases
    if value.startswith('@snippets/'):
        return os.path.join(content_root, 'snippets', value[len('@snippets/'):])
    if value.startswith('@images/'):
        return os.path.join(content_root, 'images', value[len('@images/'):])
    if value.startswith('@core/'):
        return os.path.join(content_root, 'core', value[len('@core/'):])
    # default: treat as relative to content root
    return os.path.join(content_root, value.lstrip('./'))


def _resolve_ref_string(ref: str, content_root: str, cache: Dict[str, Any]):
    # Handle fragment part after '#'
    path_part, frag = (ref.split('#', 1) + [None])[:2]
    # map aliases and relative paths
    if path_part.startswith('@') or path_part.startswith('.') or not os.path.isabs(path_part):
        file_path = _map_alias_path(path_part, content_root)
    else:
        file_path = path_part

    if not os.path.isfile(file_path):
        # Maybe the ref was just a fragment within the same file (not supported here)
        return ref

    if file_path in cache:
        loaded = cache[file_path]
    else:
        try:
            with open(file_path, 'r', encoding='utf-8') as fh:
                if file_path.endswith('.json'):
                    loaded = json.load(fh)
                else:
                    loaded = fh.read()
        except Exception:
            return ref
        cache[file_path] = loaded

    if frag and isinstance(loaded, dict):
        # Support simple JSON Pointer style: /a/b/c
        parts = [p for p in frag.split('/') if p]
        cur = loaded
        for p in parts:
            if isinstance(cur, dict) and p in cur:
                cur = cur[p]
            else:
                return cur
        return cur

    return loaded


def resolve_refs(node: Any, content_root: str, cache: Dict[str, Any] = None):
    if cache is None:
        cache = {}

    if isinstance(node, dict):
        if '$ref' in node and isinstance(node['$ref'], str):
            resolved = _resolve_ref_string(node['$ref'], content_root, cache)
            # If resolved is a dict, merge; otherwise replace
            if isinstance(resolved, dict):
                node.pop('$ref', None)
                for k, v in resolved.items():
                    node[k] = resolve_refs(v, content_root, cache)
                return node
            else:
                return resolve_refs(resolved, content_root, cache)
        # otherwise walk children
        for k, v in list(node.items()):
            node[k] = resolve_refs(v, content_root, cache)
        return node

    if isinstance(node, list):
        for i, v in enumerate(node):
            node[i] = resolve_refs(v, content_root, cache)
        return node

    if isinstance(node, str):
        # support alias-based raw file injection
        if node.startswith('@'):
            # Resolve alias paths using the same resolver so JSON files become parsed structures
            try:
                resolved = _resolve_ref_string(node, content_root, cache)
                return resolve_refs(resolved, content_root, cache)
            except Exception:
                # fallback to raw file read
                p = _map_alias_path(node, content_root)
                if os.path.isfile(p):
                    try:
                        with open(p, 'r', encoding='utf-8') as fh:
                            return fh.read()
                    except Exception:
                        return node
        return node

    return node