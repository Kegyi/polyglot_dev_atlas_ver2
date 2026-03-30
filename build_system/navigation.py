def assemble_language_picker(lang_defs, asset_prefix=""):
    html = ""
    for lang_id, meta in lang_defs.items():
        # Correctly wrap the icon path in an <img> tag and prefix asset path
        icon_path = meta.get("icon", "")
        if icon_path and not icon_path.startswith(('http://', 'https://')):
            icon_path = f"{asset_prefix}{icon_path}"
        icon_html = f'<img src="{icon_path}" alt="" style="width:16px; height:16px;">'

        html += (
            f'<button class="lang-btn" id="btn-{lang_id}" '
            f'onclick="AtlasState.select(\'{lang_id}\', \'l\')" '
            f'oncontextmenu="AtlasState.select(\'{lang_id}\', \'r\'); return false;">'
            f'{icon_html} {meta["name"]}'
            f'</button>'
        )
    return html

def assemble_sidebar(pages, mode="atlas", asset_prefix=""):
    # Always add Home at the top
    icon = "🏠" if mode == "atlas" else "📊"
    label = "Home" if mode == "atlas" else "Dashboard"
    
    html = f'<div class="nav-item active" onclick="location.href=\'{asset_prefix}index.html\'">{icon} {label}</div>'
    html += f'<div class="sidebar-title">{"Reference" if mode == "atlas" else "Tracks"}</div>'
    
    for p in pages:
        html += f'<div class="nav-item" onclick="location.href=\'{asset_prefix}{p["url"]}\'">{p["title"]}</div>'
    return html