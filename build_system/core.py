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
        print(f"WARNING: {message}")
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

    def render_content(self, content_list, depth=2, inherited_style=""):
        """Recursively renders content. Inherits styles and increments depth for smart titles."""
        html = ""
        for item in content_list:
            html += self.render_item(item, depth, inherited_style)
        return html

    def render_item(self, item, depth=2, inherited_style=""):
        itype = item.get("type")
        custom_class = item.get("class", "")
        item_id = item.get("id", "")
        id_attr = f'id="{item_id}"' if item_id else ""

        # Smart Heading Scaling
        if itype == "title":
            tag = f"h{min(depth, 6)}"
            return f'<{tag} {id_attr} class="{custom_class}">{item.get("text")}</{tag}>'
        
        elif itype in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            return f'<{itype} {id_attr} class="{custom_class}">{item.get("text")}</{itype}>'

        elif itype == "text":
            text = item.get("text", "")
            return f'<p {id_attr} class="{custom_class}">{text}</p>'

        elif itype == "note":
            variant = item.get("variant", "info")
            # Wrap note content in a dedicated container so inner block elements
            # (tables, pre, code) can be targeted separately by CSS and render
            # correctly inside the flexible note layout.
            content_html = item.get("text", "")
            return f'<div {id_attr} class="note note-{variant} {custom_class}"><div class="note-content">{content_html}</div></div>'

        elif itype == "code":
            return self.assemble_code_comparison(item.get("name"))

        elif itype == "image":
            alt = item.get("alt", "")
            src = item.get("src", "")
            return f'<figure class="{custom_class}"><img src="{src}" alt="{alt}"><figcaption>{item.get("caption", "")}</figcaption></figure>'

        elif itype == "list":
            tag = "ol" if item.get("ordered") else "ul"
            list_items = "".join([f"<li>{i}</li>" for i in item.get("items", [])])
            return f'<{tag} class="{custom_class}">{list_items}</{tag}>'

        elif itype == "blocks":
            block_html = ""
            for block in item.get("blocks", []):
                block_html += self.render_block(block, depth, inherited_style)
            return f'<div {id_attr} class="blocks-container {custom_class}">{block_html}</div>'

        return f"<!-- Unknown item type: {itype} -->"

    def render_block(self, block_data, depth=2, inherited_style=""):
        """Renders a collapsible block with inheritance and depth-based visibility logic."""
        bid = block_data.get("id", "topic-unknown")
        title = block_data.get("title", "Untitled Topic")
        custom_class = block_data.get("class", "")
        
        # Style Inheritance
        # If the block defines a `style` key (even empty string), treat it as an explicit override.
        # Only inherit when `style` is not present on the block.
        if "style" in block_data:
            current_style = block_data.get("style", "")
        else:
            current_style = inherited_style
        
        # Smart Heading Calculation
        h_tag = f"h{min(depth, 6)}"

        # Visibility Depth (Default: Top 2 levels expanded)
        is_manual_collapsed = block_data.get("collapsed")
        if is_manual_collapsed is None:
            should_collapse = depth > 3 # Level 1 (depth 2) and Level 2 (depth 3) are visible
        else:
            should_collapse = is_manual_collapsed

        collapsed_class = "is-collapsed" if should_collapse else ""
        body_class = "collapsed" if should_collapse else ""

        html = f'''
        <div class="topic-section {current_style} {collapsed_class} {custom_class}" id="{bid}">
            <div class="topic-header" onclick="app.toggleTopic('{bid}')">
                <{h_tag}>{title}</{h_tag}>
                <div class="arrow">^</div>
            </div>
            <div class="topic-body {body_class}">
                {self.render_content(block_data.get("content", []), depth + 1, current_style)}
            </div>
        </div>
        '''
        return html

    # --- ASSEMBLERS (PHASE 2: Depth-Tagged Sidebars) ---

    def assemble_code_comparison(self, snippet_id):
        snippet_root = os.path.join(self.content_dir, "snippets")
        html = f'<div class="code-comparison-grid" data-snippet-id="{snippet_id}">'
        found_any = False
        
        hljs_map = {"scala2": "scala", "scala3": "scala", "typescript": "ts"}

        if os.path.exists(snippet_root):
            for lang_dir in sorted(os.listdir(snippet_root)):
                dir_path = os.path.join(snippet_root, lang_dir)
                if not os.path.isdir(dir_path): continue
                target = next((f for f in os.listdir(dir_path) if f.startswith(f"{snippet_id}.")), None)
                if target:
                    found_any = True
                    raw_code = self._read_file(os.path.join(dir_path, target))
                    escaped = raw_code.replace('<', '&lt;').replace('>', '&gt;')
                    hljs_lang = hljs_map.get(lang_dir, lang_dir)
                    html += (f'<div class="code-block" data-lang="{lang_dir}">'
                             f'<div class="block-header-tag">{lang_dir.upper()}</div>'
                             f'<pre><code class="language-{hljs_lang}">{escaped}</code></pre></div>')
        
        if not found_any:
            self._log_warning(f"Snippet '{snippet_id}' not found.")
            # Emphasize the label so it stands out visually inside the note.
            content_html = f"<span class=\"snippet-error\">Snippet Error:</span> \"{snippet_id}\" missing"
            return f'<div class="note note-error"><div class="note-content">{content_html}</div></div>'
        return html + '</div>'

    def assemble_navigation(self, current_page_url, prefix, active_mode):
        # Primary nav and a hidden showcases list. The JS toggles between them.
        nav_html = ''

        def format_title_for_sidebar(title, cutoff=30):
            # Manual break marker
            if '|' in title:
                first, rest = title.split('|', 1)
                return f"{first.strip()}<span class=\"sidebar-wrap-indent\">{rest.strip()}</span>"

            # If shorter than cutoff, return unchanged
            if len(title) <= cutoff:
                return title

            # Try to break at common delimiters before cutoff
            for d in [';', ',', '.', '-', ':']:
                idx = title.rfind(d, 0, cutoff)
                if idx != -1:
                    a = title[:idx+1].strip()
                    b = title[idx+1:].strip()
                    return f"{a}<span class=\"sidebar-wrap-indent\">{b}</span>"

            # Fallback: break at last space before cutoff
            idx = title.rfind(' ', 0, cutoff)
            if idx != -1:
                a = title[:idx].strip()
                b = title[idx+1:].strip()
                return f"{a}<span class=\"sidebar-wrap-indent\">{b}</span>"

            return title

        main_items = []
        showcase_entries = []
        # Detect showcase collection pages intentionally placed under
        # content/pages/meta/showcases/ (rel_path == 'meta/showcases').
        # Also accept files named with the 'showcase_' prefix. We collect
        # them with a priority so an intro/index in the subdir can appear
        # first when the submenu opens.
        for p in self.site_registry.get(active_mode, []):
            # Mark active when the page URL exactly matches the currently
            # rendered page URL. This avoids collisions where multiple pages
            # share the same filename (e.g., index) but live in different
            # directories such as `meta/` and `meta/showcases/`.
            active = "active" if p.get('url') == current_page_url else ""
            safe_title = format_title_for_sidebar(p.get('title', ''))
            item_html = f'<li class="{active}"><a href="{prefix}{p["url"]}">{safe_title}</a></li>'
            rel = p.get('rel_path', '').replace('\\', '/')
            if rel == 'meta/showcases':
                # Highest priority: explicit showcases subdir items (index will be first)
                showcase_entries.append((0, item_html))
            elif p.get('id', '').startswith('showcase_'):
                showcase_entries.append((1, item_html))
            else:
                main_items.append(item_html)

        # Sort showcase entries by priority so the intro/index (priority 0)
        # from the subdir appears before the other showcase pages.
        showcase_items = [h for _, h in sorted(showcase_entries, key=lambda x: x[0])]

        # Main navigation (index and primary pages first). Showcases is a
        # secondary collection marker appended so index.html remains top.
        nav_html += '<ul class="nav-list" id="toc-main">'
        nav_html += '\n'.join(main_items)
        # Only render the Showcases collection for the Meta documentation mode.
        if active_mode == 'meta' and showcase_items:
            # Showcases toggle is visible but marked as a collection.
            nav_html += '<li class="nav-item nav-showcases"><a href="#" onclick="app.openShowcases();return false;">Showcases <span class="collection-marker">collection</span></a></li>'
        nav_html += '</ul>'

        # Hidden showcases list (JS will reveal it) - only for Meta mode
        if active_mode == 'meta' and showcase_items:
            nav_html += '<ul class="nav-list nav-showcase-list" id="toc-showcases" style="display:none">'
            # back control
            nav_html += '<li class="nav-item nav-back"><a href="#" onclick="app.closeShowcases();return false;">← Back</a></li>'
            # group label and group name for clarity
            nav_html += '\n'.join(showcase_items)
            nav_html += '</ul>'

        return nav_html

    def assemble_topic_sidebar(self, page_data):
        """Builds the TOC recursively with depth markers for density control."""
        
        def gather_subblocks(items, current_depth=1):
            """Internal recursive walker to map topics with their depth."""
            subs = []
            for it in items:
                if it.get("type") == "blocks":
                    for b in it.get("blocks", []):
                        child_blocks = gather_subblocks(b.get("content", []), current_depth + 1)
                        subs.append({
                            "id": b.get("id"),
                            "title": b.get("title"),
                            "depth": current_depth,
                            "children": child_blocks
                        })
            return subs

        def render_toc_list(blocks):
            """Turns mapped blocks into HTML <li> elements with data-depth tags."""
            html = ""
            for b in blocks:
                depth_class = f"depth-{b['depth']}"
                html += f'<li class="toc-item {depth_class}" data-topic-id="{b["id"]}" data-depth="{b["depth"]}">'
                html += f'<span onclick="app.focusTopic(\'{b["id"]}\')">{b["title"]}</span>'
                if b["children"]:
                    html += '<ul class="nav-sublist">'
                    html += render_toc_list(b["children"])
                    html += '</ul>'
                html += '</li>'
            return html

        # Initialize the scan
        mapped_topics = gather_subblocks(page_data.get("content", []), current_depth=1)
        
        toc_html = ['<div class="topic-sidebar-container">', '<ul class="nav-list" id="toc">']
        toc_html.append(render_toc_list(mapped_topics))
        toc_html.append('</ul></div>')
        
        return "".join(toc_html)

    def assemble_language_selector(self):
        data = self._load_json(self.lang_def_path, required=True)
        if not data: return ""
        html = ""
        for lid, info in data.items():
            color = info.get("color", "#777")
            html += f'<button class="lang-btn" data-lang-id="{lid}" style="--lang-color: {color}">{info.get("name", lid)}</button>'
        return html

    def assemble_mode_switcher(self, active_mode, prefix):
        html = '<div class="toggle-group mode-toggles">'
        # Add the new Meta mode (framework documentation) to the switcher
        targets = {"atlas": "index.html", "course": "course/intro.html", "meta": "meta/index.html"}
        for m in ["atlas", "course", "meta"]:
            active = "active" if m == active_mode else ""
            target_url = prefix + targets.get(m, "index.html")
            # Close the UI-only showcases view when switching modes so the
            # destination mode can restore its own saved state if present.
            html += f'<a href="{target_url}" class="toggle {active}" onclick="app.prepareModeSwitch()">{m.capitalize()}</a>'
        return html + '</div>'

    # --- BUILD PROCESS ---

    def process_page(self, page_entry):
        data = self._load_json(page_entry['path'], required=True)
        rel_path = page_entry['rel_path']
        depth = rel_path.count(os.sep) + (1 if rel_path else 0)
        prefix = "./" if depth == 0 else "../" * depth
        mode = rel_path.split(os.sep)[0] if rel_path else "atlas"

        # Topic Detection
        has_topics = any(item.get('type') == 'blocks' for item in data.get('content', []))
        topic_class = "" if has_topics else "no-topics"
        
        # Style Inheritance initialization
        page_preset_style = data.get("style", "") 

        template_file = data.get('template', 'base.html')
        template = self._read_file(os.path.join(self.templates_dir, template_file), required=True)
        if not template: return

        # Render Content with depth tracking (2 = Level 1)
        page_html = self.render_content(data.get("content", []), depth=2, inherited_style=page_preset_style)

        # Normalize asset paths produced inside content HTML:
        # - convert backslashes to forward slashes
        # - ensure relative asset references (assets/...) are prefixed correctly
        # so they resolve from the generated page location.
        page_html = page_html.replace('\\', '/')
        # Add prefix to src/href that start with assets/
        page_html = re.sub(r'(src|href)="assets/', lambda m: f"{m.group(1)}=\"{prefix}assets/", page_html)

        # Build Output
        output = template.replace("{{ title }}", data.get("title", "Polyglot Atlas"))
        output = output.replace("{{ asset_prefix }}", prefix)
        output = output.replace("{{ mode_switcher }}", self.assemble_mode_switcher(mode, prefix))
        output = output.replace("{{ language_selection_buttons }}", self.assemble_language_selector())
        # Compute the page URL as stored in the registry (consistent format)
        current_page_url = os.path.join(rel_path, page_entry['id'] + ".html").replace("\\", "/")
        output = output.replace("{{ navigation_sidebar }}", self.assemble_navigation(current_page_url, prefix, mode))
        output = output.replace("{{ topic_sidebar }}", self.assemble_topic_sidebar(data) if has_topics else "")
        output = output.replace("{{ content }}", page_html)
        output = output.replace("{{ body_class_placeholders }}", f"mode-{mode} {topic_class} {data.get('body_class', '')}")

        # Extra Assets
        extras = []
        for a in data.get('extra_assets', []):
            tag = f'<link rel="stylesheet" href="{prefix}assets/css/{a}">' if a.endswith('.css') else f'<script src="{prefix}assets/js/{a}"></script>'
            extras.append(tag)
        output = output.replace("{{ extra_assets }}", "\n".join(extras))

        # Save to dist/
        out_dir = os.path.join(self.dist_dir, rel_path)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, f"{page_entry['id']}.html"), 'w', encoding='utf-8') as f:
            f.write(output)

    def build(self):
        print("🛠️ Initializing Build Process...")
        self.warnings = []
        self.site_registry = {}
        if os.path.exists(self.dist_dir): shutil.rmtree(self.dist_dir)
        os.makedirs(self.dist_dir)

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

        # Prioritize default pages for each mode so they appear first in navigation.
        def prioritize_mode(mode, preferred_ids):
            if mode not in self.site_registry:
                return
            items = self.site_registry[mode]
            ordered = []
            # Add preferred ids first (if present)
            for pid in preferred_ids:
                for it in items:
                    if it['id'] == pid and it not in ordered:
                        ordered.append(it)
            # Then add remaining items in original order
            for it in items:
                if it not in ordered:
                    ordered.append(it)
            self.site_registry[mode] = ordered

        prioritize_mode('atlas', ['index'])
        prioritize_mode('course', ['intro'])
        prioritize_mode('meta', ['index'])

        for mk in sorted(self.site_registry.keys()):
            for pe in self.site_registry[mk]:
                self.process_page(pe)

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