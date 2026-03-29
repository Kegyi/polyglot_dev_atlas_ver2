import os
import json
import argparse
from dataclasses import dataclass
from typing import Optional


@dataclass
class State:
    primary: Optional[str] = "cpp"
    secondary: Optional[str] = None
    view: Optional[str] = None
    style: str = "default"
    compare: bool = False
    course: bool = False


def load_data(root_dir: Optional[str] = None) -> dict:
    base = root_dir or os.path.dirname(__file__)
    data_path = os.path.join(base, "content", "data", "data.json")
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "languages": {"order": ["cpp", "python", "go", "typescript", "scala2", "scala3"], "labels": {}},
            "view_categories": {"atlas": {"views": ["sheets", "patterns", "principles", "workflow"]},
                                 "learning": {"views": ["exercises", "basics", "interview", "problems"]}},
        }


def load_styles(root_dir: Optional[str] = None) -> list:
  base = root_dir or os.path.dirname(__file__)
  styles_dir = os.path.join(base, "content", "ui_styles")
  styles = []
  if os.path.isdir(styles_dir):
    for fname in sorted(os.listdir(styles_dir)):
      if not fname.lower().endswith('.json'):
        continue
      path = os.path.join(styles_dir, fname)
      try:
        with open(path, 'r', encoding='utf-8') as f:
          j = json.load(f)
        sid = j.get('id') or os.path.splitext(fname)[0]
        styles.append({'id': sid, 'label': j.get('label', sid), 'vars': j.get('vars', {})})
      except Exception:
        continue
  if not styles:
    styles = [
      {'id': 'default', 'label': 'Default', 'vars': {}},
      {'id': 'ocean', 'label': 'Ocean', 'vars': {}},
      {'id': 'sunset', 'label': 'Sunset', 'vars': {}},
    ]
  return styles


def generate_styles() -> str:
  return """
  :root{--bg:#0f1724;--panel:#0b1220;--accent:#8b5cf6;--accent2:#06b6d4;--muted:#94a3b8;--selected:#111827}
  body{font-family:Inter,Segoe UI,Arial; margin:0;background:var(--bg);color:#e6eef8}
  .topbar{display:flex;align-items:center;justify-content:space-between;padding:14px 18px}
  .controls{display:flex;gap:8px;align-items:center}
  .btn{background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--muted);padding:6px 10px;border-radius:6px;cursor:pointer}
  .btn.selected{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#061226;border:none}
  .btn.secondary{border-style:dashed}
  .content{padding:20px}
  .toolbar-right{display:flex;gap:8px;align-items:center}
  .swap{margin-left:6px}
  .panel{background:var(--panel);padding:16px;border-radius:8px}
  .view-list .panel{display:inline-block;padding:6px;border-radius:6px}
  .btn.lang.drag-preview-right{transform:translateX(8px);box-shadow:0 8px 20px rgba(2,6,23,0.55);transition:transform 180ms ease,box-shadow 180ms ease}
  .btn.lang.drag-preview-left{transform:translateX(-8px);box-shadow:0 8px 20px rgba(2,6,23,0.55);transition:transform 180ms ease,box-shadow 180ms ease}
  .btn.lang.active-left{background:linear-gradient(90deg,var(--accent),color-mix(in srgb,var(--accent) 70%, #000000 10%));color:#061226}
  .btn.lang.active-right{background:linear-gradient(90deg,var(--accent2),color-mix(in srgb,var(--accent2) 70%, #000000 10%));color:#061226}
  .panel.hidden{display:none}
  .lang-list{display:flex;gap:6px}
  .hidden{display:none}
  .theme-toggle{width:36px;height:36px;display:inline-flex;align-items:center;justify-content:center;border-radius:8px}
  .theme-icon{font-size:16px}
  body.light{--bg:#f8fafc;--panel:#ffffff;--accent:#7c3aed;--accent2:#06b6d4;--muted:#475569;color:#0b1220}
  .view-list .panel{display:inline-block;padding:6px;border-radius:6px}
  @media(min-width:900px){.content{max-width:1100px;margin:20px auto}}
  """


