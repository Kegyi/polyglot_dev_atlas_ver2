import os
import re

# Absolute candidate paths for this workspace (Windows)
root = 'c:/Users/Kegyi/C++/TestProject/polyglot_dev_atlas'
candidates = [
    os.path.join(root, 'content2', 'codes_registry.json'),
    os.path.join(root, 'content2', 'codes', 'codes_registry.json'),
]
pattern = re.compile(r'"(/content2/docs/lcci_)(\d{2})_(\d{2})_([^/\"]+)(/README\.md)?"')

def repl(m):
    prefix = '/content2/docs/lcci'
    chapter = m.group(2)
    topic = m.group(3) + '_' + m.group(4)
    tail = m.group(5) or ''
    return '"{}/{}/{}{}"'.format(prefix, chapter, topic, tail)

any_updated = 0
for target in candidates:
    if not os.path.exists(target):
        continue
    print('Processing:', target)
    with open(target, 'r', encoding='utf-8') as f:
        text = f.read()
    new_text, n = pattern.subn(repl, text)
    if n == 0:
        print('  No changes required')
    else:
        with open(target, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print('  Updated', n, 'entries in', target)
        any_updated += n

if any_updated == 0:
    print('Finished: no updates across candidates')
else:
    print('Finished: total updates =', any_updated)
