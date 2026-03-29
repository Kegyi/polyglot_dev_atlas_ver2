#!/usr/bin/env python3
import re
from pathlib import Path

root = Path('content2')
pattern = re.compile(r'(?P<prefix>/content2/docs/|docs/)lcci_(?P<ch>\d{2})_(?P<sub>\d{2})_(?P<name>[a-z0-9_]+)')

updated_files = []
for p in root.rglob('*'):
    if p.is_file():
        try:
            s = p.read_text(encoding='utf-8')
        except Exception:
            continue
        new_s, n = pattern.subn(lambda m: f"{m.group('prefix')}lcci/{m.group('ch')}/{m.group('sub')}_{m.group('name')}", s)
        if n:
            p.write_text(new_s, encoding='utf-8')
            updated_files.append((str(p), n))

for fp, count in updated_files:
    print(f"Updated {count} occurrences in {fp}")
print('Done')