def generate_scripts() -> str:
    return """
    (() => {
      const qs = s=>document.querySelector(s);
      const data = window.__DATA__ || {};
      const STORAGE_KEY = 'polyglot_ui_state_v1';

      function saveStateToStorage(state){
        try{
          const toSave = {
            primary: (typeof state.primary !== 'undefined') ? state.primary : null,
            secondary: (typeof state.secondary !== 'undefined') ? state.secondary : null,
            view: (typeof state.view !== 'undefined') ? state.view : null,
            style: (typeof state.style !== 'undefined') ? state.style : null,
            compare: !!state.compare,
            course: !!state.course,
            lastAtlas: (typeof state.lastAtlas !== 'undefined') ? state.lastAtlas : null,
            lastLearning: (typeof state.lastLearning !== 'undefined') ? state.lastLearning : null
          };
          localStorage.setItem(STORAGE_KEY, JSON.stringify(toSave));
        }catch(e){/* ignore storage errors */}
      }

      function loadStateFromStorage(state){
        try{
          const raw = localStorage.getItem(STORAGE_KEY);
          if(!raw) return state;
          const s = JSON.parse(raw);
          state.primary = (typeof s.primary !== 'undefined') ? s.primary : state.primary;
          state.secondary = (typeof s.secondary !== 'undefined') ? s.secondary : state.secondary;
          state.view = (typeof s.view !== 'undefined') ? s.view : state.view;
          state.style = (typeof s.style !== 'undefined') ? s.style : state.style;
          state.compare = (typeof s.compare !== 'undefined') ? !!s.compare : state.compare;
          state.course = (typeof s.course !== 'undefined') ? !!s.course : state.course;
          state.lastAtlas = (typeof s.lastAtlas !== 'undefined') ? s.lastAtlas : state.lastAtlas;
          state.lastLearning = (typeof s.lastLearning !== 'undefined') ? s.lastLearning : state.lastLearning;
        }catch(e){/* ignore parse errors */}
        return state;
      }

      function chooseNextLang(current){
        const order = (data.languages && data.languages.order) || [];
        if(!order || order.length===0) return '';
        for(let i=0;i<order.length;i++){
          if(order[i]!==current) return order[i];
        }
        return order[0]||'';
      }

      function setSecondary(lang){
        if(!window.appState.compare) window.appState.compare = true;
        window.appState.secondary = lang;
      }

      function setPrimary(lang){
        if(window.appState.primary === lang){
          if(window.appState.compare && window.appState.secondary){
            window.appState.primary = window.appState.secondary;
            window.appState.secondary = null;
            window.appState.compare = false;
          }
          return;
        }
        window.appState.primary = lang;
        if(window.appState.primary === window.appState.secondary){
          if(window.appState.compare){
            const next = chooseNextLang(window.appState.primary);
            window.appState.secondary = (next === window.appState.primary) ? null : next;
            if(!window.appState.secondary) window.appState.compare = false;
          } else {
            window.appState.secondary = null;
          }
        }
      }

      function toggleSecondary(lang){
        if(window.appState.compare && window.appState.secondary === lang){
          window.appState.secondary = null;
          window.appState.compare = false;
          return;
        }
        if(window.appState.primary === lang){
          if(window.appState.compare && window.appState.secondary){
            window.appState.primary = window.appState.secondary;
            window.appState.secondary = null;
            window.appState.compare = false;
          }
          return;
        }
        setSecondary(lang);
      }

      function normalizeState(){
        if(!window.appState.compare){
          window.appState.secondary = null;
        }
        if(window.appState.secondary && window.appState.primary === window.appState.secondary){
          const next = chooseNextLang(window.appState.primary);
          if(next && next!==window.appState.primary){
            window.appState.secondary = next;
          } else {
            window.appState.secondary = null;
            window.appState.compare = false;
          }
        }
      }

      function swap(){
        const tmp = window.appState.primary; window.appState.primary = window.appState.secondary; window.appState.secondary = tmp;
      }

      function toggleCompare(){
        window.appState.compare = !window.appState.compare;
        if(window.appState.compare && !window.appState.secondary){
          window.appState.secondary = chooseNextLang(window.appState.primary);
          if(window.appState.secondary===window.appState.primary){
            window.appState.secondary = null;
            window.appState.compare = false;
          }
        }
        if(!window.appState.compare){
          window.appState.secondary = null;
        }
      }

      function renderViews(state){
          const atlas = (data.view_categories && data.view_categories.atlas && data.view_categories.atlas.views) || [];
          const learning = (data.view_categories && data.view_categories.learning && data.view_categories.learning.views) || [];
          const categoryKey = state.course ? 'learning' : 'atlas';
          const visible = categoryKey === 'atlas' ? atlas : learning;
          const viewNav = qs('#viewNav');
          if(!viewNav) return;
          viewNav.innerHTML = visible.map(v => `<button class="btn view${v===state.view ? ' selected' : ''}" data-view="${v}">${v}</button>`).join(' ');
      }

      function updateUI(state){
        document.querySelectorAll('.btn.lang').forEach(b=>{
          b.classList.remove('active-left','active-right','selected');
          const key = b.dataset.lang;
          if(state.compare){
            if(state.primary===key) b.classList.add('active-left');
            if(state.secondary===key) b.classList.add('active-right');
          } else {
            if(state.primary===key) b.classList.add('active-left');
          }
        });
        const compareBtn = qs('#compareBtn');
        if(compareBtn) compareBtn.classList.toggle('selected', !!state.compare);
        document.querySelectorAll('.btn.style').forEach(b=>b.classList.toggle('selected', b.dataset.style===state.style));
        qs('#swapBtn').classList.toggle('hidden', !state.compare || !state.secondary);
        qs('#courseBtn').classList.toggle('selected', !!state.course);
        renderViews(state);
        document.querySelectorAll('.btn.view').forEach(b=>b.classList.toggle('selected', b.dataset.view===state.view));
        try{ normalizeState(); }catch(e){}
        try{ saveStateToStorage(state); }catch(e){}
      }

      window.appState = {primary:'cpp', secondary:null, view:null, style:'default', compare:false, course:false, lastAtlas:null, lastLearning:null};

      function toggleTheme(){
        const isLight = document.body.classList.toggle('light');
        const icon = qs('#themeIcon');
        icon.textContent = isLight ? '☀' : '☾';
      }

      let langDrag = null;
      const DRAG_THRESHOLD = 18;

      document.addEventListener('pointerdown', e=>{
        const btn = e.target.closest('.btn.lang');
        if(!btn) return;
        langDrag = {startX: e.clientX, btn: btn, lang: btn.dataset.lang, moved:false};
      });

      document.addEventListener('pointermove', e=>{
        if(!langDrag) return;
        const dx = e.clientX - langDrag.startX;
        if(Math.abs(dx) > DRAG_THRESHOLD){
          langDrag.moved = true;
          langDrag.btn.classList.toggle('drag-preview-right', dx>0);
          langDrag.btn.classList.toggle('drag-preview-left', dx<0);
        }
      });

      document.addEventListener('pointerup', e=>{
        if(!langDrag) return;
        const dx = e.clientX - langDrag.startX;
        langDrag.btn.classList.remove('drag-preview-right','drag-preview-left');
        if(langDrag.moved && Math.abs(dx) > DRAG_THRESHOLD){
          if(dx>0){
            // drag-right acts like right-click (secondary slot)
            const lang = langDrag.lang;
            if(window.appState.compare && window.appState.secondary === lang){
              window.appState.secondary = null; window.appState.compare = false;
            } else if(window.appState.compare && window.appState.primary === lang){
              swap();
            } else {
              setSecondary(lang);
            }
          } else {
            setPrimary(langDrag.lang);
          }
          updateUI(window.appState);
        }
        langDrag = null;
      });

      document.addEventListener('contextmenu', e=>{
        const btn = e.target.closest('.btn.lang');
        if(!btn) return;
        e.preventDefault();
        const lang = btn.dataset.lang;
        // right-click targets secondary slot
        if(window.appState.compare && window.appState.secondary === lang){
          window.appState.secondary = null; window.appState.compare = false;
        } else if(window.appState.compare && window.appState.primary === lang){
          swap();
        } else {
          setSecondary(lang);
        }
        updateUI(window.appState);
      });

      document.addEventListener('click', e=>{
        const btn = e.target.closest('.btn');
        if(btn){
          if(btn.classList.contains('lang')){
            const lang = btn.dataset.lang;
            if(window.appState.compare){
              if(window.appState.secondary === lang){
                swap();
              } else {
                setPrimary(lang);
              }
            } else {
              setPrimary(lang);
            }
            updateUI(window.appState);
            return;
          }
          if(btn.classList.contains('view')){
            const v = btn.dataset.view;
            if(window.appState.view === v){
              // deselect if already selected and clear last stored view for the category
              window.appState.view = null;
              if(window.appState.course){ window.appState.lastLearning = null; } else { window.appState.lastAtlas = null; }
            } else {
              window.appState.view = v;
              if(window.appState.course){ window.appState.lastLearning = window.appState.view; } else { window.appState.lastAtlas = window.appState.view; }
            }
            updateUI(window.appState);
            return;
          }
          if(btn.classList.contains('style')){ window.appState.style = btn.dataset.style; updateUI(window.appState); return; }
          if(btn.id==='compareBtn'){ toggleCompare(); updateUI(window.appState); return; }
          if(btn.id==='swapBtn'){ swap(); updateUI(window.appState); return; }
          if(btn.id==='courseBtn'){ window.appState.course = !window.appState.course; window.appState.view = window.appState.course ? (window.appState.lastLearning || null) : (window.appState.lastAtlas || null); updateUI(window.appState); return; }
          if(btn.id==='themeToggle'){ toggleTheme(); return; }
        }
        if(e.target.closest('#themeToggle')){ toggleTheme(); }
      });

      document.addEventListener('DOMContentLoaded', ()=>{
        loadStateFromStorage(window.appState);
        updateUI(window.appState);
      });
      document.addEventListener('DOMContentLoaded', ()=>{ const s = qs('#jsStatus'); if(s){ s.textContent = 'JS active'; s.style.color = '#34d399'; } });
    })();
    """


