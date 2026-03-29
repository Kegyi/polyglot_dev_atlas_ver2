import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
registry_path = root / "content2" / "codes_registry.json"

if not registry_path.exists():
    print("Registry not found:", registry_path)
    raise SystemExit(2)

with registry_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

changes = 0
for key, val in data.items():
    if not key.startswith("lcci_"):
        continue
    meta = val.get("meta")
    if not isinstance(meta, dict):
        continue
    old = meta.get("docs")
    parts = key.split("_")
    if len(parts) < 3:
        continue
    chapter = parts[1]
    rest = "_".join(parts[2:])
    new = f"/content2/docs/lcci/{chapter}/{rest}/README.md"
    if old != new:
        meta["docs"] = new
        changes += 1

if changes:
    with registry_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {changes} entries in {registry_path}")
