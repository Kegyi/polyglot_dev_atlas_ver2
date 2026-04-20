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
        self.renderers = self._build_renderer_registry()

    def _build_renderer_registry(self):
        return {
            "title": self._render_title,
            "h1": self._render_heading,
            "h2": self._render_heading,
            "h3": self._render_heading,
            "h4": self._render_heading,
            "h5": self._render_heading,
            "h6": self._render_heading,
            "text": self._render_text,
            "note": self._render_note,
            "code": self._render_code,
            "image": self._render_image,
            "list": self._render_list,
            "blocks": self._render_blocks,
            "table": self._render_sheet,
            "sheet": self._render_sheet,
            "matrix": self._render_sheet,
        }

    def _resolve_json_ref(self, ref, base_path=None):
        """Resolve JSON pointer references (e.g., '#/content/0' or '@core/language_icons')."""
        if not ref or not isinstance(ref, str):
            return None
        
        # Handle @core/ aliases
        if ref.startswith('@core/'):
            core_name = ref.replace('@core/', '').replace('.json', '')
            core_path = os.path.join(self.content_dir, 'core', f'{core_name}.json')
            return self._load_json(core_path)
        
        # Handle @snippets/ aliases
        if ref.startswith('@snippets/'):
            snippet_name = ref.replace('@snippets/', '')
            snippet_path = os.path.join(self.content_dir, 'snippets', snippet_name)
            return self._read_file(snippet_path)
        
        # Handle @images/ aliases (return base64)
        if ref.startswith('@images/'):
            image_name = ref.replace('@images/', '')
            image_path = os.path.join(self.assets_dir, 'images', image_name)
            if os.path.exists(image_path):
                import base64
                with open(image_path, 'rb') as f:
                    return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')
            return None
        
        # Handle JSON pointers
        if ref.startswith('#/'):
            if base_path and os.path.exists(base_path):
                doc = self._load_json(base_path)
                pointer = ref[2:].split('/')
                current = doc
                for segment in pointer:
                    if isinstance(current, dict):
                        current = current.get(segment)
                    elif isinstance(current, list):
                        try:
                            current = current[int(segment)]
                        except (ValueError, IndexError):
                            return None
                    else:
                        return None
                return current
        return None

    def _process_content_with_refs(self, content_list, page_path=None):
        """Recursively process content blocks to resolve $ref pointers."""
        if not isinstance(content_list, list):
            return content_list
        
        processed = []
        for item in content_list:
            if isinstance(item, dict):
                # Resolve $ref first
                if '$ref' in item:
                    ref_data = self._resolve_json_ref(item['$ref'], page_path)
                    if ref_data and isinstance(ref_data, dict):
                        merged = ref_data.copy()
                        merged.update({k: v for k, v in item.items() if k != '$ref'})
                        item = merged
                
                # Recursively process nested content
                if 'content' in item and isinstance(item['content'], list):
                    item['content'] = self._process_content_with_refs(item['content'], page_path)
                
                # Recursively process blocks
                if 'blocks' in item and isinstance(item['blocks'], list):
                    item['blocks'] = self._process_content_with_refs(item['blocks'], page_path)
                
                processed.append(item)
            else:
                processed.append(item)
        
        return processed

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

    def render_content(self, content_list, depth=2, inherited_style="", context=None):
        """Recursively renders content. Inherits styles and increments depth for smart titles.
        `context` is an optional dict (e.g. page-level defaults) passed through to items.
        """
        html = ""
        for item in content_list:
            html += self.render_item(item, depth, inherited_style, context=context)
        return html

    def render_item(self, item, depth=2, inherited_style="", context=None):
        itype = item.get("type")
        renderer = self.renderers.get(itype)
        if renderer:
            return renderer(item, depth=depth, inherited_style=inherited_style, context=context)
        return f"<!-- Unknown item type: {itype} -->"

    def _id_attr(self, item):
        item_id = item.get("id", "")
        return f'id="{item_id}"' if item_id else ""

    def _render_title(self, item, depth=2, inherited_style="", context=None):
        tag = f"h{min(depth, 6)}"
        return f'<{tag} {self._id_attr(item)} class="{item.get("class", "")}">{item.get("text")}</{tag}>'

    def _render_heading(self, item, depth=2, inherited_style="", context=None):
        tag = item.get("type", "h3")
        return f'<{tag} {self._id_attr(item)} class="{item.get("class", "")}">{item.get("text")}</{tag}>'

    def _render_text(self, item, depth=2, inherited_style="", context=None):
        return f'<p {self._id_attr(item)} class="{item.get("class", "")}">{item.get("text", "")}</p>'

    def _render_note(self, item, depth=2, inherited_style="", context=None):
        variant = item.get("variant", "info")
        content_html = item.get("text", "")
        return f'<div {self._id_attr(item)} class="note note-{variant} {item.get("class", "")}"><div class="note-content">{content_html}</div></div>'

    def _render_code(self, item, depth=2, inherited_style="", context=None):
        snippet_ref = item.get("path") or item.get("snippet_path") or item.get("name")
        explicit_collapse = item.get("is_collapse") if "is_collapse" in item else None
        display_name = item.get("label") or item.get("display_name") or item.get("code_name") or item.get("title")
        page_code_defaults = (context or {}).get('code_defaults', {}) if context is not None else {}

        if not display_name:
            display_name = page_code_defaults.get('display_name')

        if explicit_collapse is not None:
            is_collapse = bool(explicit_collapse)
        else:
            is_collapse = bool(page_code_defaults.get('is_collapse', False))

        line_ranges = item.get("line_ranges") or item.get("highlight_ranges") or []
        diff_mode = bool(item.get("diff_mode", False))
        fragment_key = item.get("fragment_key", "")

        return self.assemble_code_comparison(
            snippet_ref,
            is_collapse=is_collapse,
            display_name=display_name,
            line_ranges=line_ranges,
            diff_mode=diff_mode,
            fragment_key=fragment_key,
        )

    def _render_image(self, item, depth=2, inherited_style="", context=None):
        alt = item.get("alt", "")
        src = item.get("src", "")
        return f'<figure class="{item.get("class", "")}"><img src="{src}" alt="{alt}"><figcaption>{item.get("caption", "")}</figcaption></figure>'

    def _render_list(self, item, depth=2, inherited_style="", context=None):
        tag = "ol" if item.get("ordered") else "ul"
        list_items = "".join([f"<li>{i}</li>" for i in item.get("items", [])])
        return f'<{tag} class="{item.get("class", "")}">{list_items}</{tag}>'

    def _render_blocks(self, item, depth=2, inherited_style="", context=None):
        block_html = ""
        for block in item.get("blocks", []):
            block_html += self.render_block(block, depth, inherited_style, context=context)
        return f'<div {self._id_attr(item)} class="blocks-container {item.get("class", "")}">{block_html}</div>'

    def _render_sheet(self, item, depth=2, inherited_style="", context=None):
        rows = item.get("rows") or item.get("data") or []
        if not rows and item.get("columns") and item.get("items"):
            rows = [item.get("columns", [])]
            rows.extend(item.get("items", []))

        headers = item.get("headers") or []
        if headers:
            table_rows = [headers] + rows
        else:
            table_rows = rows

        detect_header = bool(item.get("detect_header", True))
        if not headers and detect_header and table_rows:
            first_row = table_rows[0]
            if isinstance(first_row, list) and first_row and all(isinstance(c, str) for c in first_row):
                headers = first_row

        transposable = bool(item.get("transpose", True))
        mode = item.get("mode", "table")
        custom_class = item.get("class", "")
        id_attr = self._id_attr(item)

        table_html = '<table class="sheet-table"><tbody>'
        for ridx, row in enumerate(table_rows):
            table_html += '<tr>'
            for cell in (row if isinstance(row, list) else [row]):
                cell_text = str(cell)
                tag = "th" if (headers and ridx == 0) else "td"
                table_html += f'<{tag}>{cell_text}</{tag}>'
            table_html += '</tr>'
        table_html += '</tbody></table>'

        toggle_html = ''
        if transposable:
            toggle_html = '<button class="sheet-transpose-btn" type="button">Transpose</button>'

        return (
            f'<div {id_attr} class="sheet-block {custom_class}" data-sheet-mode="{mode}" '
            f'data-auto-header="{str(bool(headers)).lower()}" data-fragment-group="{item.get("fragment_group", "")}">'
            f'<div class="sheet-toolbar">{toggle_html}</div>{table_html}</div>'
        )

    def render_block(self, block_data, depth=2, inherited_style="", context=None):
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
                {self.render_content(block_data.get("content", []), depth + 1, current_style, context=context)}
            </div>
        </div>
        '''
        return html

    # --- ASSEMBLERS (PHASE 2: Depth-Tagged Sidebars) ---

    def assemble_code_comparison(self, snippet_id, is_collapse=False, display_name=None, line_ranges=None, diff_mode=False, fragment_key=""):
        snippet_root = os.path.join(self.content_dir, "snippets")
        # Prepare wrapper: optional collapsed state and header label
        wrapper_classes = "collapsible-code"
        if is_collapse:
            wrapper_classes += " is-collapsed"
        header_html = ""
        if display_name:
            header_html = (f'<div class="collapsible-header">'
                           f'<div class="code-label">{display_name}</div>'
                           f'<button class="collapse-toggle" aria-expanded="{str(not is_collapse).lower()}">▸</button>'
                           f'</div>')

        ranges_attr = ""
        if line_ranges and isinstance(line_ranges, list):
            ranges_attr = ','.join([str(r) for r in line_ranges if r])
        html = (
            f'<div class="{wrapper_classes}" data-snippet-id="{snippet_id}" '
            f'data-diff-mode="{str(bool(diff_mode)).lower()}" '
            f'data-fragment-key="{fragment_key}" '
            f'data-highlight-ranges="{ranges_attr}">{header_html}<div class="code-comparison-grid">'
        )
        found_any = False

        hljs_map = {"scala2": "scala", "scala3": "scala", "typescript": "ts"}

        if not snippet_id:
            # No snippet reference provided in the page JSON
            self._log_warning(f"Snippet reference missing for a code block.")
            return ''

        # Accept a few legacy naming patterns by mapping them to the
        # new nested layout candidates we expect under snippets/{lang}/...
        def make_candidates(sid):
            c = [sid]
            if sid.startswith('design_patterns_'):
                c.append('design_patterns/' + sid[len('design_patterns_'):])
            if sid.startswith('exercise_'):
                c.append('exercises/' + sid[len('exercise_'):])
            if sid.startswith('exercises_'):
                c.append('exercises/' + sid[len('exercises_'):])
            if sid.startswith('language_basics_'):
                c.append('language_basics/' + sid[len('language_basics_'):])
            if sid.startswith('problems_'):
                c.append('problems/' + sid[len('problems_'):])
            # interview_lcci_01_02_name -> interview_lcci/01/02_name
            if sid.startswith('interview_lcci_'):
                parts = sid.split('_')
                if len(parts) >= 4:
                    chapter = parts[2]
                    rest = '_'.join(parts[3:])
                    c.append(f'interview_lcci/{chapter}/{rest}')
            # Generic fallbacks for common snippet group folders
            for fallback in ('exercises', 'problems', 'language_basics', 'design_patterns'):
                cand = f"{fallback}/{sid}"
                if cand not in c:
                    c.append(cand)
            return c

        candidates_root_names = make_candidates(snippet_id)

        if os.path.exists(snippet_root):
            for lang_dir in sorted(os.listdir(snippet_root)):
                dir_path = os.path.join(snippet_root, lang_dir)
                if not os.path.isdir(dir_path): continue
                for cand in candidates_root_names:
                    # If candidate references nested path parts (a/b/c), interpret
                    # all but the last as directories and the last as filename root.
                    if '/' in cand:
                        parts = cand.split('/')
                        base_dir = os.path.join(dir_path, *parts[:-1])
                        filename_root = parts[-1]
                        if os.path.isdir(base_dir):
                            for fname in sorted(os.listdir(base_dir)):
                                if not (fname == filename_root or fname.startswith(filename_root + '.')):
                                    continue
                                fpath = os.path.join(base_dir, fname)
                                if not os.path.isfile(fpath):
                                    continue
                                found_any = True
                                raw_code = self._read_file(fpath)
                                escaped = raw_code.replace('<', '&lt;').replace('>', '&gt;')
                                hljs_lang = hljs_map.get(lang_dir, lang_dir)
                                html += (f'<div class="code-block" data-lang="{lang_dir}" data-fragment-key="{fragment_key}">'
                                         f'<div class="block-header-tag">{lang_dir.upper()}</div>'
                                         f'<pre><code class="language-{hljs_lang}">{escaped}</code></pre></div>')
                            if found_any: break
                        # else continue to other candidate handling
                    else:
                        # Prefer nested directory
                        nested_dir = os.path.join(dir_path, cand)
                        if os.path.isdir(nested_dir):
                            for fname in sorted(os.listdir(nested_dir)):
                                fpath = os.path.join(nested_dir, fname)
                                if not os.path.isfile(fpath):
                                    continue
                                found_any = True
                                raw_code = self._read_file(fpath)
                                escaped = raw_code.replace('<', '&lt;').replace('>', '&gt;')
                                hljs_lang = hljs_map.get(lang_dir, lang_dir)
                                html += (f'<div class="code-block" data-lang="{lang_dir}" data-fragment-key="{fragment_key}">'
                                         f'<div class="block-header-tag">{lang_dir.upper()}</div>'
                                         f'<pre><code class="language-{hljs_lang}">{escaped}</code></pre></div>')
                            if found_any: break

                    # Direct file under language folder
                    file_candidate = os.path.join(dir_path, cand)
                    if os.path.isfile(file_candidate):
                        found_any = True
                        raw_code = self._read_file(file_candidate)
                        escaped = raw_code.replace('<', '&lt;').replace('>', '&gt;')
                        hljs_lang = hljs_map.get(lang_dir, lang_dir)
                        html += (f'<div class="code-block" data-lang="{lang_dir}" data-fragment-key="{fragment_key}">'
                                 f'<div class="block-header-tag">{lang_dir.upper()}</div>'
                                 f'<pre><code class="language-{hljs_lang}">{escaped}</code></pre></div>')
                        break

                    # Fallback legacy flat file name
                    target = next((f for f in os.listdir(dir_path) if f.startswith(f"{cand}.")), None)
                    if target:
                        found_any = True
                        raw_code = self._read_file(os.path.join(dir_path, target))
                        escaped = raw_code.replace('<', '&lt;').replace('>', '&gt;')
                        hljs_lang = hljs_map.get(lang_dir, lang_dir)
                        html += (f'<div class="code-block" data-lang="{lang_dir}" data-fragment-key="{fragment_key}">'
                                 f'<div class="block-header-tag">{lang_dir.upper()}</div>'
                                 f'<pre><code class="language-{hljs_lang}">{escaped}</code></pre></div>')
                        break
        
        if not found_any:
            self._log_warning(f"Snippet '{snippet_id}' not found.")
            # Emphasize the label so it stands out visually inside the note.
            content_html = f"<span class=\"snippet-error\">Snippet Error:</span> \"{snippet_id}\" missing"
            return f'<div class="note note-error"><div class="note-content">{content_html}</div></div>'
        # close inner grid and wrapper
        return html + '</div></div>'

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

        # Build a hierarchical tree of folders (children) and pages. This
        # allows emitting nested collection toggles / submenus recursively.
        def make_node():
            return { 'pages': [], 'children': {} }

        root = make_node()

        for p in self.site_registry.get(active_mode, []):
            active = "active" if p.get('url') == current_page_url else ""
            safe_title = format_title_for_sidebar(p.get('title', ''))
            item_html = f'<li class="{active}"><a href="{prefix}{p["url"]}">{safe_title}</a></li>'

            rel = p.get('rel_path', '').replace('\\', '/')
            parts = rel.split('/') if rel else []
            # If page is under the same mode, the remaining parts after the
            # mode identify nested folders. e.g., meta/showcases/gallery -> ['showcases','gallery']
            if parts and parts[0] == active_mode:
                remaining = parts[1:]
            else:
                remaining = []

            node = root
            if remaining:
                for seg in remaining:
                    node = node['children'].setdefault(seg, make_node())
                node['pages'].append((p, item_html))
            else:
                node['pages'].append((p, item_html))

        # Helper to render a node's pages and subfolders recursively. The
        # path_parts list contains the folder path parts used to construct
        # a unique DOM id for nested submenus.
        def render_node(node, path_parts=None, depth=0):
            if path_parts is None: path_parts = []
            html_parts = []

            # Sorting helper: numeric-prefixed names come first and are
            # ordered by their leading integer, then by the remainder.
            def nav_sort_key_name(name):
                m = re.match(r'^(\d+)[_\- ]?(.*)$', name)
                if m:
                    num = int(m.group(1))
                    rest = m.group(2) or ''
                    return (0, num, rest.lower())
                return (1, name.lower())

            # Render pages at this level using this precedence:
            # 1) `index` page (if present)
            # 2) pages listed in `index` page's `page_list` (if provided)
            # 3) numeric-prefixed pages sorted by leading number
            # 4) remaining pages alphabetically
            pages = list(node['pages'])
            ordered_pages = []

            # 1) index page
            index_entry = next(((p, h) for p, h in pages if p.get('id') == 'index'), None)
            index_page_ids = []
            if index_entry:
                ordered_pages.append(index_entry)
                # Attempt to read page_list from index JSON to get explicit ordering
                try:
                    idx_data = self._load_json(index_entry[0].get('path', ''), required=False) or {}
                    pl = idx_data.get('page_list', [])
                    if isinstance(pl, list):
                        # Normalize to string ids
                        index_page_ids = [str(x) for x in pl]
                except Exception:
                    index_page_ids = []

            # 2) pages from index.page_list (in order)
            if index_page_ids:
                for pid in index_page_ids:
                    match = next(((p, h) for p, h in pages if p.get('id') == pid and (p, h) not in ordered_pages), None)
                    if match:
                        ordered_pages.append(match)

            # 3 & 4) remaining pages sorted by numeric-aware key
            remaining = [ph for ph in pages if ph not in ordered_pages]
            remaining_sorted = sorted(remaining, key=lambda pi: nav_sort_key_name(pi[0].get('id', pi[0].get('title', ''))))
            ordered_pages.extend(remaining_sorted)

            for p, item_html in ordered_pages:
                html_parts.append(item_html)

            # Render child folders as collection toggles
            for child_key in sorted(node['children'].keys(), key=nav_sort_key_name):
                safe_child = re.sub(r'[^a-zA-Z0-9_-]', '-', child_key)
                label = child_key.replace('_', ' ').capitalize()
                # Build full path key for nested identification
                full_parts = (path_parts + [child_key])
                safe_full = '-'.join([re.sub(r'[^a-zA-Z0-9_-]', '-', p) for p in full_parts])
                # Toggle item
                # Emit a collection toggle. The span `.collection-marker` is
                # intentionally left empty so CSS can render a colored arrow
                # marker purely via ::after. This keeps the HTML semantic and
                # allows accessible labels on the anchor if needed.
                html_parts.append(f'<li class="nav-item nav-collection nav-{safe_full}"><a href="#" onclick="app.openCollection(\'{active_mode}\', \'{safe_full}\');return false;">{label} <span class="collection-marker" aria-hidden="true"></span></a></li>')

            return '\n'.join(html_parts)

        # Render root main list
        nav_html += '<ul class="nav-list" id="toc-main">'
        nav_html += render_node(root, [])
        nav_html += '</ul>'

        # Emit submenus recursively
        def emit_submenus(node, path_parts=None):
            nonlocal nav_html
            if path_parts is None: path_parts = []
            # Reuse numeric-aware key from render_node
            def nav_sort_key_name(name):
                m = re.match(r'^(\d+)[_\- ]?(.*)$', name)
                if m:
                    num = int(m.group(1))
                    rest = m.group(2) or ''
                    return (0, num, rest.lower())
                return (1, name.lower())

            for child_key, child_node in sorted(node['children'].items(), key=lambda kv: nav_sort_key_name(kv[0])):
                safe_full = '-'.join([re.sub(r'[^a-zA-Z0-9_-]', '-', p) for p in (path_parts + [child_key])])
                list_id = f'toc-collection-{active_mode}-{safe_full}'
                nav_html_local = f'<ul class="nav-list nav-collection-list" id="{list_id}" style="display:none">'
                nav_html_local += f'<li class="nav-item nav-back"><a href="#" onclick="app.closeCollection(\'{active_mode}\', \'{safe_full}\');return false;">← Back</a></li>'
                # Render pages at this child level honoring index -> page_list -> numeric ordering
                pages = list(child_node['pages'])
                ordered_pages = []
                index_entry = next(((p, h) for p, h in pages if p.get('id') == 'index'), None)
                index_page_ids = []
                if index_entry:
                    ordered_pages.append(index_entry)
                    try:
                        idx_data = self._load_json(index_entry[0].get('path', ''), required=False) or {}
                        pl = idx_data.get('page_list', [])
                        if isinstance(pl, list):
                            index_page_ids = [str(x) for x in pl]
                    except Exception:
                        index_page_ids = []

                if index_page_ids:
                    for pid in index_page_ids:
                        match = next(((p, h) for p, h in pages if p.get('id') == pid and (p, h) not in ordered_pages), None)
                        if match:
                            ordered_pages.append(match)

                remaining = [ph for ph in pages if ph not in ordered_pages]
                remaining_sorted = sorted(remaining, key=lambda pi: nav_sort_key_name(pi[0].get('id', pi[0].get('title', ''))))
                ordered_pages.extend(remaining_sorted)

                for p, item_html in ordered_pages:
                    nav_html_local += item_html
                # Also include toggles for grandchildren (rendered as items)
                for gc_key in sorted(child_node['children'].keys(), key=nav_sort_key_name):
                    safe_gc = re.sub(r'[^a-zA-Z0-9_-]', '-', gc_key)
                    gc_full = '-'.join([re.sub(r'[^a-zA-Z0-9_-]', '-', p) for p in (path_parts + [child_key, gc_key])])
                    label = gc_key.replace('_', ' ').capitalize()
                    nav_html_local += f'<li class="nav-item nav-collection nav-{gc_full}"><a href="#" onclick="app.openCollection(\'{active_mode}\', \'{gc_full}\');return false;">{label} <span class="collection-marker" aria-hidden="true"></span></a></li>'

                nav_html_local += '</ul>'
                # Append to main nav_html
                nav_html += nav_html_local
                # Recurse into grandchildren
                emit_submenus(child_node, path_parts + [child_key])

        emit_submenus(root, [])

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

    def _generate_bundled_css(self):
        """Inline @import rules from workspace `assets/css/main.css` and
        emit a bundled `main.css` into the dist folder. Also ensure
        `ui_states.css` is present and move other css files into
        `assets/css/custom/` inside the dist to denote page-scoped styles.
        """
        import re

        workspace_css_dir = os.path.join(self.assets_dir, "css")
        dist_css_dir = os.path.join(self.dist_dir, "assets", "css")
        if not os.path.isdir(dist_css_dir):
            return

        main_src = os.path.join(workspace_css_dir, "main.css")
        main_dest = os.path.join(dist_css_dir, "main.css")

        combined = []
        if os.path.exists(main_src):
            text = self._read_file(main_src)
            # Replace @import "..." by inlining referenced files when local
            imports = re.findall(r'@import\s+["\']([^"\']+)["\']\s*;', text)
            # Inline each import in order
            for imp in imports:
                imp_path = os.path.join(workspace_css_dir, imp)
                if os.path.exists(imp_path):
                    combined.append(f"/* Inlined: {imp} */\n")
                    combined.append(self._read_file(imp_path))
                else:
                    # If import not found, keep the import line as-is
                    combined.append(f"/* Missing import: {imp} */\n")

            # Append remaining non-import content (strip import lines)
            stripped = re.sub(r'@import\s+["\'][^"\']+["\']\s*;\s*', '', text)
            combined.append("\n/* main.css remaining content */\n")
            combined.append(stripped)
        else:
            # Fallback: if no main.css in workspace, try to join modules folder
            modules_dir = os.path.join(workspace_css_dir, "modules")
            if os.path.isdir(modules_dir):
                for fname in sorted(os.listdir(modules_dir)):
                    if fname.endswith('.css'):
                        combined.append(f"/* Inlined module: {fname} */\n")
                        combined.append(self._read_file(os.path.join(modules_dir, fname)))

        # Write bundled main.css to dist
        try:
            with open(main_dest, 'w', encoding='utf-8') as f:
                f.write('\n'.join(combined))
        except Exception as e:
            self._log_warning(f"Failed to write bundled main.css: {e}")

        # Ensure ui_states.css exists in dist (copy from workspace if present)
        ui_src = os.path.join(workspace_css_dir, "ui_states.css")
        ui_dest = os.path.join(dist_css_dir, "ui_states.css")
        if os.path.exists(ui_src):
            try:
                shutil.copyfile(ui_src, ui_dest)
            except Exception:
                self._log_warning("Failed to copy ui_states.css to dist")
        else:
            # Create an empty placeholder so templates can reference it safely
            open(ui_dest, 'a').close()

        # Move other CSS files into `custom/` inside dist assets/css so they are
        # clearly page-scoped and not part of the global bundle.
        custom_dir = os.path.join(dist_css_dir, 'custom')
        os.makedirs(custom_dir, exist_ok=True)

        for entry in os.listdir(dist_css_dir):
            src_path = os.path.join(dist_css_dir, entry)
            # Skip directories we want to keep and the bundled files
            if entry in ('modules', 'custom', 'main.css', 'ui_states.css'):
                continue
            # Move files and folders into custom
            try:
                target_path = os.path.join(custom_dir, entry)
                shutil.move(src_path, target_path)
            except Exception as e:
                # Non-fatal: log and continue
                self._log_warning(f"Failed to relocate CSS asset {entry}: {e}")

    def assemble_mode_switcher(self, active_mode, prefix):
        html = '<div class="toggle-group mode-toggles">'
        # Build mode toggles from discovered pages subfolders so adding
        # a new top-level folder under `content/pages/` auto-creates a mode.
        modes = sorted(self.site_registry.keys()) if self.site_registry else ["atlas"]
        for m in modes:
            active = "active" if m == active_mode else ""
            # Root/top-level mode ('atlas') resolves to index.html at root.
            target_url = prefix + ("index.html" if m == "atlas" else f"{m}/index.html")
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

        # Phase 1: Resolve $ref pointers in content before rendering
        if 'content' in data and isinstance(data['content'], list):
            data['content'] = self._process_content_with_refs(data['content'], page_entry['path'])

        # Topic Detection
        has_topics = any(item.get('type') == 'blocks' for item in data.get('content', []))
        topic_class = "" if has_topics else "no-topics"
        
        # Style Inheritance initialization
        page_preset_style = data.get("style", "") 

        template_file = data.get('template', 'base.html')
        template = self._read_file(os.path.join(self.templates_dir, template_file), required=True)
        if not template: return

        # Render Content with depth tracking (2 = Level 1)
        # Pass page-level `code_defaults` in context so code rendering remains generic.
        page_code_defaults = data.get('code_defaults', {})
        page_html = self.render_content(data.get("content", []), depth=2, inherited_style=page_preset_style, context={'code_defaults': page_code_defaults})

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

        # Prefer an `index` page first for every discovered mode.
        for mode_key in list(self.site_registry.keys()):
            prioritize_mode(mode_key, ['index'])

        for mk in sorted(self.site_registry.keys()):
            for pe in self.site_registry[mk]:
                self.process_page(pe)
        if os.path.exists(self.assets_dir):
            shutil.copytree(self.assets_dir, os.path.join(self.dist_dir, "assets"))
            # Post-process CSS: bundle `main.css` by inlining @imports from
            # the workspace assets/css files and produce `ui_states.css`.
            try:
                self._generate_bundled_css()
            except Exception as e:
                self._log_warning(f"CSS bundling failed: {e}")
        
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