#!/usr/bin/env python3
import json
import os
import shutil
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SRC_JSON = os.path.join(ROOT, 'codes', 'json', 'design_pattern.json')
GROUP_MD = os.path.join(ROOT, 'codes', 'markdown', 'design_pattern.md')


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def move_readme(old, new):
    ensure_dir(os.path.dirname(new))
    if os.path.exists(old):
        shutil.move(old, new)
        return 'moved'
    else:
        # create placeholder that points to original expected location
        with open(new, 'w', encoding='utf-8') as f:
            f.write(f"# Placeholder\n\nOriginal doc was expected at `{old}`.\n")
        return 'placeholder'


def update_markdown(md_path, replacements):
    if not os.path.exists(md_path):
        return 0
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    changed = 0
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
            changed += 1
    if changed:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(text)
    return changed


def main():
    data = load_json(SRC_JSON)
    replacements = {}
    moved = 0
    placeholders = 0

    for key in list(data.keys()):
        new_docs = f"/content2/docs/design_pattern/{key}/README.md"
        old_docs = data[key].get('meta', {}).get('docs')
        # record replacement for markdown
        if old_docs:
            replacements[old_docs] = new_docs
        # update json
        data[key].setdefault('meta', {})
        data[key]['meta']['docs'] = new_docs

        old_readme = os.path.join(ROOT, old_docs.lstrip('/')) if old_docs else None
        new_readme = os.path.join(ROOT, new_docs.lstrip('/'))
        if old_readme:
            result = move_readme(old_readme, new_readme)
            if result == 'moved':
                moved += 1
            else:
                placeholders += 1

    write_json(SRC_JSON, data)

    md_changes = update_markdown(GROUP_MD, replacements)

    print(f'updated json entries: {len(data)}')
    print(f'readmes moved: {moved}, placeholders created: {placeholders}')
    print(f'markdown files updated: {md_changes}')


if __name__ == '__main__':
    main()
