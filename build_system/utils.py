import os
import html

def load_snippet(snippet_path):
    """
    Reads a source file and returns HTML-escaped text.
    Tries a `content/` prefixed fallback if the given path doesn't exist.
    Returns a warning message if the file is missing.
    """
    # Direct path exists -> use it
    if os.path.exists(snippet_path):
        path_to_use = snippet_path
    else:
        # Try a common fallback where snippets live under `content/snippets/...`
        fallback = os.path.join('content', snippet_path)
        if os.path.exists(fallback):
            path_to_use = fallback
        else:
            return f"<!-- Error: Snippet not found at {snippet_path} -->\n<pre>File Missing</pre>"

    with open(path_to_use, 'r', encoding='utf-8') as f:
        code = f.read()

    # Escape < > & etc. so the browser doesn't treat them as HTML tags
    return html.escape(code)