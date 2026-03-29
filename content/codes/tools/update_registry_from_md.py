#!/usr/bin/env python3
"""Parse markdown files and update content/codes JSON group files.

This version validates dot-separated registry paths like
`01.01.is_unique.languages.cpp` before applying updates.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
import sys

# Compute repo root (three levels up from content/codes/tools)
REPO_ROOT = Path(__file__).resolve().parents[3]
SRC_JSON = REPO_ROOT / "content" / "codes" / "codes_registry.json"
# We'll look for markdown files in the `markdown/` folder only.
MD_DIR = SRC_JSON.parent / "markdown"
JSON_DIR = SRC_JSON.parent / "json"


MARKER_RE = re.compile(
    r"<!--\s*REGISTRY_PATH:\s*(?P<path>[^\s]+)\s*-->.*?```(?P<lang>[^\n`]*)\n(?P<code>.*?)\n```",
    re.S,
)

# Validate a dot-separated path that ends with `.languages.<lang>`
PATH_VALIDATE_RE = re.compile(r"^[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*\.languages\.[A-Za-z0-9_\-+]+$")


def load_json():
    if not SRC_JSON.exists():
        print(f"JSON not found: {SRC_JSON}")
        sys.exit(2)
    return json.loads(SRC_JSON.read_text(encoding="utf-8"))


def save_json(data):
    SRC_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def set_by_path(data: dict, path: str, value: str):
    parts = path.split('.')
    target = data
    for p in parts[:-1]:
        if p not in target or not isinstance(target[p], dict):
            target[p] = {}
        target = target[p]
    target[parts[-1]] = value


def main():
    if not MD_DIR.exists():
        print(f"Markdown directory not found: {MD_DIR}")
        sys.exit(2)

    # Collect markdown files under markdown/ and gather matches from them
    md_files = sorted(MD_DIR.glob("*.md"))
    if not md_files:
        print("No markdown files found in markdown/; nothing to do.")
        return

    # Build a list of marker matches from all markdown files
    all_matches = []
    for mdp in md_files:
        mdtext = mdp.read_text(encoding="utf-8")
        for m in MARKER_RE.finditer(mdtext):
            all_matches.append((mdp, m))

    # Determine whether the registry is an index of groups or a monolithic file.
    registry = load_json()
    is_index = any(isinstance(v, dict) and ("file" in v or "markdown" in v) for v in registry.values())

    if not is_index:
        # legacy single-file workflow: update the single JSON with matches from the markdown/ files
        data = registry
        for mdp, m in all_matches:
            path = m.group('path').strip()
            if not PATH_VALIDATE_RE.match(path):
                print(f"Skipping invalid path in {mdp.name}: {path}")
                continue
            code = m.group('code')
            code = code.rstrip('\n')
            set_by_path(data, path, code)
            print(f"Updated: {path}")
        save_json(data)
        print(f"Wrote {SRC_JSON}")
        return

    # If index is present, load all group JSONs into memory, then update them based on markdown files.
    group_index = registry
    group_data: dict[str, dict] = {}
    # Load group JSON files
    for g, v in group_index.items():
        file_rel = v.get("file")
        if not file_rel:
            group_data[g] = {}
            continue
        group_json_path = (SRC_JSON.parent / file_rel).resolve()
        if group_json_path.exists():
            group_data[g] = json.loads(group_json_path.read_text(encoding="utf-8"))
        else:
            group_data[g] = {}

    # Apply matches collected from markdown/ files
    for mdp, m in all_matches:
        path = m.group('path').strip()
        if not PATH_VALIDATE_RE.match(path):
            print(f"Skipping invalid path in {mdp.name}: {path}")
            continue
        code = m.group('code').rstrip('\n')
        key = path.split('.', 1)[0]
        # Find which group currently contains this key
        found = False
        for g, entries in group_data.items():
            if key in entries:
                # Set using the full path under the group's root
                set_by_path(group_data[g], path, code)
                print(f"Updated: {path} in group {g}")
                found = True
                break
        if not found:
            # Put into a fallback 'common' group if present, else first group
            target_group = 'common' if 'common' in group_data else next(iter(group_data.keys()), None)
            if target_group is None:
                print(f"No group to place {path}; skipping")
                continue
            set_by_path(group_data[target_group], path, code)
            print(f"Updated: {path} in group {target_group} (new)")

    # Write back each group JSON to its file
    for g, entries in group_data.items():
        file_rel = group_index[g].get("file")
        if not file_rel:
            # choose a default path
            file_rel = f"json/{g}.json"
            group_index[g]["file"] = file_rel
        group_json_path = (SRC_JSON.parent / file_rel).resolve()
        group_json_path.parent.mkdir(parents=True, exist_ok=True)
        group_json_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {group_json_path}")

    # Rewrite index (in case we added default paths)
    SRC_JSON.write_text(json.dumps(group_index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {SRC_JSON} (index updated)")


if __name__ == '__main__':
    main()
