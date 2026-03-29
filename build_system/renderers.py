def render_keyword_pill(name, version, type_class, url, note=""):
    """
    Renders a single keyword 'chip' or 'pill'.
    type_class: 'hard', 'soft', or 'reserved_unused'
    """
    # Clean version for CSS class (C++20 -> v-cpp20)
    ver_css = f"v-{version.lower().replace('+', 'p').replace(' ', '')}"
    
    title_attr = f'title="{note if note else f"Added in {version}"}"'
    
    return (
        f'<a href="{url}" target="_blank" {title_attr} '
        f'class="kw-pill kw-{type_class} {ver_css}">'
        f'{name}<span class="ver-tag">{version}</span>'
        f'</a>'
    )

def render_table_row(label, cells):
    """
    Renders a standard table row.
    cells: a list of HTML strings for each <td>
    """
    td_html = "".join([f"<td>{cell}</td>" for cell in cells])
    return f"<tr><td><strong>{label}</strong></td>{td_html}</tr>"