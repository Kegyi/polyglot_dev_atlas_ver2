import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS = os.path.join(ROOT, 'content', 'snippets')

# Languages to normalize (skip cpp which is the source of truth)
LANGS = ['python', 'go', 'typescript', 'scala2', 'scala3']

cpp_ex = os.path.join(SNIPPETS, 'cpp', 'exercises')
if not os.path.isdir(cpp_ex):
    print('C++ exercises folder not found:', cpp_ex)
    raise SystemExit(1)

# Discover difficulty dirs from C++ exercises folder
difficulties = [d for d in sorted(os.listdir(cpp_ex)) if os.path.isdir(os.path.join(cpp_ex, d))]
if not difficulties:
    print('No difficulty subfolders found in C++ exercises. Expected beginner/intermediate/advanced')
    raise SystemExit(1)

# Build mapping from exercise basename -> difficulty by scanning files inside each difficulty dir
mapping = {}
for diff in difficulties:
    diff_dir = os.path.join(cpp_ex, diff)
    for entry in os.listdir(diff_dir):
        fpath = os.path.join(diff_dir, entry)
        if os.path.isfile(fpath):
            base, ext = os.path.splitext(entry)
            mapping[base] = diff

print('Detected difficulties:', difficulties)
print('Mapped exercises from C++ count:', len(mapping))

# For each language, move files from exercises/<name>/<name>.<ext> -> exercises/<difficulty>/<name>.<ext>
for lang in LANGS:
    lang_dir = os.path.join(SNIPPETS, lang)
    ex_dir = os.path.join(lang_dir, 'exercises')
    if not os.path.isdir(ex_dir):
        print(f"Skipping {lang}: no exercises folder")
        continue

    # Ensure difficulty dirs exist
    for diff in difficulties:
        os.makedirs(os.path.join(ex_dir, diff), exist_ok=True)

    # Find per-snippet subdirs (e.g., exercises/array_reverse/array_reverse.py)
    moved = 0
    missing = 0
    for name in os.listdir(ex_dir):
        item = os.path.join(ex_dir, name)
        # Only consider directories (the per-snippet layout)
        if not os.path.isdir(item):
            continue
        # Try to find a file inside that matches the snippet base name
        files = [f for f in os.listdir(item) if os.path.isfile(os.path.join(item, f))]
        if not files:
            print(f"No files in {item}, skipping")
            continue
        # Prefer a file that starts with the folder name, else take first
        chosen = None
        for f in files:
            if f.startswith(name):
                chosen = f
                break
        if not chosen:
            chosen = files[0]
        src = os.path.join(item, chosen)
        base, ext = os.path.splitext(chosen)
        # Determine target difficulty
        diff = mapping.get(name)
        if not diff:
            print(f"No difficulty mapping for {name}; skipping move for {lang}")
            missing += 1
            continue
        dst_dir = os.path.join(ex_dir, diff)
        dst = os.path.join(dst_dir, chosen)
        if os.path.exists(dst):
            print(f"Target already exists, removing source dir: {dst}")
            # Remove the now-empty source dir if present
            try:
                shutil.rmtree(item)
            except Exception:
                pass
            continue
        shutil.move(src, dst)
        # Remove the now-empty source dir if empty
        try:
            os.rmdir(item)
        except OSError:
            pass
        print(f"Moved {src} -> {dst}")
        moved += 1

    # Update rename_map.csv: change SourcePath from exercises/<name>/<file> to exercises/<difficulty>/<file>
    rm_path = os.path.join(lang_dir, 'rename_map.csv')
    if os.path.exists(rm_path):
        with open(rm_path, 'r', encoding='utf-8') as f:
            lines = [l.rstrip('\n') for l in f]
        header = None
        if lines and 'SourcePath' in lines[0]:
            header = lines[0]
            lines = lines[1:]
        updated = [header] if header else []
        for l in lines:
            if not l.strip():
                continue
            # Format: "exercises/<base>/<file>","exercises_<base>.<ext>"
            parts = l.split(',')
            if len(parts) < 2:
                updated.append(l)
                continue
            src = parts[0].strip().strip('"')
            newname = parts[1].strip()
            # If src starts with exercises/<name>/ then adjust
            if src.startswith('exercises/'):
                rest = src[len('exercises/'):]
                seg = rest.split('/', 1)[0]
                # seg is likely the base folder
                if seg in mapping:
                    diff = mapping[seg]
                    # rebuild src path using same filename portion
                    filename = rest.split('/',1)[1] if '/' in rest else rest
                    new_src = f'exercises/{diff}/{filename}'
                    updated.append(f'"{new_src}",{newname}')
                    continue
            # otherwise keep line
            updated.append(l)
        with open(rm_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(updated) + '\n')
        print(f"Updated rename_map.csv for {lang}")
    else:
        print(f"No rename_map.csv for {lang}; skipping update")

    print(f"{lang}: moved={moved}, missing_mapping={missing}")

print('Normalization complete')