def generate_controls_html(data: dict, state: State) -> str:
    langs = data.get('languages', {}).get('order', ['cpp', 'python'])
    labels = data.get('languages', {}).get('labels', {})
    lang_buttons = ' '.join(
      '<button class="btn lang" data-lang="{lang}">{label}</button>'.format(
        lang=l,
        label=labels.get(l, l)
      ) for l in langs
    )

    view_cats = data.get('view_categories', {})
    atlas_views = view_cats.get('atlas', {}).get('views', [])
    learning_views = view_cats.get('learning', {}).get('views', [])

    def mk_buttons(views):
      return ' '.join(
        '<button class="btn view" data-view="{v}">{label}</button>'.format(v=v, label=v)
        for v in views
      )

    # we emit a single view navigation container (`#viewNav`) and let client-side
    # script render the correct view buttons based on appState (no default selection)
    atlas_buttons = mk_buttons(atlas_views)
    learning_buttons = mk_buttons(learning_views)
    course_selected = ' selected' if state.course else ''

    styles = load_styles()
    style_buttons = ' '.join(
        '<button class="btn style{sel}" data-style="{id}">{label}</button>'.format(
            sel=(' selected' if s['id'] == state.style else ''), id=s['id'], label=s['label']
        ) for s in styles
    )

    return f"""
    <div class=topbar>
      <div class=controls>
        <div class=lang-list>{lang_buttons}</div>
        <div style='width:12px'></div>
        <div class=view-list>
          <div id="viewNav" class="panel"></div>
        </div>
      </div>
      <div class=toolbar-right>
        <div class=style-list>{style_buttons}</div>
          <button id=compareBtn class=btn>Compare</button>
          <button id=swapBtn class='btn swap hidden'>Swap</button>
          <label for=courseToggle id=courseBtn class='btn{course_selected}'>Course</label>
        <button id=themeToggle class='btn theme-toggle' title='Toggle theme'><span id=themeIcon class='theme-icon'>☾</span></button>
      </div>
    </div>
    """


