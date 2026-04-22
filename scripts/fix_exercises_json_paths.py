import os
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'content', 'pages', 'course', 'exercises.json')
CPP_EX = os.path.join(ROOT, 'content', 'snippets', 'cpp', 'exercises')

if not os.path.exists(PAGE):
    print('Page not found:', PAGE)
    raise SystemExit(1)

# Build mapping from cpp exercises difficulty folders
mapping = {}
if os.path.isdir(CPP_EX):
    for diff in os.listdir(CPP_EX):
        diff_dir = os.path.join(CPP_EX, diff)
        if not os.path.isdir(diff_dir):
            continue
        for fn in os.listdir(diff_dir):
            if os.path.isfile(os.path.join(diff_dir, fn)):
                base, _ = os.path.splitext(fn)
                mapping[base] = diff

print('Loaded mapping from C++ exercises:', len(mapping), 'entries')

with open(PAGE, 'r', encoding='utf-8') as f:
    data = json.load(f)

changes = []
missed = []

def walk_list(lst, parent_path=''):
    for i, item in enumerate(lst):
        if isinstance(item, dict):
            if item.get('type') == 'code':
                # If already has path, leave
                if 'path' in item:
                    continue
                name = item.get('name')
                if not name:
                    continue
                diff = mapping.get(name)
                if not diff:
                    missed.append({'name': name, 'parent': parent_path})
                    continue
                new_path = f"exercises/{diff}/{name}"
                item.pop('name', None)
                item['path'] = new_path
                changes.append({'name': name, 'path': new_path, 'parent': parent_path})
            else:
                # recurse into content lists or blocks
                if 'content' in item and isinstance(item['content'], list):
                    walk_list(item['content'], parent_path + '/' + item.get('id', ''))
                if 'blocks' in item and isinstance(item['blocks'], list):
                    for b in item['blocks']:
                        if isinstance(b, dict) and 'content' in b and isinstance(b['content'], list):
                            walk_list(b['content'], parent_path + '/' + b.get('id', ''))
        elif isinstance(item, list):
            walk_list(item, parent_path)

# Top-level content
if 'content' in data and isinstance(data['content'], list):
    walk_list(data['content'], '/content')

# Write back if changes
if changes:
    with open(PAGE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

print('Changes made:', len(changes))
for c in changes:
    print(f"- {c['name']} -> {c['path']} (parent: {c['parent']})")

if missed:
    print('\nUnmapped names (need manual mapping):', len(missed))
    for m in missed:
        print(f"- {m['name']} (parent: {m['parent']})")

print('Done')
