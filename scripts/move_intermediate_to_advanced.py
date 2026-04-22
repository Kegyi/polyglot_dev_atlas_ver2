import json
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(__file__))
PAGE = os.path.join(ROOT, 'content', 'pages', 'course', 'exercises.json')
SNIPPETS = os.path.join(ROOT, 'content', 'snippets')

with open(PAGE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# find advanced basenames from advanced_exercises block
advanced_names = set()
for item in data['content']:
    if item.get('type') == 'blocks':
        for b in item.get('blocks', []):
            if b.get('id') == 'advanced_exercises' or b.get('id') == 'advanced_exercises':
                # advanced_exercises found as its own block object
                for c in b.get('content', []):
                    for inner in c.get('blocks', []):
                        for part in inner.get('content', []):
                            if part.get('type') == 'code' and 'path' in part:
                                advanced_names.add(os.path.basename(part['path']))

# fallback: also scan for any exercises/advanced/* paths anywhere
for item in data['content']:
    if item.get('type') == 'blocks':
        for b in item.get('blocks', []):
            for c in b.get('content', []):
                if c.get('type') == 'blocks':
                    for inner in c.get('blocks', []):
                        for part in inner.get('content', []):
                            if part.get('type') == 'code' and 'path' in part:
                                p = part['path']
                                if p.startswith('exercises/advanced/'):
                                    advanced_names.add(os.path.basename(p))

if not advanced_names:
    print('No advanced exercises discovered; aborting.')
    raise SystemExit(1)

print('Advanced names:', advanced_names)

# remove intermediate occurrences whose code path basename is in advanced_names
changed = False
for item in data['content']:
    if item.get('type') == 'blocks':
        for b in item.get('blocks', []):
            if b.get('id') == 'intermediate_exercises':
                new_content = []
                for c in b.get('content', []):
                    if c.get('type') == 'blocks':
                        kept_blocks = []
                        for inner in c.get('blocks', []):
                            # check inner.content for code path
                            move_this = False
                            for part in inner.get('content', []):
                                if part.get('type') == 'code' and 'path' in part:
                                    name = os.path.basename(part['path'])
                                    if name in advanced_names:
                                        move_this = True
                                        break
                            if not move_this:
                                kept_blocks.append(inner)
                            else:
                                print('Removing intermediate block', inner.get('id'))
                                changed = True
                        if kept_blocks:
                            c['blocks'] = kept_blocks
                            new_content.append(c)
                        else:
                            # skip the entire c if empty
                            pass
                    else:
                        new_content.append(c)
                b['content'] = new_content

if changed:
    with open(PAGE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print('Updated exercises.json; removed duplicate intermediate entries.')
else:
    print('No changes to exercises.json needed.')

# Move snippet files from intermediate -> advanced for each language
moved = []
for lang in os.listdir(SNIPPETS):
    lang_dir = os.path.join(SNIPPETS, lang)
    ex_dir = os.path.join(lang_dir, 'exercises')
    if not os.path.isdir(ex_dir):
        continue
    inter_dir = os.path.join(ex_dir, 'intermediate')
    adv_dir = os.path.join(ex_dir, 'advanced')
    if not os.path.isdir(inter_dir):
        continue
    os.makedirs(adv_dir, exist_ok=True)
    for name in advanced_names:
        # move any files starting with name.* from intermediate to advanced
        found = False
        for fn in os.listdir(inter_dir):
            if fn.startswith(name + '.') or fn == name:
                src = os.path.join(inter_dir, fn)
                dst = os.path.join(adv_dir, fn)
                print('Moving', src, '->', dst)
                shutil.move(src, dst)
                moved.append(dst)
                found = True
        if not found:
            # also check nested folder named name
            nested = os.path.join(inter_dir, name)
            if os.path.isdir(nested):
                target = os.path.join(adv_dir, name)
                print('Moving dir', nested, '->', target)
                shutil.move(nested, target)
                moved.append(target)

print('Files moved:', moved)
