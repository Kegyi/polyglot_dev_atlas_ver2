import os
import json
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict

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
    data_json_path = os.path.join(os.path.dirname(__file__), "content", "data", "data.json")
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
    base_dir = os.path.join(os.path.dirname(__file__), "content", "pages")
    views_flat = [v for vals in view_categories.values() for v in vals]
    views_map = {v.lower(): v for v in views_flat}

    if os.path.isdir(base_dir):
        for fname in sorted(os.listdir(base_dir)):
            if not fname.endswith('.page.json'): continue
            key = fname[:-len('.page.json')]
            match_view = views_map.get(key.lower())
            with open(os.path.join(base_dir, fname), 'r', encoding='utf-8') as f:
                try: obj = json.load(f)
                except Exception: continue

            groups_map = {k: v.get('title', k) for k, v in obj.get('groups', {}).items()}
            for slug, item in obj.get('content', {}).items():
                group_key = item.get('group', 'groupTitle')
                insight = item['points'][0] if item.get('points') else (item['notes'][0] if item.get('notes') else '')
                sub_contents = []
                if item.get('points'): sub_contents.append({"title": "Points", "text": "\n".join(item.get('points', []))})
                if item.get('notes'): sub_contents.append({"title": "Notes", "text": "\n".join(item.get('notes', []))})

                pages.append({
                    "id": f"{key}_{slug}", "group": group_key, "group_title": groups_map.get(group_key, group_key),
                    "view": match_view or obj.get('page') or key, "title": item.get('title', ''),
                    "description": item.get('description', ''), "insight": insight,
                    "code_snippets": item.get('code_snippets', {}) or item.get('code', {}),
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
            qs('#main-content').innerHTML = `
                <div class="content-wrap">
                    <h1 style="font-size:42px; margin:0; letter-spacing:-1px">${p.title}</h1>
                    <p style="font-size:18px; color:var(--text-m); margin:20px 0; line-height:1.6">${p.description}</p>
                    <div style="background:rgba(129,140,248,0.1); padding:24px; border-radius:12px; border-left:4px solid var(--accent); margin-bottom:40px">
                        <div style="font-size:10px;font-weight:800;color:var(--text-m);text-transform:uppercase;margin-bottom:8px">Core Insight</div>
                        <div style="line-height:1.5">${p.insight}</div>
                    </div>
                    <div class="code-grid ${state.compare?'split':''}">
                        <div class="code-box"><div class="code-label">${state.primary || 'No Language'}</div><pre><code>${state.primary ? (p.code_snippets[state.primary] || '// No snippet') : ''}</code></pre></div>
                        ${state.compare && state.secondary ? `<div class="code-box"><div class="code-label">${state.secondary}</div><pre><code>${p.code_snippets[state.secondary] || '// No snippet'}</code></pre></div>` : ''}
                    </div>
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
    content = load_mock_data()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(assemble_page(content))
    print("Build complete: index.html")