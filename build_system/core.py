import os
import shutil
import re
import json

class AtlasBuilder:
    def __init__(self):
        # Path Configuration
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.dist_dir = os.path.join(self.base_dir, "dist")
        self.content_dir = os.path.join(self.base_dir, "content")
        self.templates_dir = os.path.join(self.base_dir, "templates")
        self.assets_dir = os.path.join(self.base_dir, "assets")
        self.pages_dir = os.path.join(self.content_dir, "pages")
        self.lang_def_path = os.path.join(self.content_dir, "definitions", "languages.json")
        
        # Build Status & Registry
        self.site_registry = {} 
        self.warnings = []

    def _log_warning(self, message):
        print(f"⚠️  WARNING: {message}")
        self.warnings.append(message)

    def _read_file(self, path, required=False):
        if not os.path.exists(path):
            if required: self._log_warning(f"Missing required file: {path}")
            return ""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def _load_json(self, path, required=False):
        if not os.path.exists(path):
            if required: self._log_warning(f"Missing required JSON: {path}")
            return {}
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            self._log_warning(f"Malformed JSON in {path}: {str(e)}")
            return {}

    # --- RECURSIVE SCHEMA RENDERER ---

    def render_content(self, content_list, depth=2):
        """Recursively renders the 'content' array based on the JSON Schema."""
        html = ""
        for item in content_list:
            html += self.render_item(item, depth)
        return html

    def render_item(self, item, depth=2):
        """Maps specific JSON items to HTML strings."""
        itype = item.get("type")
        custom_class = item.get("class", "")
        item_id = item.get("id", "")
        id_attr = f'id="{item_id}"' if item_id else ""

        # 1. Headers (Direct)
        if itype in ["h1", "h2", "h3", "h4", "h5", "h6", "title"]:
            tag = "h1" if itype == "title" else itype
            return f'<{tag} {id_attr} class="{custom_class}">{item.get("text")}</{tag}>'

        # 2. Text Paragraphs
        elif itype == "text":
            text = item.get("text", "")
            return f'<p {id_attr} class="{custom_class}">{text}</p>'

        # 3. Notes / Callouts
        elif itype == "note":
            variant = item.get("variant", "info")
            return f'<div {id_attr} class="note note-{variant} {custom_class}">{item.get("text")}</div>'

        # 4. Code Comparison (Assembler)
        elif itype == "code":
            return self.assemble_code_comparison(item.get("name"))

        # 5. Images
        elif itype == "image":
            alt = item.get("alt", "")
            src = item.get("src", "")
            return f'<figure class="{custom_class}"><img src="{src}" alt="{alt}"><figcaption>{item.get("caption", "")}</figcaption></figure>'

        # 6. Lists
        elif itype == "list":
            tag = "ol" if item.get("ordered") else "ul"
            list_items = "".join([f"<li>{i}</li>" for i in item.get("items", [])])
            return f'<{tag} class="{custom_class}">{list_items}</{tag}>'

        # 7. Blocks Container (Recursion point)
        elif itype == "blocks":
            block_html = ""
            for block in item.get("blocks", []):
                block_html += self.render_block(block, depth)
            return f'<div {id_attr} class="blocks-container {custom_class}">{block_html}</div>'

        return f"<!-- Unknown item type: {itype} -->"

    def render_block(self, block_data, depth=2):
        """Renders a single collapsible Topic Block with dynamic heading levels."""
        bid = block_data.get("id", "topic-unknown")
        title = block_data.get("title", "Untitled Topic")
        custom_class = block_data.get("class", "")
        collapsed = "is-collapsed" if block_data.get("collapsed") else ""
        body_class = "collapsed" if block_data.get("collapsed") else ""
        
        # Determine heading tag based on nesting depth
        h_tag = f"h{min(depth, 6)}"

        html = f'''
        <div class="topic-section {collapsed} {custom_class}" id="{bid}">
            <div class="topic-header" onclick="app.toggleTopic('{bid}')">
                <{h_tag}>{title}</{h_tag}>
                <div class="arrow">^</div>
            </div>
            <div class="topic-body {body_class}">
                {self.render_content(block_data.get("content", []), depth + 1)}
            </div>
        </div>
        '''
        return html

    # --- ASSEMBLERS ---

    def assemble_code_comparison(self, snippet_id):
        snippet_root = os.path.join(self.content_dir, "snippets")
        html = '<div class="comparison-grid">'
        found_any = False
        if os.path.exists(snippet_root):
            for lang_dir in sorted(os.listdir(snippet_root)):
                dir_path = os.path.join(snippet_root, lang_dir)
                if not os.path.isdir(dir_path): continue
                target = next((f for f in os.listdir(dir_path) if f.startswith(f"{snippet_id}.")), None)
                if target:
                    found_any = True
                    raw_code = self._read_file(os.path.join(dir_path, target))
                    escaped = raw_code.replace('<', '&lt;').replace('>', '&gt;')
                    html += f'<div class="code-card" data-lang="{lang_dir}"><span class="lang-tag">{lang_dir.upper()}</span><pre><code>{escaped}</code></pre></div>'
        
        if not found_any:
            self._log_warning(f"Snippet '{snippet_id}' not found.")
            return f'<div class="build-error" style="padding:1rem; border:1px solid var(--sel-l); color:var(--sel-l); margin:1rem 0; border-radius:8px; font-family:monospace; font-size:0.8rem;">⚠️ Snippet Error: "{snippet_id}" missing in content/snippets/*/</div>'
        return html + '</div>'

    def assemble_navigation(self, current_page_id, prefix, active_mode):
        nav_html = '<ul class="nav-list">'
        for p in self.site_registry.get(active_mode, []):
            active = "active" if p['id'] == current_page_id else ""
            nav_html += f'<li class="{active}"><a href="{prefix}{p["url"]}">{p["title"]}</a></li>'
        return nav_html + '</ul>'

    def assemble_topic_sidebar(self, page_data):
        """Extracts block IDs recursively to build the Table of Contents."""
        # Build a nested TOC: top-level group blocks -> their child blocks
        def gather_subblocks(items):
            """Recursively find all 'blocks' entries inside items and return their block list."""
            subs = []
            for it in items:
                if it.get("type") == "blocks":
                    for b in it.get("blocks", []):
                        subs.append({"id": b.get("id"), "title": b.get("title")})
                # descend into known container slots
                if isinstance(it, dict):
                    if "blocks" in it:
                        for b in it.get("blocks", []):
                            # each block may itself contain nested 'content' with blocks
                            if isinstance(b, dict) and "content" in b:
                                subs.extend(gather_subblocks(b.get("content", [])))
                    if "content" in it:
                        subs.extend(gather_subblocks(it.get("content", [])))
            return subs

        toc_html = []

        # Container for topic sidebar (view-mode control is rendered in the template)
        toc_html.append('<div class="topic-sidebar-container">')

        toc_html.append('<ul class="nav-list" id="toc">')

        # Top-level: look for blocks items in the page content that represent groups
        for item in page_data.get("content", []):
            if item.get("type") != "blocks":
                continue
            # each top-level block in this item is a group (e.g., creational_patterns)
            for group in item.get("blocks", []):
                gid = group.get("id")
                gtitle = group.get("title", "Untitled")
                # collect immediate child blocks under this group's content
                children = []
                if isinstance(group, dict):
                    # find nested 'blocks' within group's content recursively
                    children = gather_subblocks(group.get("content", []))

                # render group title as clickable header and attach data-topic-id to the group li
                toc_html.append(f'<li class="toc-group" data-topic-id="{gid}"><span onclick="app.focusTopic(\'{gid}\')">{gtitle}</span>')
                if children:
                    toc_html.append('<ul class="nav-sublist">')
                    for c in children:
                        # render each child with a data-topic-id for reliable selection
                        toc_html.append(f'<li data-topic-id="{c["id"]}" onclick="app.focusTopic(\'{c["id"]}\')">{c["title"]}</li>')
                    toc_html.append('</ul>')
                toc_html.append('</li>')

        toc_html.append('</ul>')
        toc_html.append('</div>')
        return "".join(toc_html)

    def assemble_language_selector(self):
        data = self._load_json(self.lang_def_path, required=True)
        if not data: return "<!-- Lang Def Missing -->"
        html = '<div class="selector-container">'
        for lid, info in data.items():
            color = info.get("color", "var(--accent)")
            html += f'<button class="lang-pill" data-lang-id="{lid}" style="--lang-color: {color}">{info.get("name", lid)}</button>'
        html += '<button class="swap-btn" onclick="app.swapLanguages()">⇄ SWAP</button></div>'
        return html

    def assemble_mode_switcher(self, active_mode, prefix):
        html = '<div class="mode-switcher">'
        targets = {"atlas": "index.html", "course": "course/intro.html"}
        for m in sorted(self.site_registry.keys()):
            active = "active" if m == active_mode else ""
            target_url = prefix + targets.get(m, "index.html")
            html += f'<a href="{target_url}" class="mode-btn {active}">{m.capitalize()}</a>'
        return html + '</div>'

    # --- BUILD PROCESS ---

    def process_page(self, page_entry):
        data = self._load_json(page_entry['path'], required=True)
        rel_path = page_entry['rel_path']
        depth = rel_path.count(os.sep) + (1 if rel_path else 0)
        prefix = "./" if depth == 0 else "../" * depth
        mode = rel_path.split(os.sep)[0] if rel_path else "atlas"

        template_file = data.get('template', 'base.html')
        template = self._read_file(os.path.join(self.templates_dir, template_file), required=True)
        if not template: return

        # Render Content via Schema Logic
        page_html = self.render_content(data.get("content", []), depth=2)

        # Placeholder Replacement
        output = template.replace("{{ title }}", data.get("title", "Polyglot Atlas"))
        output = output.replace("{{ asset_prefix }}", prefix)
        output = output.replace("{{ mode_switcher }}", self.assemble_mode_switcher(mode, prefix))
        output = output.replace("{{ language_selection_buttons }}", self.assemble_language_selector())
        output = output.replace("{{ navigation_sidebar }}", self.assemble_navigation(page_entry['id'], prefix, mode))
        output = output.replace("{{ topic_sidebar }}", self.assemble_topic_sidebar(data))
        output = output.replace("{{ content }}", page_html)
        output = output.replace("{{ body_class_placeholders }}", f"mode-{mode} {data.get('body_class', '')}")

        # Extra Assets
        extras = []
        for a in data.get('extra_assets', []):
            tag = f'<link rel="stylesheet" href="{prefix}assets/css/{a}">' if a.endswith('.css') else f'<script src="{prefix}assets/js/{a}"></script>'
            extras.append(tag)
        output = output.replace("{{ extra_assets }}", "\n".join(extras))

        # Save
        out_dir = os.path.join(self.dist_dir, rel_path)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f"{page_entry['id']}.html"), 'w', encoding='utf-8') as f:
            f.write(output)

    def build(self):
        print("🛠️  Initializing Build Process...")
        self.warnings = []
        self.site_registry = {}
        if os.path.exists(self.dist_dir): shutil.rmtree(self.dist_dir)
        os.makedirs(self.dist_dir)

        # 1. Scan folders to build the site map
        for root, _, files in os.walk(self.pages_dir):
            rel = os.path.relpath(root, self.pages_dir)
            if rel == ".": rel = ""
            mode = rel.split(os.sep)[0] if rel else "atlas"
            if mode not in self.site_registry: self.site_registry[mode] = []
            for f in files:
                if f.endswith('.json'):
                    p_id = f.replace('.json', '')
                    p_path = os.path.join(root, f)
                    p_data = self._load_json(p_path)
                    self.site_registry[mode].append({
                        "id": p_id, "title": p_data.get("title", p_id),
                        "url": os.path.join(rel, p_id + ".html").replace("\\", "/"),
                        "path": p_path, "rel_path": rel
                    })

        # 2. Generate pages from registry
        for mk in sorted(self.site_registry.keys()):
            for pe in self.site_registry[mk]:
                self.process_page(pe)

        # 3. Static Asset Sync
        if os.path.exists(self.assets_dir):
            shutil.copytree(self.assets_dir, os.path.join(self.dist_dir, "assets"))
        
        locales_src = os.path.join(self.content_dir, "locales")
        if os.path.exists(locales_src):
            shutil.copytree(locales_src, os.path.join(self.dist_dir, "content", "locales"))

        print("-" * 30)
        if self.warnings:
            print(f"✅ Build complete with {len(self.warnings)} warning(s).")
        else:
            print("✨ Build finished successfully.")

if __name__ == "__main__":
    AtlasBuilder().build()