import html

def render_keyword_pill(item, config):
    """
    Renders a single keyword link with a version tag.
    item: { "name": "if", "type": "hard", "ver": "98" }
    """
    name = item.get("name")
    ver = item.get("ver")
    kw_type = item.get("type", "hard")
    note = item.get("note", "")
    base_url = config.get("base_url", "")
    
    # Determine version class
    v_class = "v-legacy"
    if ver in ["20", "23", "latest"]: v_class = "v-latest"
    elif ver in ["11", "14", "17", "modern"]: v_class = "v-modern"

    return (
        f'<a href="{base_url}{name}" target="_blank" class="kw-pill kw-{kw_type} {v_class}" title="{note}">'
        f'{name}<span class="ver-tag">{ver}</span>'
        f'</a>'
    )