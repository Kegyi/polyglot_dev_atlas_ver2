import os
import html

def load_snippet(snippet_path):
    """
    Reads a source file and returns HTML-escaped text.
    Returns a warning message if the file is missing.
    """
    if not os.path.exists(snippet_path):
        return f"<!-- Error: Snippet not found at {snippet_path} -->\n<pre>File Missing</pre>"
    
    with open(snippet_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Escape < > & etc. so the browser doesn't treat them as HTML tags
    return html.escape(code)