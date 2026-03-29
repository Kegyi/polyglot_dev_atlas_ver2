# Registry export/import scripts

scripts/export_registry_to_md.py
- Generates `docs/codes_registry.md` from `content/codes_registry.json`.

scripts/update_registry_from_md.py
- Reads `docs/codes_registry.md` and updates `content/codes_registry.json` for any code blocks preceded by markers of the form `<!-- REGISTRY_PATH: key.languages.lang -->`.

Usage
-----

From the repository root:

```bash
python scripts/export_registry_to_md.py
# edit codes_registry.md
python scripts/update_registry_from_md.py
```

Notes
-----
- Only code blocks with the explicit `REGISTRY_PATH` marker are written back to the JSON.
- The importer preserves other JSON fields and writes a prettified file.
- The exporter now supports organizing markdown into optional hierarchical groups for human readability. For `lcci` we additionally support a `Section` / `Topic` layout (e.g. `Section 01` then `Topic 01 - Is Unique`).

Sections/Topics
---------------
You can organize large collections by adding section/topic structure in the markdown. The exporter will no longer emit a redundant `- Title:` line; instead each topic heading is written as `Topic <sub> - <Title>` when available. To regenerate grouped markdown files run:

```bash
python content/codes/tools/export_registry_to_md.py
```

If you need to produce a custom layout for a particular group (for example `lcci`), see `content/codes/tools/generate_lcci_md_sections.py` which creates a `Section` / `Topic` structure from `content/codes/json/lcci.json`.
