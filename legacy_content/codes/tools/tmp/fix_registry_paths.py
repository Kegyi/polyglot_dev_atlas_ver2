from pathlib import Path
import re

root = Path('.')
registry = root / 'content2' / 'codes_registry.json'
print('CWD:', Path.cwd())
print('Looking for registry at:', registry)
print('Exists?', registry.exists())
if not registry.exists():
    # also try an alternative path used by some scripts
    alt = root / 'content2' / 'codes' / 'codes_registry.json'
    print('Trying alternative:', alt)
    if alt.exists():
        registry = alt
        print('Using alternative registry:', registry)
    else:
        print('Registry not found:', registry)
        raise SystemExit(1)

text = registry.read_text(encoding='utf-8')
# Pattern with leading slash
pattern1 = re.compile(r'(/content2/docs/lcci)_(\d{2})_(\d{2})_([A-Za-z0-9_]+)(/README\.md)?')
text2, n1 = pattern1.subn(r'\1/\2/\3_\4\5', text)
# Pattern without leading slash (just in case)
pattern2 = re.compile(r'(content2/docs/lcci)_(\d{2})_(\d{2})_([A-Za-z0-9_]+)(/README\.md)?')
text3, n2 = pattern2.subn(r'\1/\2/\3_\4\5', text2)

n = n1 + n2
if n == 0:
    print('No changes required')
else:
    registry.write_text(text3, encoding='utf-8')
    print(f'Updated {n} occurrences in', registry)
