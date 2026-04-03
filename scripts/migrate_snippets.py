#!/usr/bin/env python3
"""
Migration script: reorganize flat snippet files into nested folders per language.
Rules (Python-targeted but applied per-language):
- design_patterns_<name> -> design_patterns/<name>.ext
- exercise_<name> or exercises_<name> -> exercises/<name>.ext
- interview_lcci_<CC>_<NN>_<rest>.ext -> interview_lcci/<CC>/<NN>_<rest>.ext
- language_basics_<name> -> language_basics/<name>.ext
- problems_<name> -> problems/<name>.ext
- fallback: leave files unchanged

This script moves files and prints actions.
"""
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNIPPETS_ROOT = ROOT / 'content' / 'snippets'

PREFIX_RULES = [
    ('design_patterns_', 'design_patterns'),
    ('exercise_', 'exercises'),
    ('exercises_', 'exercises'),
    ('language_basics_', 'language_basics'),
    ('problems_', 'problems'),
]

def ensure_dir(p: Path):
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)

moved = []
skipped = []

for lang_dir in sorted(SNIPPETS_ROOT.iterdir()):
    if not lang_dir.is_dir():
        continue
    for p in sorted(lang_dir.iterdir()):
        if p.is_dir():
            # already structured, skip
            skipped.append((p, 'is_dir'))
            continue
        name = p.name
        lower = name.lower()
        dest_dir = None
        dest_name = None
        # interview pattern
        if lower.startswith('interview_lcci_'):
            parts = name.split('_')
            # parts: ['interview','lcci','01','02','rest...']
            if len(parts) >= 4:
                chapter = parts[2]
                rest = '_'.join(parts[3:])
                dest_dir = lang_dir / 'interview_lcci' / chapter
                dest_name = rest
        else:
            for pref, folder in PREFIX_RULES:
                if lower.startswith(pref):
                    rest = name[len(pref):]
                    dest_dir = lang_dir / folder
                    dest_name = rest
                    break
        if dest_dir is None:
            skipped.append((p, 'no_rule'))
            continue
        ensure_dir(dest_dir)
        target = dest_dir / dest_name
        # Avoid overwriting: if target exists, append numeric suffix
        if target.exists():
            base = target.stem
            ext = target.suffix
            i = 2
            while True:
                newt = dest_dir / f"{base}_{i}{ext}"
                if not newt.exists():
                    target = newt
                    break
                i += 1
        try:
            shutil.move(str(p), str(target))
            moved.append((p, target))
        except Exception as e:
            skipped.append((p, f'error:{e}'))

print('Migration complete')
print(f'Moved: {len(moved)}')
for src, dst in moved[:200]:
    print(' M:', src, '->', dst)
print(f'Skipped: {len(skipped)}')
for src, reason in skipped[:200]:
    print(' S:', src, reason)
