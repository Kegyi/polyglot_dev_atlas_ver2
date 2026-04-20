# Migration Coverage Plan (Legacy -> v2)

Date: 2026-04-20

## 1) Coverage Matrix

### Legacy source inventory (polyglot_dev_atlas/content)

- adaptation_course.json -> Partially covered
  - v2 mapping: content/pages/course/index.json, content/pages/course/interview/**
  - gap: no explicit step-by-step adaptation flow page parity yet.
- adapter_insights.json -> Partially covered
  - v2 mapping: content/pages/atlas/design_patterns.json (Adapter exists)
  - gap: adapter-specific insight metadata not explicitly migrated as structured notes.
- basics_enhancements.json -> Partially covered
  - v2 mapping: content/pages/course/basics.json
  - gap: detailed sections are still placeholder-level in basics root page.
- basics_groups.json -> Partially covered
  - v2 mapping: content/pages/course/basics.json
  - gap: grouped topic pages not expanded in v2.
- content_manifest.json -> Covered
  - v2 equivalent behavior handled by recursive scan in build_system/core.py.
- course_steps.json -> Partially covered
  - v2 mapping: content/pages/course/interview/** and course landing pages.
  - gap: explicit step progression data model/page sequence still missing.
- course_steps_groups.json -> Partially covered
  - v2 mapping: course navigation folders.
  - gap: no dedicated grouped course-step view.
- design_patterns_groups.json -> Covered
  - v2 mapping: content/pages/atlas/design_patterns.json with grouped sections.
- interview_groups.json -> Covered
  - v2 mapping: content/pages/course/interview/** chapter folders.
- modern_approach_notes.json -> Partially covered
  - v2 mapping: content/pages/atlas/design_patterns.json
  - gap: modernization notes are not fully represented as structured insights.
- principles.json -> Partially covered
  - v2 mapping: content/pages/atlas/principles.json
  - gap: v2 currently includes fewer principle blocks than legacy source.
- principles_groups.json -> Covered
  - v2 mapping: principles block grouping in content/pages/atlas/principles.json.
- workflow.json -> Partially covered
  - v2 mapping: content/pages/atlas/workflow.json
  - gap: legacy had richer workflow snippets/sections than current v2 page.
- workflow_groups.json -> Covered (legacy was effectively empty)

### v2 keyword readiness

- Existing definition files:
  - content/definitions/keywords/cpp.json
  - content/definitions/keywords/csharp.json
  - content/definitions/keywords/go.json
  - content/definitions/keywords/javascript.json
  - content/definitions/keywords/rust.json
- Existing keyword pages:
  - content/pages/atlas/keywords/index.json
  - content/pages/atlas/keywords/cpp.json
- Current gap:
  - definitions are not yet dynamically rendered from selected language state.
  - one nav entry exists (keywords folder), but content remains mostly static.

## 2) Migration Priorities (Order)

1. Keywords architecture (single page, selected language rendering, compare mode support).
2. Remove all "See legacy docs:" placeholders from interview pages by materializing full structured content.
3. Expand course basics and problems from landing pages into grouped topic pages.
4. Restore missing depth for principles and workflow from legacy notes/snippets.
5. Archive/remove legacy runtime artifacts after parity verification.

## 3) Obsolete Candidates

High-confidence obsolete after parity check:
- legacy_build.py
- legacy_index.html
- debug_mockup.html
- index_mock.html

Migration-temporary (remove only when migration is complete):
- legacy_content/**
- scripts/generate_interview_pages_from_legacy.py
- other one-off migration scripts in scripts/

## 4) Keywords Execution Plan (Detailed)

1. Keep one route/page: content/pages/atlas/keywords/index.json.
2. Add a dedicated keywords block type (keywords_matrix) with source = definitions/keywords.
3. Extend build_system/core.py to bundle all keyword definitions for runtime use.
4. Implement frontend renderer that listens to data-selection-mode, data-primary, data-secondary.
5. Render rules:
   - single mode: one language table.
   - double mode: two-language comparison table.
6. Add fallback UI for missing language datasets.
7. Add content/schema validation for keyword definition integrity.
8. Deprecate content/pages/atlas/keywords/cpp.json once dynamic rendering is validated.

## 5) Cleanup Gate

Only archive/remove legacy assets when all checks are true:
- No "See legacy docs:" remains in content/pages/**.
- keywords dynamic rendering complete.
- principles/workflow depth parity accepted.
- build and manual smoke tests pass from dist/ output.
