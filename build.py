import json
import os
import shutil
from build_system.registry import BLOCK_REGISTRY
from build_system.navigation import assemble_language_picker, assemble_sidebar
from build_system.utils import load_snippet

# Config
BASE_TEMPLATE = "templates/base.html"
CONTENT_DIR = "content/pages"
SNIPPET_DIR = "content/snippets"
LANG_DEF = "content/definitions/languages.json"
KEYWORD_DIR = "content/definitions/keywords"
OUTPUT_DIR = "dist"

def load_json(path):
    if not os.path.exists(path): return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_all():
    # 1. Clean & Setup
    if os.path.exists(OUTPUT_DIR): shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    
    # 2. Ensure content directories exist (Auto-healing)
    for folder in [CONTENT_DIR, KEYWORD_DIR, SNIPPET_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created missing directory: {folder}")

    if os.path.exists("assets"):
        shutil.copytree("assets", os.path.join(OUTPUT_DIR, "assets"))

    # 2. Load Global Data
    langs = load_json(LANG_DEF)
    keywords = {}
    if os.path.exists(KEYWORD_DIR):
        for f in os.listdir(KEYWORD_DIR):
            if f.endswith(".json"):
                data = load_json(os.path.join(KEYWORD_DIR, f))
                if 'id' in data:
                    keywords[data['id']] = data

    # 3. Discovery (Sidebar generation) - discover pages grouped by top-level subfolder (mode)
    def discover_pages_by_mode(content_directory):
        modes = {}
        if not os.path.exists(content_directory):
            return modes

        for entry in os.listdir(content_directory):
            entry_path = os.path.join(content_directory, entry)
            if not os.path.isdir(entry_path):
                continue

            mode = entry
            pages = []
            for root, dirs, files in os.walk(entry_path):
                for fname in files:
                    if not fname.endswith('.json'):
                        continue
                    source_path = os.path.join(root, fname)
                    rel_path = os.path.relpath(source_path, content_directory)
                    url = rel_path.replace(os.sep, '/').replace('.json', '.html')
                    data = load_json(source_path)
                    pages.append({
                        'title': data.get('title', fname),
                        'url': url,
                        'source_path': source_path
                    })

            modes[mode] = pages
        return modes

    modes = discover_pages_by_mode(CONTENT_DIR)

    # 4. Build pages for each mode and preserve folder structure in dist
    for mode_name, pages in modes.items():
        for p in pages:
            process_page(p['source_path'], langs, keywords, pages, mode_name, p['url'])

def process_page(path, langs, keywords, sidebar_pages, mode, url=None):
    """
    Orchestrates the conversion of a single JSON page into a styled HTML file.
    """
    data = load_json(path)
    with open(BASE_TEMPLATE, 'r', encoding='utf-8') as t:
        template = t.read()

    # 1. Process Content Blocks
    html_blocks = []
    topics = [] # For the Right Sidebar (TOC)
    page_title = data.get("title")
    if page_title:
        html_blocks.append(f'<div class="page-title">{page_title}</div>') # TODO: style this better

    for block in data.get("blocks", []):
        b_type = block.get("type")
        payload = block.get("payload", {})
        
        # Collect IDs for Right Sidebar (TOC) anchoring
        if "id" in block and "title" in block:
            topics.append({"id": block["id"], "title": block["title"]})

        # Render the block using the registry
        if b_type == "keyword_sheet":
            # Keyword sheet is a special case: it needs the global keyword database
            if b_type in BLOCK_REGISTRY:
                html_blocks.append(BLOCK_REGISTRY[b_type](payload, keywords))
        elif b_type in {"code_comparison", "exercise"}:
            if b_type in BLOCK_REGISTRY:
                html_blocks.append(BLOCK_REGISTRY[b_type](payload, langs, SNIPPET_DIR))
        elif b_type in BLOCK_REGISTRY:
            # Standard blocks (markdown)
            html_blocks.append(BLOCK_REGISTRY[b_type](payload))
        else:
            print(f"  [Warning] No assembler found for block type: {b_type}")

    # 2. Build Navigation UI placeholders (will be generated after asset_prefix)
    lang_picker = ""
    sidebar = ""
    
    # 3. Topic Sidebar Logic (Right Sidebar)
    # Rule: If only 1 topic exists, we hide the sidebar to maximize space.
    topic_sidebar_html = ""
    body_class = "hide-toc" 
    
    if len(topics) > 1:
            body_class = "" 
            topic_sidebar_html = '<div class="sidebar-title">On this page</div>'
            for t in topics:
                # Change from onclick to a standard <a> tag for native browser jumping
                topic_sidebar_html += f'<a href="#{t["id"]}" class="nav-item">• {t["title"]}</a>'

    # 4. Handle "Page Intent" (Custom Assets)
    config = data.get("config", {})
    extra_assets = ""
    
    # Inject page-specific CSS
    for style in config.get("styles", []):
        extra_assets += f'<link rel="stylesheet" href="assets/css/pages/{style}">\n'
    
    # Inject page-specific JS
    for script in config.get("scripts", []):
        extra_assets += f'<script src="assets/js/pages/{script}"></script>\n'

    # 5. Determine output path and compute asset prefix for correct relative links
    if url:
        out_rel = url
    else:
        out_rel = os.path.basename(path).replace('.json', '.html')

    output_path = os.path.join(OUTPUT_DIR, out_rel.replace('/', os.sep))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Compute prefix from page dir to OUTPUT_DIR (e.g., '..' or '../..')
    page_dir = os.path.dirname(output_path)
    rel_to_dist = os.path.relpath(OUTPUT_DIR, page_dir).replace(os.sep, '/')
    if rel_to_dist == '.':
        asset_prefix = ''
    else:
        asset_prefix = rel_to_dist + '/'

    # Ensure extra_assets references include the asset prefix
    prefixed_extra = ''
    for style in config.get('styles', []):
        prefixed_extra += f'<link rel="stylesheet" href="{asset_prefix}assets/css/pages/{style}">\n'
    for script in config.get('scripts', []):
        prefixed_extra += f'<script src="{asset_prefix}assets/js/pages/{script}"></script>\n'

    # Build the language picker and sidebar with correct asset_prefix so links/icons resolve
    lang_picker = assemble_language_picker(langs, asset_prefix)
    sidebar = assemble_sidebar(sidebar_pages, mode, asset_prefix)

    # 6. Final Template Assembly with asset prefix
    output = template.replace("{{ title }}", data.get("title", "Untitled Page"))
    output = output.replace("{{ language_picker }}", lang_picker)
    output = output.replace("{{ navigation_sidebar }}", sidebar)
    output = output.replace("{{ topic_sidebar }}", topic_sidebar_html)
    output = output.replace("{{ content }}", "\n".join(html_blocks))
    output = output.replace("{{ extra_assets }}", prefixed_extra)
    output = output.replace("{{ body_class_placeholders }}", body_class)
    output = output.replace("{{ asset_prefix }}", asset_prefix)

    # Fill slot placeholders: default to first language name if available
    try:
        primary_label = list(langs.values())[0].get('name') if langs and len(langs) > 0 else 'Primary'
    except Exception:
        primary_label = 'Primary'
    output = output.replace("{{ slot_primary }}", primary_label)
    output = output.replace("{{ slot_secondary }}", "")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"  [Built] {out_rel} (Mode: {mode})")

if __name__ == "__main__":
    build_all()