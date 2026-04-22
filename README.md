# Polyglot Dev Atlas — v2

A multi-language developer reference tool enabling **side-by-side code comparison** across C++, Go, Python, TypeScript, Scala 2, and Scala 3.  
The app is a **static site** (no server needed): a Python build pipeline reads JSON content and code snippets, then renders everything into plain HTML/CSS/JS under `dist/`.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Architecture at a Glance](#2-architecture-at-a-glance)
3. [Getting Started](#3-getting-started)
4. [File & Directory Reference](#4-file--directory-reference)
   - [Root files](#41-root-files)
   - [build_system/](#42-build_system)
   - [content/](#43-content)
   - [assets/](#44-assets)
   - [templates/](#45-templates)
   - [scripts/](#46-scripts)
   - [tools/](#47-tools)
   - [.github/workflows/](#48-githubworkflows)
   - [dist/](#49-dist)
   - [Obsolete / Dead files](#410-obsolete--dead-files)
5. [Content System Deep Dive](#5-content-system-deep-dive)
   - [Page JSON format](#51-page-json-format)
   - [Block types](#52-block-types)
   - [$ref resolution](#53-ref-resolution)
   - [Code snippets](#54-code-snippets)
6. [Build System Deep Dive](#6-build-system-deep-dive)
7. [Frontend Architecture](#7-frontend-architecture)
8. [CI/CD](#8-cicd)
9. [Migration Status](#9-migration-status)
10. [Known Issues & Next Steps](#10-known-issues--next-steps)

---

## 1. Project Overview

The Atlas has **three modes**, each served as a section of the same static site:

| Mode | URL prefix | Purpose |
|------|------------|---------|
| **Atlas** | `/atlas/` | Quick-reference: design patterns, principles, workflow, keyword grids |
| **Course** | `/course/` | Learning curriculum: language basics, interview prep (17 chapters), exercises |
| **Meta** | `/meta/` | Documentation about the app itself: block types, showcases, customization guide |

All content lives in **JSON files** under `content/pages/`. The Python builder reads those files, resolves `$ref` pointers to shared definitions and raw code snippets, renders every page to HTML, assembles navigation, and writes the output to `dist/`.

---

## 2. Architecture at a Glance

```
content/ (JSON pages + code snippets)
    │
    ▼
build_system/core.py  (AtlasBuilder)
    │  • scan pages
    │  • validate JSON schema
    │  • resolve $ref pointers
    │  • render 20+ block types to HTML
    │  • assemble navigation / breadcrumbs
    │  • generate search-index.json
    │  • copy & inline assets
    │
    ▼
dist/  (static HTML — open dist/index.html in any browser)
    │
    ▼
assets/js + assets/css  (loaded at runtime in the browser)
```

---

## 3. Getting Started

**Requirements:** Python 3.10+

```bash
# Install optional but recommended dependencies
pip install -r requirements.txt   # jsonschema, watchdog

# Run a full build
python build.py

# Validate content without producing output
python build_system/core.py --validate-only

# Auto-rebuild on file changes (requires watchdog)
python build_system/core.py --watch
```

After a successful build, open `dist/index.html` in a browser — no server needed.

---

## 4. File & Directory Reference

### 4.1 Root files

| File | Purpose |
|------|---------|
| `build.py` | **Main entry point.** Imports `AtlasBuilder` from `build_system/core.py` and calls `builder.build()`. Handles top-level error reporting and prints a success summary. |
| `requirements.txt` | Two optional Python dependencies: `jsonschema>=4.0.0` (page validation) and `watchdog>=2.0.0` (watch mode). The build works without them but produces no validation or hot-reload. |
| `build_run.log` | Last build's stdout/stderr output. Useful for debugging failed builds. Not committed; regenerated on each run. |
| `CI_CD_GUIDE.md` | Documents all three GitHub Actions workflows and how to trigger them manually. |
| `IMPROVEMENTS.md` | Original six-phase improvement roadmap (Phase 1–6). Kept as a reference spec document. |
| `IMPROVEMENTS_PROGRESS.md` | Running status snapshot of what has been implemented. Updated manually. |
| `MIGRATION_COVERAGE_PLAN.md` | Maps every legacy v1 JSON file to its v2 equivalent and documents remaining gaps. |
| `PHASE_1_IMPLEMENTATION.md` | Detailed notes on what was built during Phase 1 (schema normalization, `$ref` resolution, core schema files). |
| `.gitignore` | Standard Python + build output ignores. |

---

### 4.2 `build_system/`

The Python build pipeline. All files here are imported as a package — never run directly except `core.py` (which also accepts CLI flags).

#### `build_system/config.py`
Defines all **path constants** used across the build:
- `BASE_DIR`, `CONTENT_DIR`, `ASSETS_DIR`, `TEMPLATES_DIR`, `DIST_DIR`
- `SETTINGS` dict with site title, base template filename, and paths to locales/modules
- Creates `dist/` if it does not exist

Anything that needs a path should import from here rather than hardcoding strings.

#### `build_system/core.py`
The **heart of the system** (~3000 lines). Contains a single class `AtlasBuilder` with these major responsibilities:

| Method group | What it does |
|---|---|
| `__init__` | Sets up all path references, initializes `site_registry`, warning list, and the renderer registry |
| `_build_renderer_registry()` | Returns a `dict[str, callable]` mapping every block `type` string to its render function |
| `_resolve_json_ref(ref)` | Resolves `@core/`, `@keywords/`, `@snippets/`, `@images/`, and `#/json/pointer` references |
| `_load_json(path)` | Reads and parses a JSON file with error handling |
| `_render_*()` methods | One method per block type — each receives a block dict and returns an HTML string |
| `_render_blocks()` | Recursive block container; calculates the correct heading level (`h2`–`h6`) based on nesting depth |
| `_render_dynamic()` | Renders `dynamic`/`lang_content` blocks — content that varies per selected language |
| `_render_keyword_grid()` | Renders a language-aware keyword comparison table |
| `scan_pages()` | Walks `content/pages/` and registers every `.json` file in `site_registry` with its mode (atlas/course/meta) |
| `build_navigation()` | Assembles sidebar HTML and prev/next paging from the registry |
| `generate_search_index()` | Extracts title/description/text from all pages and writes `dist/content/search-index.json` |
| `build()` | Orchestrates the entire pipeline in order |

The builder also accepts CLI flags via `argparse`:
- `--validate-only` — runs scan + schema validation, exits without writing to `dist/`
- `--watch` — starts a `watchdog` observer to re-run `build()` on file changes

#### `build_system/dead_link_checker.py`
Standalone validator that crawls all `.json` page files, extracts every HTTP/HTTPS URL (from both plain text and markdown `[text](url)` syntax), and HEAD-requests each one to check for broken links. Used by the `dead-links.yml` CI workflow.

Key class: `DeadLinkChecker`  
Key methods: `_extract_urls_from_text()`, `check_page()`, `run()`, `print_report()`

> ~~`build_system/core.py.broken`~~ — **OBSOLETE.** A broken backup snapshot of `core.py` created during a failed refactor. Safe to delete.

---

### 4.3 `content/`

All source content. Nothing here is served directly — everything is processed by the build system.

#### `content/pages/`

The **main content tree.** 126 JSON files organised into three subdirectories that map directly to the three app modes.

```
content/pages/
├── index.json              Home page (the root / of the app)
├── atlas/
│   ├── index.json          Atlas mode landing page
│   ├── design_patterns.json
│   ├── principles.json
│   ├── workflow.json
│   ├── keywords.json       Keyword index (links to per-language pages)
│   └── keywords/
│       ├── index.json
│       └── cpp.json        (only C++ keyword page exists so far)
├── course/
│   ├── index.json          Course mode landing page
│   ├── basics.json         Language basics (placeholder level)
│   ├── problems.json       Problems section (placeholder level)
│   ├── exercises.json
│   └── interview/
│       ├── 1_strings_and_arrays/
│       ├── 2_linked_list/
│       ├── 3_stacks_and_queues/
│       ├── 4_trees_and_graphs/
│       ├── 5_bit_manipulation/
│       ├── 8_recursion_dynamic_programming/
│       ├── 10_sorting_and_searching/
│       ├── 16_moderate/
│       └── 17_hard/
└── meta/
    ├── index.json
    ├── getting_started.json
    ├── content_types.json   Documents every supported block type
    ├── blocks_nesting.json  Demonstrates nested blocks
    ├── customization.json
    ├── external_links_test.json
    ├── insights_test.json
    └── showcases/
```

> `content/pages/course/exercieses.json` has already been renamed to `exercises.json` and references were updated.
>
> `content/pages/course/exercieses.json.bak` was deleted during cleanup.
>
> Interview content currently uses `8_recursion_dynamic_programming/` as the canonical folder.

#### `content/schemas/`

| File | Purpose |
|---|---|
| `page_schema.json` | JSON Schema (draft-07) for every page file. Defines required fields (`title`), optional fields (`description`, `category`, `template`, `body_class`, `extra_assets`, `style`, `schema_version`, `code_defaults`), and the `content` array structure. Used by `AtlasBuilder` when `jsonschema` is installed. |

#### `content/core/`

Shared JSON fragments referenced by pages via `"$ref": "@core/<name>"`.

| File | Purpose |
|---|---|
| `base_block.json` | JSON Schema for a single content block. Defines the `id`, `title`, `type`, `content`, `style`, `is_collapsible`, and `$ref` fields. All block renderers are expected to accept objects matching this schema. |
| `page_base.json` | Root page schema — the authoritative definition used by `page_schema.json`. |
| `language_icons.json` | Single source of truth for per-language icon SVG paths. Pages pull this in via `$ref` instead of duplicating it. |

#### `content/definitions/`

| File | Purpose |
|---|---|
| `languages.json` | **Master language registry.** Object keyed by language ID (`cpp`, `go`, `python`, `typescript`, `scala2`, `scala3`). Each entry contains `name`, `color`, `icon` path, file `extension`, `prism_class` for syntax highlighting, `tagline`, and `paradigm` tags. Read by the builder to know which languages exist and by the JS selection engine to populate the language picker. |
| `keywords/` | Per-language keyword definition files (`cpp.json`, `go.json`, `python.json`, `typescript.json`, `scala2.json`, `scala3.json`). Each maps keyword names to definitions and language-specific notes. Consumed by `_render_keyword_grid()`. |
| `schema/` | Additional JSON schemas for definitions (supplementary, not the primary validation path). |
| `possible_future_language_options.txt` | Removed during cleanup (it was an obsolete planning note superseded by `languages.json`). |

#### `content/keywords/`

Per-language keyword data in JSON format, mirroring `content/definitions/keywords/`. These are the files actually read at build time via `@keywords/<lang>` references.

| File | What it contains |
|---|---|
| `cpp.json` | C++ keywords with descriptions |
| `go.json` | Go keywords |
| `python.json` | Python keywords |
| `typescript.json` | TypeScript keywords |
| `scala2.json` | Scala 2 keywords |
| `scala3.json` | Scala 3 keywords |
| `designs/` | Keyword sets scoped to design-pattern vocabulary (in progress) |

#### `content/snippets/`

Raw source code files organised by language then category. The builder scans this tree and generates multi-language comparison grids.

```
content/snippets/
├── cpp/
│   ├── language_basics/
│   ├── design_patterns/
│   ├── problems/
│   ├── interview_lcci/
│   ├── exercises/
│   └── rename_map.csv    ← migration mapping, safe to delete after migration
├── go/       (same structure)
├── python/   (same structure)
├── typescript/
├── scala2/
└── scala3/
```

Each file is a plain source code file (`.cpp`, `.go`, `.py`, `.ts`, `.scala`). File names are used as the comparison key — files with the same name across languages are grouped into a side-by-side comparison block.

#### `content/modules/`

Reusable **HTML fragment templates** used during the build to scaffold comparison sections. These are not full pages — the builder pastes them into generated pages and then substitutes `[[COMPARE:category]]` placeholders with the actual snippet grid.

| File | Purpose |
|---|---|
| `comparison.html` | Template for a `<section class="comparison-section">` with a `[[COMPARE:syntax_basics]]` placeholder. |
| `hero.html` | Hero/banner section template. |
| `atlas-grid.html` | Layout skeleton for the Atlas side-by-side grid view. |
| `syntax_overview.html` | Template for a syntax overview section. |

> These files may be partially superseded by inline rendering in `core.py`. Review which are still referenced before modifying.

#### `content/locales/`

Locale stub files were removed during cleanup. i18n is currently not implemented, and UI strings are hardcoded in templates and JS.

---

### 4.4 `assets/`

Static frontend resources. Copied verbatim to `dist/assets/` by the builder.

#### `assets/css/`

All styling is written in plain CSS using custom properties (CSS variables). No preprocessor.

| File | Purpose |
|---|---|
| `main.css` | **Core styles.** Defines the palette system (`--accent` per `data-palette`), theme tokens (`--bg`, `--panel`, `--border`, `--text`), the three geometric design modes (Sharp / Round / Airy via `data-global-style`), layout grid, sidebar, and navigation. |
| `ui_states.css` | Styles for interactive states: active/hover on nav items, collapsed blocks, hash-target flash animation, permalink icon visibility. |
| `accessible.css` | Accessibility overrides: focus rings, reduced-motion media query, screen-reader utilities. |
| `ide.css` | Code block presentation styles: line numbers, copy button, diff highlighting, line-range highlight. |
| `gallery.css` | Grid layout for language selection gallery / comparison card grid. |
| `meta.css` | Styles specific to Meta mode pages (documentation showcase). |
| `reference.css` | Styles for Atlas mode reference pages (keyword tables, principle cards). |
| `tutorial.css` | Styles for Course mode tutorial pages (step indicators, exercise panels). |
| `playground.css` | Styles for potential future interactive playground pages. |

**`assets/css/themes/`** — One file per theme, each overriding the CSS variables set in `main.css`.

| File | Theme |
|---|---|
| `dark.css` | Dark theme (default) |
| `light.css` | Light theme |
| `high-contrast.css` | High-contrast accessibility theme |

**`assets/css/modules/`** — Component-level CSS modules (loaded per-page via `extra_assets` in page JSON).

#### `assets/js/`

Vanilla JavaScript — no build step, no frameworks, no bundler. All files are included in every page via `<script>` tags in `templates/base.html`.

| File | Responsibility |
|---|---|
| `app.js` | **General UI controller.** Theme cycling (Dark→Light→High-Contrast), palette picker, Global Design Style (Sharp/Round/Airy), sidebar open/close, view-mode toggle (Show All / Primary Only / Compare), scroll-spy for active nav highlighting, and mode-specific last-page persistence in `localStorage`. |
| `selection_engine.js` | **Language picker logic.** Manages the `AtlasState` object (`viewMode`, `primaryLang`, `secondaryLang`). Handles left-click (set primary), right-click (set secondary), drag selection, and `data-lang-*` CSS class toggling that shows/hides language columns. Persists state to `localStorage` for zero-flicker reload. |
| `polyglot_filter.js` | **Multi-select language filter.** Allows hiding specific language columns in comparison grids (independent of the primary/secondary selection). Saves selected set to `localStorage` under key `atlas-filter-langs`. |
| `search_ui.js` | **Client-side search.** Loads `dist/content/search-index.json` lazily on first focus, filters results by title/description/text, and renders a dropdown of matching pages with links. |
| `content_renderers.js` | **Phase 2 runtime helpers.** Adds behaviour to server-rendered blocks: sheet transpose toggle (swap rows/columns), line-range highlighting in code blocks, diff-mode visual presentation, and fragment vertical alignment across visible language columns. |
| `permalinks.js` | **Permalink UX.** Attaches click handlers to `<a class="permalink">` anchors so clicking copies the full absolute URL to clipboard. Also handles hash-target flash animation on page load and `hashchange`. |
| `service_worker.js` | **PWA offline cache.** Caches critical assets on install (CSS, JS, HLJS themes). Uses cache-first for static assets and network-first for content JSON. Cache version: `atlas-v1`. |

#### `assets/hljs/`

Bundled [Highlight.js](https://highlightjs.org/) distribution for syntax highlighting in code blocks. Includes language packs and two themes:
- `atom-one-dark.min.css` (used in dark and high-contrast mode)
- `github.min.css` (used in light mode)

#### `assets/icons/`

SVG icons for each supported language. Named by language ID: `cpp.svg`, `go.svg`, `python.svg`, `typescript.svg`, `scala.svg`.

#### `assets/manifest.json`

Web App Manifest enabling PWA installation. Defines app name, `start_url`, `display: standalone`, theme color (`#09090b`), and inline SVG icons (no external image dependencies). Categories: productivity, education.

---

### 4.5 `templates/`

#### `templates/base.html`

The **single HTML template** for all pages. The builder performs string substitution on `{{ title }}`, `{{ asset_prefix }}`, `{{ sidebar_html }}`, `{{ content_html }}`, and other template variables.

Key structural elements:
- **Anti-flash script** (inline, blocking): reads `localStorage` and sets `data-theme`, `data-palette`, `data-global-style`, `data-selection-mode`, `data-primary`, `data-secondary` on `<html>` before first paint.
- `<link id="theme-css">` for the active theme stylesheet (swapped by `app.js`)
- `<link id="hljs-theme">` for the active HLJS theme
- `<nav class="sidebar">` (populated by `{{ sidebar_html }}`)
- `<main class="content-area">` (populated by `{{ content_html }}`)
- All JS files included at end of `<body>`

---

### 4.6 `scripts/`

One-time **migration helper scripts** used during the v1→v2 migration. These are no longer needed for routine development. Keep in version control for historical reference but do not rely on them.

| File | What it did |
|---|---|
| `migrate_snippets.py` | Migrated v1 code snippets to the new folder structure |
| `generate_interview_pages_from_legacy.py` | Scaffolded the 100+ interview chapter JSON pages from legacy content |
| `normalize_exercises_structure.py` | Normalised exercise JSON to the v2 block schema |
| `restructure_exercises.py` | Restructured exercise file organisation |
| `fix_exercises_json_paths.py` | Fixed snippet `$ref` paths in exercise pages after folder renames |
| `auto_fix_exercises_json_paths.py` | Automated version of the above |
| `apply_group_difficulty_to_exercises_json.py` | Added `difficulty` metadata to exercise blocks |
| `cleanup_remove_duplicate_code_defaults.py` | Removed duplicated `code_defaults` entries introduced by earlier migration steps |
| `move_intermediate_to_advanced.py` | Reclassified some exercise difficulty levels |
| `update_design_patterns_paths.py` | Updated snippet paths in design patterns pages after snippet reorganisation |

> Most of these are one-time helpers and can be removed after final audit/cleanup.

---

### 4.7 `tools/`

| File | Purpose |
|---|---|
| `copy_typescript_snippets.ps1` | PowerShell script that copies TypeScript snippet files from one location to another. One-time helper used during snippet migration. Safe to delete after verifying TypeScript snippet coverage. |

---

### 4.8 `.github/workflows/`

Three GitHub Actions workflows — see `CI_CD_GUIDE.md` for full documentation.

| File | Trigger | Purpose |
|---|---|---|
| `build.yml` | Push to main/develop, PRs | Full build + schema validation + dead link check + deploy to GitHub Pages |
| `dead-links.yml` | Daily 2AM UTC, manual | Checks all external URLs; opens a GitHub issue if broken links are found |
| `validate-pr.yml` | PR opened/updated | Validates JSON schema of changed content files only (faster than full build) |

---

### 4.9 `dist/`

**Build output — do not edit manually.** Regenerated on every `python build.py` run.

```
dist/
├── index.html              Home page
├── atlas/                  One .html per atlas page
├── course/                 One .html per course page (110+ files)
├── meta/                   One .html per meta page
├── content/
│   └── search-index.json   Full-text search index (generated at build time)
└── assets/                 Copied from assets/
```

The `dist/` directory is committed to the repository (GitHub Pages deployment reads from it). The `build.yml` CI workflow also uploads it as an artifact.

---

### 4.10 Obsolete / Dead files

The following files are no longer part of the active development workflow. They are either v1 artifacts, one-time migration helpers, or broken backups.

| File / Directory | Reason | Recommended action |
|---|---|---|
| ~~`legacy_build.py`~~ | Original v1 builder; completely replaced by `build_system/core.py` | **Deleted** |
| ~~`legacy_index.html`~~ | v1 bundled single-file output; superseded by `dist/` | **Deleted** |
| ~~`legacy_content/`~~ | 500+ v1-format content files; some still referenced as migration source, rest are dead | **Archive** (zip and remove from working tree once migration reaches 100%) |
| ~~`debug_mockup.html`~~ | HTML mockup used to prototype UI layout | **Deleted** |
| ~~`index_mock.html`~~ | Another UI prototype mockup | **Deleted** |
| ~~`build_system/core.py.broken`~~ | Broken backup created during a failed refactor | **Deleted** |
| ~~`content/pages/course/exercieses.json`~~ | Misspelled filename (`exercieses` vs `exercises`) | **Renamed** to `exercises.json` |
| ~~`content/pages/course/exercieses.json.bak`~~ | Backup of the misspelled file | **Deleted** |
| ~~`content/definitions/possible_future_language_options.txt`~~ | Plain-text brainstorm note; superseded by `languages.json` and the roadmap | **Deleted** |
| ~~`content/locales/en.json`~~ | Empty i18n stub | **Deleted** |
| ~~`content/locales/hu.json`~~ | Empty i18n stub | **Deleted** |
| ~~`content/snippets/cpp/rename_map.csv`~~ | Migration mapping file; no longer needed once snippets are settled | **Delete** |
| ~~`scripts/*.py`~~ (all 10 files) | One-time migration helpers | **Delete** after final audit |
| ~~`scripts/copy_typescript_snippets.ps1`~~ | One-time snippet copy script moved from `tools/` into the audit bucket | **Delete** after final script audit |
| ~~`tmp/LAYOUT.md`~~ | Temporary layout planning note | **Delete** |

---

## 5. Content System Deep Dive

### 5.1 Page JSON format

Every page is a JSON file under `content/pages/`. Minimal valid page:

```json
{
  "title": "My Page",
  "content": []
}
```

Full set of top-level fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | string | ✅ | Browser tab title and search index entry |
| `description` | string | | SEO description, also indexed for search |
| `schema_version` | string | | Set to `"2.0"` for v2 pages |
| `category` | string | | Sidebar grouping label |
| `template` | string | | HTML template file (defaults to `base.html`) |
| `body_class` | string | | Extra CSS classes on `<body>` |
| `extra_assets` | string[] | | Additional CSS/JS to include on this page |
| `style` | string | | Page-level style preset |
| `code_defaults` | object | | Default language/theme for code blocks on this page |
| `content` | array | | Array of block objects |

### 5.2 Block types

The builder's renderer registry maps `type` strings to render functions. All supported types:

| Type | Renders as | Notes |
|---|---|---|
| `title` | `<h1>` with page-title styling | Use once per page at the top |
| `h1`–`h6` | `<h1>`–`<h6>` | Nesting depth inside `blocks` auto-adjusts the actual tag level |
| `text` | `<p>` | Supports inline markdown (bold, italic, `code`, links) |
| `note` | Styled callout box | For warnings, tips, important notices |
| `insight` | Highlighted insight card | For pro-tips and key takeaways |
| `link` | `<a>` | Explicit link block |
| `code` | Syntax-highlighted `<pre><code>` | Supports `language`, `lines` (range), `diff` fields |
| `image` | `<img>` | Supports `@images/` refs (base64-inlined) |
| `list` | `<ul>` or `<ol>` | Nested lists supported |
| `blocks` | `<section>` container | **Recursive.** Each nested `blocks` becomes a collapsible section. |
| `table` / `sheet` / `matrix` | `<table>` | 2D data. The `content_renderers.js` adds a Transpose toggle at runtime. |
| `dynamic` / `lang_content` | Per-language variants | Content that changes based on the selected language |
| `keyword_grid` | Comparison table | Renders keyword definitions side-by-side across languages |

### 5.3 `$ref` resolution

Any field in a block can be a `$ref` pointer instead of inline data. The builder resolves these at build time:

| Prefix | Resolves to |
|---|---|
| `@core/<name>` | `content/core/<name>.json` |
| `@keywords/<lang>` | `content/keywords/<lang>.json` |
| `@snippets/<path>` | Raw text content of `content/snippets/<path>` |
| `@images/<name>` | Base64-encoded content of `assets/images/<name>` |
| `#/json/pointer` | JSON Pointer into the same page document |

### 5.4 Code snippets

Snippets live in `content/snippets/<lang>/<category>/<filename>.<ext>`.  
The builder groups files **by name across languages** to produce comparison columns. For example:

```
content/snippets/
  cpp/language_basics/variables.cpp
  go/language_basics/variables.go
  python/language_basics/variables.py
  typescript/language_basics/variables.ts
```

These four files produce a single four-column comparison block titled "variables".

---

## 6. Build System Deep Dive

The build runs in this order inside `AtlasBuilder.build()`:

1. **Clean** `dist/` (selective — preserves `.git` if present)
2. **Copy assets** from `assets/` to `dist/assets/`
3. **Scan pages** — walks `content/pages/`, builds `site_registry` mapping each page JSON to its output HTML path and navigation position
4. **For each page:**
   a. Load and validate JSON against `content/schemas/page_schema.json`
   b. Resolve all `$ref` pointers recursively
   c. Render each block in the `content` array to HTML
   d. Build sidebar HTML (highlighting the current page)
   e. Build breadcrumbs and prev/next links
   f. Substitute all variables into `templates/base.html`
   g. Write the resulting HTML to `dist/<mode>/<page>.html`
5. **Generate search index** — writes `dist/content/search-index.json`
6. **Validate internal links** — checks all `href` and `src` in generated HTML resolve to a file in `dist/`
7. **Print summary** — page count, warning count, any validation errors

---

## 7. Frontend Architecture

The app is a **single-page-style experience built from static HTML**. There is no client-side routing — each page is a full HTML document. JavaScript only adds:

- Persistent state (theme, language selection) via `localStorage`
- DOM class toggling to show/hide language columns (`data-lang-*` attributes)
- Client-side search against the pre-built `search-index.json`
- Minor UX enhancements (permalinks, sheet transpose, scroll-spy)

**Zero external runtime dependencies.** Highlight.js and all CSS are bundled under `assets/`.

**PWA support** via `service_worker.js` and `assets/manifest.json`. The app is installable and works offline after first load.

**Theme system:** `data-theme` on `<html>` drives CSS variable values via attribute selectors in `main.css` + `themes/*.css`. Switching themes updates the attribute and swaps the `<link id="theme-css">` href — no page reload needed.

---

## 8. CI/CD

See `CI_CD_GUIDE.md` for full documentation. Summary:

| Workflow | When | What |
|---|---|---|
| `build.yml` | Push/PR to main/develop | Build, validate, dead-link check, deploy to GitHub Pages |
| `dead-links.yml` | Daily + manual | Check all external URLs |
| `validate-pr.yml` | PR | Fast JSON schema validation of changed files |

---

## 9. Migration Status

As of 2026-04-22, interview migration for the currently present chapter folders is largely complete.

**Completed:**
- Core cleanup pass: legacy root files removed, misnamed exercises page renamed, empty locale stubs removed
- Interview chapter content migration completed for: `1`, `2`, `3`, `4`, `5`, `8`, `10`, `16`, `17`
- Most interview pages now use `Example Output` positioned after `Code Example`
- Core build infrastructure (schema, `$ref` resolution, renderer registry, search index, CI/CD)

**Remaining migration/content tasks:**
- `course/basics.json` and `course/problems.json` are still high-level placeholders

See `MIGRATION_COVERAGE_PLAN.md` for broader gap tracking.

---

## 10. Known Issues & Next Steps

| Issue | File(s) | Action |
|---|---|---|
| Remaining one-time migration helpers | `scripts/` | Delete after final audit |

