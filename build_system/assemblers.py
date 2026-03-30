import os
from pathlib import Path
from .renderers import render_keyword_pill
from .utils import load_snippet, find_extension

def assemble_keyword_sheet(payload, global_keywords):
    """Builds the flex-based 'Keywords Atlas' table."""
    langs = payload.get("languages", [])
    categories = payload.get("categories", [])
    
    html = '<div class="content-block"><div class="block-body"><table class="atlas-table">'
    # Header
    html += '<thead><tr><th>Category</th>'
    for lang in langs:
        html += f'<th data-lang="{lang}">{lang.upper()}</th>'
    html += '</tr></thead><tbody>'
    
    # Rows
    for cat in categories:
        html += f'<tr><td>{cat.capitalize()}</td>'
        for lang in langs:
            lang_data = global_keywords.get(lang, {})
            cat_items = lang_data.get("keywords", {}).get(cat, [])
            config = lang_data.get("config", {})
            
            pills = "".join([render_keyword_pill(i, config) for i in cat_items])
            html += f'<td data-lang="{lang}">{pills if pills else "—"}</td>'
        html += '</tr>'
        
    html += '</tbody></table></div></div>'
    return html

def assemble_code_comparison(payload, langs, snippet_dir):
    """
    Renders side-by-side code snippets with conditional notes.
    Replaces 'assemble_syntax_block' to match Registry.
    """
    title = payload.get("title")
    desc = payload.get("description", "")
    footer = payload.get("footer", "")
    notes = payload.get("notes", [])
    filename = payload.get("filename")

    html = f'<div class="content-block" id="{payload.get("id", "")}">'
    if title:
        html += f'<div class="block-header">{title}</div><div class="block-body">'
    else:
        html += f'<div class="block-body">'
    
    if desc: html += f'<div class="block-desc">{desc}</div>'
    
    html += '<div class="code-grid">'
    for lang in langs:
        ext = find_extension(Path(snippet_dir) / lang, filename)
        snippet_path = Path(snippet_dir) / lang / f"{filename}{ext}"

        code = load_snippet(snippet_path)
        
        if code:
            html += f'<div class="code-card" data-lang="{lang}">'
            html += f'<div class="code-fn">{filename+ext if filename else "main."+ext}</div>'
            html += f'<pre><code>{code}</code></pre></div>'
        else:
            html += f'<div class="code-card" data-lang="{lang}">'
            html += f'<div class="snippet-missing">⚠️ Snippet not found for {lang.upper()}</div></div>'
    html += '</div>'

    # Conditional Notes (Insights)
    for n in notes:
        # Supports req-pair and req-any logic
        type_key = f'data-req-{n.get("type", "pair")}'
        html += f'<div class="cond-note" {type_key}="{n["req"]}">{n["text"]}</div>'

    if footer: 
        html += f'<div class="block-footer">{footer}</div>'
    
    html += '</div></div>'
    return html

def assemble_exercise(payload, langs, snippet_dir):
    """Renders Exercise blocks with hidden/revealable solutions."""
    diff = payload.get("difficulty", "beginner")
    html = f'<div class="content-block" id="{payload.get("id", "")}">'
    html += f'<div class="block-header"><div style="display:flex; align-items:center; gap:10px;">'
    html += f'<div class="difficulty-accent {diff}"></div><span>{payload.get("title")}</span></div></div>'
    html += f'<div class="block-body"><div class="block-desc">{payload.get("task")}</div>'
    html += f'<button class="btn-reveal" onclick="toggleSolution(this)">Show Solution</button>'
    html += f'<div class="exercise-solution" style="display:none;">'
    
    # Solutions are rendered using the code comparison grid
    html += assemble_code_comparison({"filename": payload.get("filename")}, langs, snippet_dir)
    
    html += '</div></div></div>'
    return html

def assemble_markdown(payload):
    """For simple text/principle pages."""
    return f'<div class="md-content">{payload.get("text", "")}</div>'