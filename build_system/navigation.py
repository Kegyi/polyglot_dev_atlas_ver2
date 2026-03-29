import json

def assemble_language_picker(lang_defs):
    """Generates the horizontal bar of language buttons."""
    html = '<div class="picker-scroll-container">'
    for lang_id, meta in lang_defs.items():
        color = meta.get("color", "#333")
        html += (
            f'<button class="lang-btn" data-lang="{lang_id}" '
            f'style="--lang-color: {color}">'
            f'<img src="{meta["icon"]}" alt="{meta["name"]}"> {meta["name"]}'
            f'</button>'
        )
    html += '</div>'
    return html

def assemble_sidebar(atlas_pages, course_pages):
    """
    Generates a sidebar containing BOTH lists. 
    JS will toggle visibility between them.
    """
    # Atlas List
    html = '<div id="sidebar-atlas" class="sidebar-content active">'
    html += '<div class="sidebar-header">Atlas Categories</div><ul class="nav-list">'
    for page in atlas_pages:
        html += f'<li><a href="{page["url"]}">{page["title"]}</a></li>'
    html += '</ul></div>'

    # Course List
    html += '<div id="sidebar-course" class="sidebar-content" style="display:none;">'
    html += '<div class="sidebar-header">Learning Path</div><ul class="nav-list">'
    for page in course_pages:
        html += f'<li><a href="{page["url"]}">{page["title"]}</a></li>'
    html += '</ul></div>'
    
    return html

def assemble_topic_sidebar(topics):
    """Generates the 'On This Page' navigation list."""
    if not topics:
        return ""
    
    html = '<nav class="topic-sidebar"><div class="sidebar-header">On This Page</div><ul>'
    for topic in topics:
        html += f'<li><a href="#{topic["id"]}" class="topic-link">{topic["title"]}</a></li>'
    html += '</ul></nav>'
    return html