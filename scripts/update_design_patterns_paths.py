import os
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'content', 'pages', 'atlas', 'design_patterns.json')

with open(PAGE, 'r', encoding='utf-8') as f:
    data = json.load(f)

changes = []

def walk(node, path=''):
    if isinstance(node, dict):
        if node.get('type') == 'code' and 'name' in node:
            name = node['name']
            # map design_patterns_foo -> design_patterns/foo
            if name.startswith('design_patterns_'):
                rest = name[len('design_patterns_'):]
                new_path = f'design_patterns/{rest}'
            else:
                # generic: replace underscores with slashes on first slash suggestion
                new_path = name
            node.pop('name', None)
            node['path'] = new_path
            changes.append((name, new_path, path))
        else:
            for k, v in list(node.items()):
                walk(v, path + '/' + k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, path + f'[{i}]')

walk(data)

if changes:
    with open(PAGE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

print('Updated', len(changes), 'code items:')
for c in changes:
    print('-', c[0], '->', c[1], 'at', c[2])
