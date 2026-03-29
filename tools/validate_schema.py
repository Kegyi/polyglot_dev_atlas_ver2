import os
import sys
import json

try:
    import jsonschema
except Exception:
    print("jsonschema is not installed. Run: pip install jsonschema")
    sys.exit(2)


def find_schema(content_root: str):
    candidates = [
        os.path.join(content_root, 'core', 'page_schema.json'),
        os.path.join(content_root, 'core', 'schema.json'),
        os.path.join(content_root, 'page_schema.json'),
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None


def validate_all(content_root: str):
    schema_path = find_schema(content_root)
    if not schema_path:
        print('No schema file found under content/core or content root. Skipping validation.')
        return 0

    with open(schema_path, 'r', encoding='utf-8') as sf:
        schema = json.load(sf)

    pages_dir = os.path.join(content_root, 'pages')
    if not os.path.isdir(pages_dir):
        print('No pages/ directory found under content/.')
        return 1

    errors = 0
    for fname in sorted(os.listdir(pages_dir)):
        if not fname.endswith('.page.json'):
            continue
        path = os.path.join(pages_dir, fname)
        with open(path, 'r', encoding='utf-8') as pf:
            try:
                doc = json.load(pf)
            except Exception as e:
                print(f'[ERROR] Failed to parse {fname}: {e}')
                errors += 1
                continue

        try:
            jsonschema.validate(instance=doc, schema=schema)
        except jsonschema.ValidationError as ve:
            print(f'[INVALID] {fname}: {ve.message}')
            errors += 1
        except Exception as e:
            print(f'[ERROR] {fname}: {e}')
            errors += 1

    if errors:
        print(f'Validation completed: {errors} file(s) failed.')
        return 2
    print('Validation completed: all files valid.')
    return 0


if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(__file__))
    content_root = os.path.join(root, 'content')
    sys.exit(validate_all(content_root))
