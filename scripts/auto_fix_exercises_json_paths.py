import os
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'content', 'pages', 'course', 'exercieses.json')
SNIPPETS_ROOT = os.path.join(ROOT, 'content', 'snippets')

with open(PAGE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build an index: name -> list of (lang, difficulty, relpath)
index = {}
for lang in os.listdir(SNIPPETS_ROOT):
    lang_dir = os.path.join(SNIPPETS_ROOT, lang)
    if not os.path.isdir(lang_dir):
        continue
    exercises_dir = os.path.join(lang_dir, 'exercises')
    if not os.path.isdir(exercises_dir):
        continue
    for root, dirs, files in os.walk(exercises_dir):
        rel = os.path.relpath(root, exercises_dir).replace('\\', '/')
        parts = rel.split('/') if rel != '.' else []
        difficulty = parts[0] if parts else None
        for fn in files:
            base, _ = os.path.splitext(fn)
            name = base
            index.setdefault(name, []).append({'lang': lang, 'difficulty': difficulty, 'path': os.path.join('exercises', rel, fn).replace('\\','/') if rel != '.' else os.path.join('exercises', fn)})

print('Indexed', len(index), 'snippet files under exercises across languages')

changes = []
missed = []

def walk_and_fix(lst, parent_path=''):
    for item in lst:
        if isinstance(item, dict):
            if item.get('type') == 'code':
                if 'path' in item:
                    continue
                name = item.get('name')
                if not name:
                    continue
                # look up in index
                hits = index.get(name, [])
                chosen = None
                # prefer cpp with difficulty
                for h in hits:
                    if h['lang'] == 'cpp' and h['difficulty']:
                        chosen = h
                        break
                if not chosen and hits:
                    # prefer any hit with known difficulty
                    for h in hits:
                        if h['difficulty']:
                            chosen = h
                            break
                if not chosen and hits:
                    chosen = hits[0]
                if chosen and chosen.get('difficulty'):
                    diff = chosen['difficulty']
                    new_path = f"exercises/{diff}/{name}"
                    item.pop('name', None)
                    item['path'] = new_path
                    changes.append({'name': name, 'path': new_path, 'parent': parent_path, 'source': chosen})
                else:
                    missed.append({'name': name, 'parent': parent_path, 'hits': hits})
            else:
                if 'content' in item and isinstance(item['content'], list):
                    walk_and_fix(item['content'], parent_path + '/' + item.get('id',''))
                if 'blocks' in item and isinstance(item['blocks'], list):
                    for b in item['blocks']:
                        if isinstance(b, dict) and 'content' in b and isinstance(b['content'], list):
                            walk_and_fix(b['content'], parent_path + '/' + b.get('id',''))

if 'content' in data and isinstance(data['content'], list):
    walk_and_fix(data['content'], '/content')

if changes:
    with open(PAGE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

print('Auto changes:', len(changes))
for c in changes:
    src = c['source']
    print(f"- {c['name']} -> {c['path']} (found: lang={src['lang']} path={src['path']})")

if missed:
    print('\nStill unmapped:', len(missed))
    for m in missed[:50]:
        print(f"- {m['name']} (parent: {m['parent']}) hits={len(m['hits'])}")

print('Done')
