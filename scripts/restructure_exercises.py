import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS = os.path.join(ROOT, 'content', 'snippets')

LANGS = ['python', 'go', 'typescript', 'scala2', 'scala3']

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

for lang in LANGS:
    lang_dir = os.path.join(SNIPPETS, lang)
    exercises_dir = os.path.join(lang_dir, 'exercises')
    if not os.path.isdir(exercises_dir):
        print(f"Skipping {lang}: no exercises folder")
        continue

    items = [f for f in os.listdir(exercises_dir) if os.path.isfile(os.path.join(exercises_dir, f))]
    if not items:
        print(f"No exercise files for {lang}")
        continue

    # Prepare rename_map.csv
    rm_path = os.path.join(lang_dir, 'rename_map.csv')
    existing = []
    if os.path.exists(rm_path):
        with open(rm_path, 'r', encoding='utf-8') as f:
            existing = f.read().splitlines()
    else:
        # add header for CSV style used in this repo
        existing = ['"SourcePath","NewName"']

    changed = False
    for fn in items:
        base, ext = os.path.splitext(fn)
        # Create subdir per exercise
        target_dir = os.path.join(exercises_dir, base)
        ensure_dir(target_dir)
        src = os.path.join(exercises_dir, fn)
        dst_name = fn  # keep original filename inside subdir
        dst = os.path.join(target_dir, dst_name)
        if os.path.exists(dst):
            print(f"Already moved: {dst}")
        else:
            shutil.move(src, dst)
            print(f"Moved {src} -> {dst}")
            changed = True

        # Append mapping line: "exercises/<base>/<fn>","exercises_<base><ext>"
        # Use legacy flat name as NewName prefixed with exercises_
        newname = f"exercises_{base}{ext}"
        line = f'"exercises/{base}/{dst_name}","{newname}"'
        if line not in existing:
            existing.append(line)
            changed = True

    if changed:
        with open(rm_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(existing) + '\n')
        print(f"Updated rename_map.csv for {lang}")
    else:
        print(f"No changes for {lang}")

print("Done")
