import json
import os
import shutil

# Import our modular build system
from build_system.icon_sync import sync_icons
from build_system.registry import get_assembler
from build_system.navigation import assemble_language_picker, assemble_sidebar, assemble_topic_sidebar

# Configuration
CONTENT_PAGES_DIR = "content/pages"
CONTENT_COURSES_DIR = "content/courses"
LANGUAGES_DEF_PATH = "content/definitions/languages.json"
TEMPLATE_PATH = "templates/base.html"
OUTPUT_DIR = "dist"

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def build_all():
    # 0. Auto-Sync Icons before anything else
    sync_icons(LANGUAGES_DEF_PATH, "assets/icons")

    # 1. Setup Environment
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    # Copy assets to dist (CSS, JS, Icons)
    if os.path.exists("assets"):
        shutil.copytree("assets", os.path.join(OUTPUT_DIR, "assets"))

    # 2. Load Global Data
    languages_data = load_json(LANGUAGES_DEF_PATH)
    
    # 3. Discover Content (for Sidebar Navigation)
    # We scan the directories to see what pages actually exist
    atlas_pages = []
    for f in os.listdir(CONTENT_PAGES_DIR):
        if f.endswith(".json"):
            # Load title from inside the file for the sidebar
            data = load_json(os.path.join(CONTENT_PAGES_DIR, f))
            atlas_pages.append({
                "title": data.get("title", f),
                "url": f.replace(".json", ".html")
            })

    course_pages = []
    if os.path.exists(CONTENT_COURSES_DIR):
        for f in os.listdir(CONTENT_COURSES_DIR):
            if f.endswith(".json"):
                data = load_json(os.path.join(CONTENT_COURSES_DIR, f))
                course_pages.append({
                    "title": data.get("title", f),
                    "url": f.replace(".json", ".html")
                })

    # 4. Generate Global UI Components
    lang_picker_html = assemble_language_picker(languages_data)
    nav_sidebar_html = assemble_sidebar(atlas_pages, course_pages)

    # 5. Build Every Page
    # Build Atlas Pages
    for f in os.listdir(CONTENT_PAGES_DIR):
        if f.endswith(".json"):
            process_page(
                os.path.join(CONTENT_PAGES_DIR, f), 
                lang_picker_html, 
                nav_sidebar_html
            )

    # Build Course Pages (if any)
    if os.path.exists(CONTENT_COURSES_DIR):
        for f in os.listdir(CONTENT_COURSES_DIR):
            if f.endswith(".json"):
                process_page(
                    os.path.join(CONTENT_COURSES_DIR, f), 
                    lang_picker_html, 
                    nav_sidebar_html
                )

def process_page(file_path, lang_picker_html, nav_sidebar_html):
    page_data = load_json(file_path)
    page_title = page_data.get("title", "Untitled")
    
    html_blocks = []
    topics = []

    # Assemble Content Blocks
    for block in page_data.get("blocks", []):
        block_type = block.get("type")
        payload = block.get("payload", {})
        block_id = block.get("id", "")
        block_title = block.get("title", "")

        # Collect topics for the Right Sidebar (Auto-TOC)
        if block_id and block_title:
            topics.append({"id": block_id, "title": block_title})

        # Get the right assembler from the registry
        assembler_fn = get_assembler(block_type)
        if assembler_fn:
            content = assembler_fn(payload)
            # Wrap in section for scroll-spy and anchor links
            section_wrapper = f'<section id="{block_id}" class="page-block">{content}</section>'
            html_blocks.append(section_wrapper)
        else:
            print(f"Warning: No assembler for '{block_type}' in {file_path}")

    # Generate Topic Sidebar (TOC)
    topic_sidebar_html = assemble_topic_sidebar(topics)

    # Load Base Template
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as t:
        template = t.read()

    # Final Assembly (Template Injection)
    final_html = template.replace("{{ title }}", page_title)
    final_html = final_html.replace("{{ language_picker }}", lang_picker_html)
    final_html = final_html.replace("{{ navigation_sidebar }}", nav_sidebar_html)
    final_html = final_html.replace("{{ topic_sidebar }}", topic_sidebar_html)
    final_html = final_html.replace("{{ content }}", "\n".join(html_blocks))

    # Save to dist/
    output_filename = os.path.basename(file_path).replace(".json", ".html")
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(final_html)
    
    print(f"Built: {output_filename}")

if __name__ == "__main__":
    build_all()