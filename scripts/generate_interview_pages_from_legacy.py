#!/usr/bin/env python3
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / 'legacy_content' / 'codes' / 'json' / 'lcci.json'
OUT_DIR = ROOT / 'content' / 'pages' / 'course' / 'interview'

slug_re = re.compile(r"[^a-z0-9]+")

def slugify(s: str) -> str:
    s = s.lower().strip()
    s = slug_re.sub('_', s)
    s = re.sub(r'_+', '_', s)
    s = s.strip('_')
    return s


def make_folder_name(cat_num: str, title: str) -> str:
    # convert '01' and 'Strings and Arrays' -> '1_strings_and_arrays'
    num = str(int(cat_num))
    slug = slugify(title)
    return f"{num}_{slug}"


def make_file_name(prob_num: str, slug: str) -> str:
    num = str(int(prob_num))
    return f"{num}_{slug}.json"


def make_code_name(cat_num: str, prob_num: str, slug: str) -> str:
    # keep two-digit numbers in code name like interview_lcci_01_01_is_unique
    cat = cat_num.zfill(2)
    prob = prob_num.zfill(2)
    return f"interview_lcci_{cat}_{prob}_{slug}"


def build_page(meta_title: str, docs: str, code_name: str):
    title = meta_title
    desc = meta_title
    page = {
        "title": title,
        "description": desc,
        "style": "text_style",
        "content": [
            {"type": "title", "text": title},
            {"type": "text", "text": desc},
            {"type": "blocks", "blocks": [
                {"id": "problem_statement", "title": "Problem Statement", "content": [
                    {"type": "text", "text": f"See legacy docs: {docs}" if docs else "Problem statement available in legacy docs."}
                ]},
                {"id": "example_cases", "title": "Example Cases", "content": [
                    {"type": "text", "text": "See example cases in the docs."}
                ]},
                {"id": "code_example", "title": "Code Example", "content": [
                    {"type": "code", "name": code_name}
                ]}
            ]}
        ]
    }
    return page


def main():
    if not LEGACY.exists():
        print(f"ERROR: legacy file not found: {LEGACY}")
        return 2
    data = json.loads(LEGACY.read_text(encoding='utf-8'))
    created = 0
    skipped = 0
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # iterate top-level chapters
    for cat_key, cat_val in data.items():
        if cat_key == 'title':
            continue
        try:
            int(cat_key)
        except Exception:
            continue
        cat_title = cat_val.get('title', f'Chapter {int(cat_key)}')
        folder_name = make_folder_name(cat_key, cat_title)
        folder_path = OUT_DIR / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)

        # iterate second-level entries
        for prob_key, prob_map in cat_val.items():
            # skip 'title' key
            if prob_key == 'title':
                continue
            # some keys are numbers mapping to dict containing slugs
            # e.g., '01': { 'is_unique': { ... } }
            # When prob_map is dict with nested slugs, iterate
            if isinstance(prob_map, dict):
                for slug_key, slug_obj in prob_map.items():
                    # slug_obj should have 'meta' and 'languages'
                    if not isinstance(slug_obj, dict) or 'meta' not in slug_obj:
                        continue
                    meta = slug_obj.get('meta', {})
                    meta_title = meta.get('title', slug_key.replace('_', ' ').title())
                    docs = meta.get('docs', '')
                    slug = slugify(slug_key)
                    file_name = make_file_name(prob_key, slug)
                    out_file = folder_path / file_name
                    code_name = make_code_name(cat_key, prob_key, slug)
                    if out_file.exists():
                        skipped += 1
                        continue
                    page = build_page(meta_title, docs, code_name)
                    out_file.write_text(json.dumps(page, indent=4, ensure_ascii=False) + "\n", encoding='utf-8')
                    created += 1
            else:
                # unexpected structure; skip
                continue

    print(f"Created {created} pages, skipped {skipped} existing files.")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
