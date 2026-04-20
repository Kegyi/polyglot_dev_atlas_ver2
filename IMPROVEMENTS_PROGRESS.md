# Implementation Progress — Polyglot Dev Atlas v2

Status snapshot (2026-04-20)

- Overall completion (migration scope): ~78%

## Legacy Coverage Audit

Legacy baseline discovered:
- Legacy structured source files under `polyglot_dev_atlas/content`: 14 JSON files.
- Legacy bundled output is still represented in `polyglot_dev_atlas/output/polyglot_dev_atlas.html`.

v2 current content footprint:
- `content/pages`: 126 JSON pages.
- Mode split by path: atlas (5), course (110), meta (10), root index (1).

Covered from legacy:
- `workflow` page exists in v2 (`content/pages/atlas/workflow.json`).
- `principles` page exists in v2 (`content/pages/atlas/principles.json`).
- `design patterns` page exists in v2 (`content/pages/atlas/design_patterns.json`).
- Interview chapter/problem tree exists in v2 (`content/pages/course/interview/**`).

Partially covered from legacy:
- `course/basics` and `course/problems` exist but are still high-level placeholders.
- Interview pages are scaffolded, but 100 pages still contain `See legacy docs:` markers and need full content materialization.

Missing or underdeveloped relative to legacy intent:
- Keywords are not yet a fully dynamic language-aware system:
  - Definitions exist for 5 languages in `content/definitions/keywords/*.json`.
  - Rendered keyword pages currently exist only for index and C++ (`content/pages/atlas/keywords/index.json`, `content/pages/atlas/keywords/cpp.json`).
  - No runtime wiring currently consumes keyword definitions to render by selected language(s).

## Active Migration Queue (Trimmed)

Items removed from active queue because already covered:
- Blocks-based renderer foundation.
- Recursive build scan and mode-aware navigation generation.
- Language selector and compare/single slot state persistence.
- Legacy interview page generation pipeline.

Active high-priority work:
1. Keyword architecture completion (single Keywords nav entry + selected-language rendering).
2. Replace `See legacy docs:` placeholders with normalized v2 content blocks (problem statement, constraints, examples, complexity, code).
3. Expand `course/basics` and `course/problems` from landing pages into topic pages comparable to legacy depth.
4. CI quality gates for schema/content validation.

## Keywords Migration Plan (Execution-Ready)

Target behavior:
- One `Keywords` entry in Atlas navigation.
- Page renders only selected language content in single mode.
- Page renders selected pair in compare mode.

Planned implementation steps:
1. Introduce a normalized keywords page model:
  - Keep one page at `content/pages/atlas/keywords/index.json`.
  - Add a block type (for example `keywords_matrix`) that references `content/definitions/keywords/*.json`.
2. Build-time aggregation:
  - Extend `build_system/core.py` to load all keyword definition files into one payload embedded in the generated keywords page.
3. Runtime renderer:
  - Implement renderer in `assets/js/selection_engine.js` or a dedicated renderer module.
  - Bind rendering to root attributes `data-selection-mode`, `data-primary`, `data-secondary`.
4. UX rules:
  - Single mode: show one keyword table.
  - Double mode: show side-by-side comparison table with diff highlights.
  - Add graceful fallback if a selected language has no keyword dataset.
5. Content completion:
  - Fill missing language datasets to match `content/definitions/languages.json`.
6. Validation:
  - Add schema checks for keyword definition shape and duplicate keyword detection.
7. Remove obsolete keyword page-per-language pattern:
  - Deprecate `content/pages/atlas/keywords/cpp.json` after dynamic index rendering is in place.

## Obsolete Candidates (Do Not Delete Blindly)

High confidence (safe to archive/remove after backup):
- `legacy_build.py`
- `legacy_index.html`
- `debug_mockup.html`
- `index_mock.html`

Medium confidence (remove only after feature parity checks):
- `legacy_content/**` (still referenced during migration and by generated interview stubs).
- Migration helper scripts in `scripts/` once their target domains are fully migrated.

## Definition of Done for Migration

Migration phase can be considered complete when:
- No `See legacy docs:` markers remain in `content/pages/**`.
- `course/basics` and `course/problems` are expanded beyond placeholder landing pages.
- Keywords page is fully dynamic and selected-language aware with compare support.
- Legacy runtime artifacts are archived and no longer required for build or docs.
