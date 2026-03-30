import os
import html
from functools import lru_cache
from pathlib import Path

@lru_cache(maxsize=128)
def load_snippet(snippet_path):
    """
    Reads a source file, escapes HTML, and caches the result.
    Returns None if the file is missing to allow the assembler to show a fallback.
    """
    if not os.path.exists(snippet_path):
        return None

    try:
        with open(snippet_path, 'r', encoding='utf-8') as f:
            code = f.read()
        return html.escape(code)
    except Exception as e:
        print(f"Error reading {snippet_path}: {e}")
        return None
    
def find_extension(directory, base_name):
    directory = Path(directory)

    matches = list(directory.glob(f"{base_name}.*"))

    if not matches:
        return None  # file not found

    if len(matches) > 1:
        raise ValueError(f"Multiple matches found: {matches}")

    return matches[0].suffix  # includes dot