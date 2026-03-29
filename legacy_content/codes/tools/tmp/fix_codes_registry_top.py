import re
from pathlib import Path

repo_root = Path(__file__).resolve().parents[4]
registry = repo_root / 'content2' / 'codes' / 'codes_registry.json'
backup = registry.with_suffix('.json.bak')

pattern = re.compile(r"/content2/docs/lcci_(\d{2})_(\d{2})_([^/\"]+)(/README.md)?")

if not registry.exists():
    print(f"Registry not found: {registry}")
    raise SystemExit(1)

text = registry.read_text(encoding='utf-8')
new_text, n = pattern.subn(r"/content2/docs/lcci/\1/\2_\3\4", text)

if n == 0:
    print('No changes required')
    raise SystemExit(0)

# Backup and write
backup.write_text(text, encoding='utf-8')
registry.write_text(new_text, encoding='utf-8')
print(f'Updated {n} occurrences in {registry}')
print(f'Backup saved to {backup}')
