import json
import os
from .renderers import render_keyword_pill, render_table_row
from .utils import load_snippet

# Global Cache to avoid repeated disk reads
LANG_CACHE = {}
KEYWORD_CACHE = {}

def get_keyword_data(lang_id):
    """Loads keyword JSON for a specific language."""
    if lang_id not in KEYWORD_CACHE:
        path = f"content/definitions/keywords/{lang_id}.json"
        if os.path.exists(path):
            with open(path, "r", encoding='utf-8') as f:
                KEYWORD_CACHE[lang_id] = json.load(f)
        else:
            return None
    return KEYWORD_CACHE.get(lang_id)

def resolve_url(config, kw_item):
    """Determines the URL for a keyword, using override or base_url."""
    if "url" in kw_item:
        return kw_item["url"]
    base = config.get("base_url", "")
    name = kw_item["name"]
    return f"{base}{name}"

def assemble_keyword_sheet(payload):
    """
    Assembler for the Keyword Comparison Table.
    Expects payload: { "languages": [...], "categories": [...] }
    """
    target_langs = payload.get("languages", [])
    categories = payload.get("categories", [])
    
    # 1. Build Headers
    html = '<div class="table-wrapper">'
    html += '<table class="atlas-table"><thead><tr>'
    html += '<th class="concept-header">Concept</th>'
    for lang in target_langs:
        # data-column-lang is REQUIRED for JS filtering
        html += f'<th data-column-lang="{lang}">{lang.upper()}</th>'
    html += "</tr></thead><tbody>"

    # 2. Build Rows
    for cat in categories:
        readable_cat = cat.replace("_", " ").title()
        html += f'<tr><td class="concept-label"><strong>{readable_cat}</strong></td>'
        
        for lang in target_langs:
            lang_data = get_keyword_data(lang)
            cell_content = "—"
            
            if lang_data:
                kw_list = lang_data.get("keywords", {}).get(cat, [])
                config = lang_data.get("config", {})
                
                pills = [
                    render_keyword_pill(
                        item["name"], 
                        item.get("added_in", "?"), 
                        item.get("type", "hard"), 
                        resolve_url(config, item),
                        item.get("note", "")
                    ) for item in kw_list
                ]
                if pills:
                    cell_content = "".join(pills)
            
            # data-column-lang is REQUIRED here too
            html += f'<td data-column-lang="{lang}">{cell_content}</td>'
        
        html += "</tr>"

    html += "</tbody></table></div>"
    return html

def assemble_code_comparison(payload):
    """
    Assembler for side-by-side code snippets.
    Expects payload: { "files": [ {"lang": "id", "path": "..."} ] }
    """
    files = payload.get("files", [])
    
    # The container class 'code-comparison-grid' is used by CSS for the split-view
    html = '<div class="code-comparison-grid">'
    
    for item in files:
        lang_id = item["lang"]
        file_path = item["path"]
        
        # utils.load_snippet handles the file reading and HTML escaping
        raw_code = load_snippet(file_path)
        
        # 'code-column' and 'data-column-lang' are REQUIRED for JS filtering
        html += f'''
        <div class="code-column" data-column-lang="{lang_id}">
            <div class="code-header">
                <span class="lang-label">{lang_id.upper()}</span>
            </div>
            <pre class="line-numbers"><code class="language-{lang_id}">{raw_code}</code></pre>
        </div>
        '''
        
    html += '</div>'
    return html

def assemble_markdown(payload):
    """
    Simple assembler for markdown/text blocks.
    In the future, integrate a markdown-to-html library here.
    """
    text = payload.get("text", "")
    return f'<div class="markdown-block">{text}</div>'