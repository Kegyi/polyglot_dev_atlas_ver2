"""Dereference local $ref and string path entries (restricted to content/scheets/)
then validate the fully-dereferenced page JSON against the page schema.

Usage:
  python deref_validate.py --page content/pages/scheets.page.json

Security: refs are resolved only under the `content/scheets` directory; path traversal is blocked.
"""
from __future__ import annotations
import json
from pathlib import Path
import argparse
import sys
from typing import Any, Dict, Set
from jsonschema import validate, ValidationError, SchemaError

ROOT = Path(__file__).resolve().parents[2]
SCHEETS_DIR = (ROOT / "content" / "scheets").resolve()
SCHEMA_PATH = (ROOT / "content" / "schema" / "page_schema.json").resolve()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def is_within_dir(path: Path, directory: Path) -> bool:
    try:
        path = path.resolve()
    except Exception:
        return False
    try:
        return directory.resolve() in (path.resolve(),) or directory.resolve() in path.resolve().parents
    except Exception:
        return False


def resolve_ref_path(ref: str, base_dir: Path) -> Path:
    # Accept absolute-like starting with /content/... or relative paths
    if ref.startswith('/'):
        cand = ROOT.joinpath(ref.lstrip('/'))
    else:
        cand = (base_dir / ref)
    return cand.resolve()


def deref(node: Any, base_dir: Path, seen_files: Set[Path]) -> Any:
    # Strings that point to scheet files are treated as refs too
    if isinstance(node, str):
        if node.startswith('/content/scheets/') or node.endswith('.scheet.json'):
            ref_path = resolve_ref_path(node, base_dir)
            if not is_within_dir(ref_path, SCHEETS_DIR):
                raise ValueError(f"Ref path outside allowed scheets dir: {ref_path}")
            if ref_path in seen_files:
                return load_json(ref_path)  # avoid infinite recursion by returning raw (already seen)
            data = load_json(ref_path)
            seen_files.add(ref_path)
            return deref(data, ref_path.parent, seen_files)
        return node

    if isinstance(node, list):
        return [deref(x, base_dir, seen_files) for x in node]

    if isinstance(node, dict):
        # If object is exactly a $ref token, resolve it
        if set(node.keys()) == {"$ref"}:
            ref = node["$ref"]
            if not isinstance(ref, str):
                raise ValueError("$ref must be a string path")
            ref_path = resolve_ref_path(ref, base_dir)
            if not is_within_dir(ref_path, SCHEETS_DIR):
                raise ValueError(f"Ref path outside allowed scheets dir: {ref_path}")
            if ref_path in seen_files:
                return load_json(ref_path)
            data = load_json(ref_path)
            seen_files.add(ref_path)
            return deref(data, ref_path.parent, seen_files)

        # Otherwise recursively deref properties
        out: Dict[str, Any] = {}
        for k, v in node.items():
            out[k] = deref(v, base_dir, seen_files)
        return out

    # primitives
    return node


def build_wrapper_schema(raw_schema: Dict[str, Any]) -> Dict[str, Any]:
    # The repo's page_schema.json defines top-level properties rather than a full object schema.
    # Wrap it into a proper root schema for validation.
    definitions = raw_schema.get("definitions")
    props = {k: v for k, v in raw_schema.items() if k != "definitions"}
    wrapper = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": props,
        "additionalProperties": False,
    }
    if definitions:
        wrapper["definitions"] = definitions
    return wrapper


def collect_refs(node: Any, base_dir: Path) -> Set[Path]:
    refs: Set[Path] = set()
    if isinstance(node, str):
        if node.startswith('/content/scheets/') or node.endswith('.scheet.json'):
            refs.add(resolve_ref_path(node, base_dir))
        return refs
    if isinstance(node, list):
        for item in node:
            refs.update(collect_refs(item, base_dir))
        return refs
    if isinstance(node, dict):
        if '$ref' in node and isinstance(node['$ref'], str):
            refs.add(resolve_ref_path(node['$ref'], base_dir))
        for v in node.values():
            refs.update(collect_refs(v, base_dir))
        return refs
    return refs


def validate_page(page_path: Path, schema_path: Path, write_deref: Path | None = None) -> int:
    # 1) Validate the page file as authored (with string refs or $ref) against page_schema
    page = load_json(page_path)
    raw_schema = load_json(schema_path)
    wrapper = build_wrapper_schema(raw_schema)
    # Allow authored pages to include simple $ref objects for content items
    try:
        contents_prop = wrapper['properties'].get('contents')
        if contents_prop and 'additionalProperties' in contents_prop:
            inner = contents_prop['additionalProperties'].get('additionalProperties')
            if inner and isinstance(inner.get('oneOf'), list):
                ref_obj_schema = {
                    'type': 'object',
                    'properties': { '$ref': { 'type': 'string' } },
                    'required': ['$ref'],
                    'additionalProperties': False,
                }
                # avoid duplicate
                if ref_obj_schema not in inner['oneOf']:
                    inner['oneOf'].append(ref_obj_schema)
    except Exception:
        pass
    try:
        validate(instance=page, schema=wrapper)
        print("VALID: page file conforms to page_schema.json")
    except ValidationError as e:
        print("PAGE VALIDATION ERROR:", e.message)
        print('path:', list(e.path))
        return 3
    except SchemaError as e:
        print("SCHEMA ERROR:", e)
        return 4

    # 2) Collect all scheet refs from the page and validate each scheet file against scheet_schema
    refs = collect_refs(page, page_path.parent)
    if not refs:
        print("No scheet references found.")

    scheet_schema_path = (ROOT / 'content' / 'schema' / 'scheet_schema.json')
    if not scheet_schema_path.exists():
        print(f"Scheet schema not found at {scheet_schema_path}; skipping scheet validation.")
    else:
        scheet_schema = load_json(scheet_schema_path)
        for r in sorted(refs):
            try:
                if not is_within_dir(r, SCHEETS_DIR):
                    print(f"SKIP: ref outside scheets dir: {r}")
                    continue
                data = load_json(r)
                validate(instance=data, schema=scheet_schema)
                print(f"VALID: scheet {r.name} ok")
            except ValidationError as e:
                print(f"SCHEET VALIDATION ERROR for {r}:", e.message)
                return 5
            except Exception as e:
                print(f"ERROR loading/validating scheet {r}:", e)
                return 6

    # 3) If requested, write a fully-dereferenced page JSON (useful for downstream pipelines)
    if write_deref:
        try:
            deref_page = deref(page, page_path.parent, set())
            write_deref.write_text(json.dumps(deref_page, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"Wrote dereferenced page to {write_deref}")
        except Exception as e:
            print("DEREFERENCE ERROR:", e)
            return 2

    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Dereference local $ref and validate against page schema")
    p.add_argument('--page', default=str(ROOT / 'content' / 'pages' / 'scheets.page.json'))
    p.add_argument('--schema', default=str(SCHEMA_PATH))
    p.add_argument('--write-deref', default=None, help='Optional path to write dereferenced JSON')
    args = p.parse_args(argv)
    exit_code = validate_page(Path(args.page), Path(args.schema), Path(args.write_deref) if args.write_deref else None)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
