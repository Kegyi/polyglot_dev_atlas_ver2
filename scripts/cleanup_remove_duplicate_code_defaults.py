#!/usr/bin/env python3
import json
from pathlib import Path

PAGE_PATH = Path(__file__).resolve().parent.parent / "content" / "pages" / "course" / "exercieses.json"
BACKUP_PATH = PAGE_PATH.with_suffix('.json.bak')

def clean_item(obj, defaults):
    removed = 0
    if isinstance(obj, dict):
        if obj.get('type') == 'code':
            for key, val in list(defaults.items()):
                if key in obj and obj[key] == val:
                    del obj[key]
                    removed += 1
        for v in obj.values():
            removed += clean_item(v, defaults)
    elif isinstance(obj, list):
        for el in obj:
            removed += clean_item(el, defaults)
    return removed


def main():
    if not PAGE_PATH.exists():
        print(f"ERROR: page file not found: {PAGE_PATH}")
        return 2
    data = json.loads(PAGE_PATH.read_text(encoding='utf-8'))
    defaults = data.get('code_defaults', {})
    if not defaults:
        print("No page-level code_defaults found; nothing to remove.")
        return 0
    keep_defaults = {}
    if 'display_name' in defaults:
        keep_defaults['display_name'] = defaults['display_name']
    if 'is_collapse' in defaults:
        keep_defaults['is_collapse'] = defaults['is_collapse']
    if not keep_defaults:
        print("No relevant defaults (display_name/is_collapse) found; nothing to remove.")
        return 0

    BACKUP_PATH.write_bytes(PAGE_PATH.read_bytes())
    removed = clean_item(data.get('content', []), keep_defaults)
    if removed:
        PAGE_PATH.write_text(json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding='utf-8')
        print(f"Removed {removed} duplicated keys matching page defaults and wrote changes to {PAGE_PATH}")
        print(f"Backup saved to {BACKUP_PATH}")
    else:
        print("No duplicated keys matching page defaults were found.")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
