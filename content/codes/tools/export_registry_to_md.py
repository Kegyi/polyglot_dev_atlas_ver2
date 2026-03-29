#!/usr/bin/env python3
"""Export content/codes_registry.json -> per-group json/ + markdown files.

Placed in `content/codes/tools` so maintainers can run it from the repo root:

python content/codes/tools/export_registry_to_md.py
"""
from __future__ import annotations
import json
from pathlib import Path
import sys

# Compute repo root (three levels up from content/codes/tools)
REPO_ROOT = Path(__file__).resolve().parents[3]
SRC = REPO_ROOT / "content" / "codes" / "codes_registry.json"

# Grouping rules: list of (group_name, regex)
GROUP_RULES = [
    ("lcci", r"^lcci_"),
    ("exercise", r"^exercise_"),
    (
        "design_pattern",
        r"^(abstract_factory|adapter|bridge|builder|chain_of_responsibility|command|composite|decorator|facade|factory_method|flyweight|interpreter|iterator|mediator|memento|observer|prototype|proxy|singleton|state|strategy|template_method|visitor)$",
    ),
    ("problems", r"^(arrays_and_collections|balanced_brackets|bit_manipulation|matrix_mul|top_k_frequent|word_count|grid_shortest_path|concurrency_demo)$"),
    ("common", r".*"),
]


def choose_group(key: str) -> str:
    import re

    for g, pat in GROUP_RULES:
        if re.match(pat, key):
            return g
    return "common"


def safe_str(x):
    return "" if x is None else str(x)


def write_md(data: dict):
    base = OUT.parent
    json_dir = base / "json"
    md_dir = base / "markdown"
    json_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    is_index = any(isinstance(v, dict) and ("file" in v or "markdown" in v) for v in data.values())

    groups: dict[str, dict] = {}
    if is_index:
        for g, v in data.items():
            file_rel = v.get("file")
            if not file_rel:
                continue
            group_json = (SRC.parent / file_rel).resolve()
            if group_json.exists():
                groups[g] = json.loads(group_json.read_text(encoding="utf-8"))
    else:
        for key in sorted(data.keys()):
            grp = choose_group(key)
            groups.setdefault(grp, {})[key] = data[key]

    index = {}
    for g, entries in sorted(groups.items()):
        group_json_path = json_dir / f"{g}.json"
        group_md_path = md_dir / f"{g}.md"
        group_json_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        with group_md_path.open("w", encoding="utf-8") as f:
            f.write(f"# Codes registry — {g}\n\n")
            f.write("This file contains code snippets exported from content/codes_registry.json.\n")
            f.write("Edit this file and run `content/codes/tools/update_registry_from_md.py` to push changes back.\n\n")

            for key in sorted(entries.keys()):
                entry = entries[key] or {}
                f.write(f"## {key}\n\n")

                meta = entry.get("meta", {})
                docs = meta.get("docs")
                if docs:
                    f.write(f"- Docs: {safe_str(docs)}\n")
                    f.write("\n")

                languages = entry.get("languages") or {}
                if not languages:
                    f.write("*(no language snippets)*\n\n")
                    continue

                for lang in sorted(languages.keys()):
                    code = languages[lang] or ""
                    marker = f"REGISTRY_PATH: {key}.languages.{lang}"
                    f.write(f"<!-- {marker} -->\n")
                    f.write(f"### {lang}\n\n")
                    fence_lang = lang if all(c.isalnum() or c in "-_+" for c in lang) else ""
                    f.write(f"```{fence_lang}\n")
                    f.write(code.rstrip() + "\n")
                    f.write("```\n\n")

        index[g] = {"file": f"json/{g}.json", "markdown": f"markdown/{g}.md"}

    SRC.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {SRC} (index) and {len(groups)} group files in json/ and markdown/")


def main():
    if not SRC.exists():
        print(f"Source not found: {SRC}")
        sys.exit(2)
    data = json.loads(SRC.read_text(encoding="utf-8"))
    write_md(data)
    print("Wrote index and per-group files in json/ and markdown/")


if __name__ == "__main__":
    main()