def assemble_page(data: dict, state: State) -> str:
    head = f"<meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>UI Skeleton</title>"
    styles = f"<style>{generate_styles()}</style>"
    scripts = f"<script>{generate_scripts()}</script>"
    controls = generate_controls_html(data, state)
    body = f"<div class=panel>{controls}<div class=content><div class=panel><h3>Rendered page content (placeholder)</h3><p>This area will show generated content in the next step.</p></div></div></div>"
    # visible build timestamp and JS status for debugging in previews
    import datetime
    ts = datetime.datetime.utcnow().isoformat() + 'Z'
    stamp = f"<div style=\"position:fixed;right:12px;bottom:12px;background:rgba(0,0,0,0.5);padding:8px;border-radius:6px;font-size:12px;color:#dbeafe\">Built: {ts} <span id=\"jsStatus\" style=\"margin-left:8px;color:#f97316\">JS inactive</span></div>"
    # embed the data used by the page so the client-side renderer can rebuild views
    data_blob = json.dumps(data).replace('</', '<\/')
    data_script = f"<script>window.__DATA__ = {data_blob};</script>"
    return f"<!doctype html><html><head>{head}{styles}</head><body>{data_script}{body}{stamp}{scripts}</body></html>"


def write_output(html: str, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    parser = argparse.ArgumentParser(description='Generate UI skeleton HTML')
    parser.add_argument('--out', '-o', default=os.path.join(os.path.dirname(__file__), 'build', 'ui_skeleton.html'))
    parser.add_argument('--data-root', '-d', default=None)
    args = parser.parse_args()
    data = load_data(args.data_root)
    state = State()
    html = assemble_page(data, state)
    write_output(html, args.out)
    print('Wrote', args.out)


if __name__ == '__main__':
    main()
