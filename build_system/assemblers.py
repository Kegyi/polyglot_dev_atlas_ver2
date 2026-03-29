import json
import os
from .renderers import render_keyword_pill, render_table_row
from .utils import load_snippet

# Global Cache to avoid repeated disk reads
LANG_CACHE = {}
KEYWORD_CACHE = {}

def get_keyword_data(lang_id):
    if lang_id not in KEYWORD_CACHE:
        path = f"content/definitions/keywords/{lang_id}.json"
        if os.path.exists(path):
            with open(path, "r") as f:
                KEYWORD_CACHE[lang_id] = json.load(f)
    return KEYWORD_CACHE.get(lang_id)

def resolve_url(config, kw_item):
    if "url" in kw_item:
        return kw_item["url"]
    base = config.get("base_url", "")
    name = kw_item["name"]
    return f"{base}{name}"

def assemble_keyword_sheet(payload):
    target_langs = payload.get("languages", [])
    categories = payload.get("categories", [])
    
    # 1. Headers with data-attributes
    html = '<table class="atlas-table"><thead><tr><th>Concept</th>'
    for lang in target_langs:
        html += f'<th data-column-lang="{lang}">{lang.upper()}</th>'
    html += "</tr></thead><tbody>"

    for cat in categories:
        readable_cat = cat.replace("_", " ").title()
        html += f"<tr><td><strong>{readable_cat}</strong></td>"
        
        for lang in target_langs:
            lang_data = get_keyword_data(lang)
            kw_list = lang_data.get("keywords", {}).get(cat, [])
            config = lang_data.get("config", {})
            
            pills = [render_keyword_pill(i["name"], i["added_in"], i["type"], resolve_url(config, i), i.get("note", "")) for i in kw_list]
            
            # 2. Cells with data-attributes
            cell_content = " ".join(pills) if pills else "—"
            html += f'<td data-column-lang="{lang}">{cell_content}</td>'
        
        html += "</tr>"

    html += "</tbody></table>"
    return html

def assemble_code_comparison(payload):
    """
    Payload: {
        "files": [
            {"lang": "rust", "path": "snippets/hello.rs"},
            {"lang": "cpp", "path": "snippets/hello.cpp"}
        ]
    }
    """
    files = payload.get("files", [])
    html_output = '<div class="code-comparison-grid">'
    
    for item in files:
        lang_id = item["lang"]
        file_path = item["path"]
        
        # Load the actual code from the external file
        raw_code = load_snippet(file_path)
        
        # We wrap it in Prism.js classes for syntax highlighting
        # We also add data-column-lang for our JS selection logic
        html_output += f'''
        <div class="code-column" data-column-lang="{lang_id}">
            <div class="code-header">{lang_id.upper()}</div>
            <pre class="line-numbers"><code class="language-{lang_id}">{raw_code}</code></pre>
        </div>
        '''
        
    html_output += '</div>'
    return html_output