#!/usr/bin/env python3
import re
from pathlib import Path
p = Path('c:/Users/Kegyi/C++/TestProject/polyglot_dev_atlas/content2/codes_registry.json')
s = p.read_text(encoding='utf-8')
# replace /content2/docs/lcci/01/02_name/README.md -> /content2/docs/lcci/01/02_name/README.md
s2, n = re.subn(r'(/content2/docs/)lcci_(\d{2})_(\d{2})_([a-z0-9_]+)', r"\1lcci/\2/\3_\4", s)
if n:
    p.write_text(s2, encoding='utf-8')
    print(f'Updated {n} occurrences in {p}')
else:
    print('No changes')
