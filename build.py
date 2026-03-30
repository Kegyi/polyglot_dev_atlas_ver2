import json
import os
import shutil
from build_system.registry import BLOCK_REGISTRY
from build_system.navigation import assemble_language_picker, assemble_sidebar
from build_system.utils import load_snippet

# Config
BASE_TEMPLATE = "templates/base.html"
CONTENT_DIR = "content/pages"
COURSE_DIR = "content/courses"
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
    for folder in [CONTENT_DIR, COURSE_DIR, KEYWORD_DIR, SNIPPET_DIR]:
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

    # 3. Discovery (Sidebar generation) - Safely handle empty directories
    def discover_pages(directory):
        pages = []
        if os.path.exists(directory):
            for f in os.listdir(directory):
                if f.endswith(".json"):
                    data = load_json(os.path.join(directory, f))
                    pages.append({
                        "title": data.get("title", f),
                        "url": f.replace(".json", ".html"),
                        "source_path": os.path.join(directory, f)
                    })
        return pages

    atlas_pages = discover_pages(CONTENT_DIR)
    course_pages = discover_pages(COURSE_DIR)

    # 4. Build Atlas Pages
    for p in atlas_pages:
        process_page(p['source_path'], langs, keywords, atlas_pages, "atlas")

    # 5. Build Course Pages
    for p in course_pages:
        process_page(p['source_path'], langs, keywords, course_pages, "course")

def process_page(path, langs, keywords, sidebar_pages, mode):
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

    # 2. Build Navigation UI
    lang_picker = assemble_language_picker(langs)
    # The left sidebar shows pages relevant to the current mode (Atlas vs Course)
    sidebar = assemble_sidebar(sidebar_pages, mode)
    
    # 3. Topic Sidebar Logic (Right Sidebar)
    # Rule: If only 1 topic exists, we hide the sidebar to maximize space.
    topic_sidebar_html = ""
    body_class = "hide-toc" 
    
    if len(topics) > 1:
        body_class = "" # Remove hide class to show the gutter
        topic_sidebar_html = '<div class="sidebar-title">On this page</div>'
        for t in topics:
            # Anchors link to the block IDs
            topic_sidebar_html += f'<div class="nav-item" onclick="location.href=\'#{t["id"]}\'">• {t["title"]}</div>'

    # 4. Handle "Page Intent" (Custom Assets)
    config = data.get("config", {})
    extra_assets = ""
    
    # Inject page-specific CSS
    for style in config.get("styles", []):
        extra_assets += f'<link rel="stylesheet" href="assets/css/pages/{style}">\n'
    
    # Inject page-specific JS
    for script in config.get("scripts", []):
        extra_assets += f'<script src="assets/js/pages/{script}"></script>\n'

    # 5. Final Template Assembly
    output = template.replace("{{ title }}", data.get("title", "Untitled Page"))
    output = output.replace("{{ language_picker }}", lang_picker)
    output = output.replace("{{ navigation_sidebar }}", sidebar)
    output = output.replace("{{ topic_sidebar }}", topic_sidebar_html)
    output = output.replace("{{ content }}", "\n".join(html_blocks))
    output = output.replace("{{ extra_assets }}", extra_assets)
    output = output.replace("{{ body_class_placeholders }}", body_class)

    # 6. Save to Dist
    out_name = os.path.basename(path).replace(".json", ".html")
    output_path = os.path.join(OUTPUT_DIR, out_name)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
        
    print(f"  [Built] {out_name} (Mode: {mode})")

if __name__ == "__main__":
    build_all()