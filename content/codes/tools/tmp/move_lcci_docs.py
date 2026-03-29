import json
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DOCS = REPO / "content2" / "docs"
LCCI_ROOT = DOCS / "lcci"
LCCI_JSON = REPO / "content2" / "codes" / "json" / "lcci.json"

mapping = {}

for p in sorted(DOCS.iterdir()):
    name = p.name
    if not p.is_dir():
        continue
    if not name.startswith("lcci_"):
        continue
    # split into at most 4 parts: lcci, chap, sub, rest
    parts = name.split("_", 3)
    if len(parts) >= 4:
        chap = parts[1]
        sub = parts[2]
        rest = parts[3]
        newname = f"{sub}_{rest}"
    else:
        # fallback
        chap = parts[1] if len(parts) > 1 else "misc"
        newname = "_".join(parts[2:]) or name

    target = LCCI_ROOT / chap / newname
    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"Moving {p} -> {target}")
    # Use shutil.move to preserve contents
    shutil.move(str(p), str(target))
    mapping[name] = target.relative_to(REPO)

# Update lcci.json meta.docs paths
if LCCI_JSON.exists():
    data = json.loads(LCCI_JSON.read_text(encoding="utf-8"))
    changed = 0
    # data structure is nested: chapter -> sub -> name -> entry
    for chap, subs in list(data.items()):
        for sub, entries in list(subs.items()):
            for name, entry in list(entries.items()):
                meta = entry.get("meta")
                if not meta:
                    continue
                docs = meta.get("docs")
                if not docs:
                    continue
                # docs may contain old folder name; find any mapping whose key is in the docs path
                for old, newrel in mapping.items():
                    if old in docs:
                        newpath = f"/{newrel.as_posix()}/README.md"
                        meta["docs"] = newpath
                        changed += 1
                        break
    if changed:
        LCCI_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated {changed} meta.docs entries in {LCCI_JSON}")
else:
    print(f"{LCCI_JSON} not found; skipped JSON updates")

print("Done")
