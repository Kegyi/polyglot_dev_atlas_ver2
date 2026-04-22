# Polyglot Dev Atlas — v2

A multi-language developer reference tool enabling **side-by-side code comparison** across C++, Go, Python, TypeScript, Scala 2, and Scala 3.  
The app is a **static site** (no server needed): a Python build pipeline reads JSON content and code snippets, then renders everything into plain HTML/CSS/JS under `dist/`.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Architecture at a Glance](#2-architecture-at-a-glance)
3. [Installation & Usage (Production)](#3-installation--usage-production)
4. [Getting Started (Development)](#4-getting-started-development)
5. [File & Directory Reference](#5-file--directory-reference)
   - [Root files](#51-root-files)
   - [build_system/](#52-build_system)
   - [content/](#53-content)
   - [assets/](#54-assets)
   - [templates/](#55-templates)
   - [scripts/](#56-scripts)
   - [.github/workflows/](#57-githubworkflows)
   - [dist/](#58-dist)
6. [Content System Deep Dive](#6-content-system-deep-dive)
   - [Page JSON format](#61-page-json-format)
   - [Block types](#62-block-types)
   - [$ref resolution](#63-ref-resolution)
   - [Code snippets](#64-code-snippets)
7. [Build System Deep Dive](#7-build-system-deep-dive)
8. [Frontend Architecture](#8-frontend-architecture)
9. [CI/CD](#9-cicd)
10. [Known Issues & Next Steps](#10-known-issues--next-steps)

---

## 1. Project Overview

The Atlas has **three modes**, each served as a section of the same static site:

| Mode | URL prefix | Purpose |
|------|------------|---------|
| **Atlas** | `/atlas/` | Quick-reference: design patterns, principles, workflow, keyword grids |
| **Course** | `/course/` | Learning curriculum: language basics (5 chapters), problems, interview prep (9 chapter groups), exercises |
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
    │  • assemble navigation / breadcrumbs / pager
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

## 3. Installation & Usage (Production)

This section is for people who want to **use** the app (not develop it).

### Option A — Use prebuilt output locally (PC / tablet)

1. Download a packaged build that contains the `dist/` folder.
2. Extract it anywhere on your device.
3. Open `dist/index.html` in a browser.

Windows:
```bash
start dist/index.html
```

macOS / Linux:
```bash
open dist/index.html
```

This works fully offline after files are present.

### Option B — Use as installed PWA (PC / tablet / phone)

Host `dist/` on any static hosting (for example GitHub Pages). Then open the hosted URL and install:
- Chrome / Edge (desktop or Android): use the install icon in the address bar/menu
- Safari on iPhone/iPad: Share -> Add to Home Screen

After install, Atlas opens like an app and can be used offline after first load.

### Device guidance

- PC/Laptop: best experience for side-by-side code comparison
- Tablet: good usability, especially in landscape mode
- Phone: usable for reading, but multi-column code comparison is limited by screen width

For phones, landscape orientation is recommended when viewing code-heavy pages.

---

## 4. Getting Started (Development)

```bash
# Full build
python build.py

# Validate content without producing output
python build_system/core.py --validate-only

# Auto-rebuild on file changes (requires watchdog)
python build_system/core.py --watch
```

**Editing content:** all page content lives in `content/pages/` as JSON files. After any edit, re-run `python build.py` and refresh the browser.

**Editing styles or JS:** edit files under `assets/css/` or `assets/js/`. Run the build to copy them to `dist/assets/`.

---

## 5. File & Directory Reference

### 5.1 Root files

| File | Purpose |
|------|---------|
| `build.py` | **Main entry point.** Imports `AtlasBuilder` from `build_system/core.py` and calls `builder.build()`. Handles top-level error reporting and prints a success summary. |
| `requirements.txt` | Two optional Python dependencies: `jsonschema>=4.0.0` and `watchdog>=2.0.0`. |
| `CI_CD_GUIDE.md` | Documents all GitHub Actions workflows and how to trigger them manually. |
| `README.md` | Project documentation (this file). |
| `.gitignore` | Standard Python + build output ignores. |

---

### 5.2 `build_system/`

The Python build pipeline. All files here are imported as a package.

#### `build_system/config.py`
Defines all **path constants** used across the build:
- `BASE_DIR`, `CONTENT_DIR`, `ASSETS_DIR`, `TEMPLATES_DIR`, `DIST_DIR`
- `SETTINGS` dict with site title, base template filename, and paths to locales/modules

#### `build_system/core.py`
The **heart of the system** (~3 000 lines). Contains a single class `AtlasBuilder`:

| Method group | What it does |
|---|---|
| `__init__` | Sets up path references, initializes `site_registry`, warning list, and the renderer registry |
| `_build_renderer_registry()` | Returns a `dict[str, callable]` mapping every block `type` string to its render function |
| `_resolve_json_ref(ref)` | Resolves `@core/`, `@keywords/`, `@snippets/`, `@images/`, and `#/json/pointer` references |
| `_render_*()` methods | One method per block type — each receives a block dict and returns an HTML string |
| `_render_blocks()` | Recursive block container; calculates heading level (`h2`–`h6`) based on nesting depth |
| `_render_dynamic()` | Renders `dynamic`/`lang_content` blocks — content that varies per selected language |
| `_render_keyword_grid()` | Renders a language-aware keyword comparison table |
| `scan_pages()` | Walks `content/pages/` and registers every `.json` file in `site_registry` |
| `assemble_navigation()` | Assembles sidebar HTML from the registry; folder-local for nested sections |
| `assemble_prev_next()` | Builds prev/next pager; stays within submenu folders for nested pages |
| `generate_search_index()` | Extracts title/description/text and writes `dist/content/search-index.json` |
| `build()` | Orchestrates the entire pipeline in order |

CLI flags via `argparse`:
- `--validate-only` — runs scan + schema validation, exits without writing to `dist/`
- `--watch` — starts a `watchdog` observer to re-run `build()` on file changes

#### `build_system/dead_link_checker.py`
Standalone validator that crawls all `.json` page files, extracts every HTTP/HTTPS URL, and HEAD-requests each one to check for broken links. Used by the `dead-links.yml` CI workflow.

---

### 5.3 `content/`

All source content. Nothing here is served directly — everything is processed by the build system.

#### `content/pages/`

The **main content tree.** JSON files organised into three subdirectories mapping to the three app modes.

```
content/pages/
├── index.json                  Home page
├── atlas/
│   ├── index.json              Atlas mode landing page
│   ├── design_patterns.json
│   ├── principles.json
│   ├── workflow.json
│   └── keywords.json           Dynamic keyword page (language-aware)
├── course/
│   ├── index.json              Course mode landing page
│   ├── basics.json             Language basics landing (links to 5 sub-chapters)
│   ├── basics/
│   │   ├── index.json
│   │   ├── foundations_and_flow.json
│   │   ├── types_and_modeling.json
│   │   ├── data_structures.json
│   │   ├── systems_and_io.json
│   │   └── problem_solving_and_reliability.json
│   ├── problems.json           Cross-language problem set (7 problems)
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
    ├── content_types.json
    ├── blocks_nesting.json
    ├── customization.json
    ├── external_links_test.json
    ├── insights_test.json
    └── showcases/
```

#### `content/schemas/`

| File | Purpose |
|---|---|
| `page_schema.json` | JSON Schema (draft-07) for every page file. Used by `AtlasBuilder` when `jsonschema` is installed. |

#### `content/core/`

Shared JSON fragments referenced by pages via `"$ref": "@core/<name>"`.

| File | Purpose |
|---|---|
| `base_block.json` | JSON Schema for a single content block |
| `page_base.json` | Root page schema |
| `language_icons.json` | Per-language icon SVG paths |

#### `content/definitions/`

| File | Purpose |
|---|---|
| `languages.json` | **Master language registry.** Each entry has `name`, `color`, `icon`, `extension`, `prism_class`, `tagline`, and `paradigm`. Read by builder and JS selection engine. |

#### `content/keywords/`

Per-language keyword data read at build time via `@keywords/<lang>` references.

| File | Contents |
|---|---|
| `cpp.json` | C++ keywords with descriptions |
| `go.json` | Go keywords |
| `python.json` | Python keywords |
| `typescript.json` | TypeScript keywords |
| `scala2.json` | Scala 2 keywords |
| `scala3.json` | Scala 3 keywords |

#### `content/snippets/`

Raw source code files organised by language then category.

```
content/snippets/
├── cpp/
│   ├── language_basics/    26 topics
│   ├── design_patterns/
│   ├── problems/           7 cross-language problems
│   ├── interview_lcci/
│   └── exercises/
├── go/        (same structure)
├── python/    (same structure)
├── typescript/
├── scala2/
└── scala3/
```

Files with the same name across languages are grouped into a side-by-side comparison block.

#### `content/modules/`

Reusable HTML fragment templates used during the build for comparison section scaffolding. May be partially superseded by inline rendering in `core.py`.

---

### 5.4 `assets/`

Static frontend resources. Copied verbatim to `dist/assets/` by the builder.

#### `assets/css/`

All styling is plain CSS using custom properties. No preprocessor.

| File | Purpose |
|---|---|
| `main.css` | Core styles: palette system, theme tokens, geometric design modes (Sharp/Round/Airy), layout grid, sidebar, navigation |
| `ui_states.css` | Interactive states: view-mode control, swap button, active/hover nav, collapsed blocks |
| `accessible.css` | Accessibility overrides: focus rings, reduced-motion, screen-reader utilities |
| `ide.css` | Code block presentation: line numbers, copy button, diff highlighting |
| `gallery.css` | Grid layout for language comparison cards |
| `meta.css` | Meta mode page styles |
| `reference.css` | Atlas mode reference styles (keyword tables, principle cards) |
| `tutorial.css` | Course mode styles (step indicators, exercise panels) |
| `playground.css` | Future interactive playground styles |

**`assets/css/themes/`**

| File | Theme |
|---|---|
| `dark.css` | Dark theme (default) |
| `light.css` | Light theme |
| `high-contrast.css` | High-contrast accessibility theme |

Each theme defines `--on-accent` (text color on accent backgrounds) in addition to the standard color tokens.

**`assets/css/modules/`** — Component-level CSS modules: `variables.css`, `nav.css`, `sidebar.css`, `layout.css`, `components.css`, `content_blocks.css`, `insights.css`, `collections.css`.

#### `assets/js/`

Vanilla JavaScript — no build step, no frameworks.

| File | Responsibility |
|---|---|
| `app.js` | Theme cycling, palette picker, geometric style picker (dropdown), sidebar open/close, view-mode toggle, scroll-spy, mode-specific page persistence |
| `selection_engine.js` | Language picker: manages `AtlasState` (`viewMode`, `primaryLang`, `secondaryLang`), single/double toggle, swap button, drag-select, `localStorage` persistence |
| `polyglot_filter.js` | Multi-select language column filter independent of primary/secondary selection |
| `search_ui.js` | Client-side search against pre-built `search-index.json` |
| `content_renderers.js` | Runtime block enhancements: sheet transpose, line-range highlighting, diff mode |
| `permalinks.js` | Click-to-copy permalink anchors, hash-target flash |
| `service_worker.js` | PWA offline cache (cache-first for static assets, network-first for content) |

#### `assets/hljs/`

Bundled Highlight.js with `atom-one-dark.min.css` (dark/high-contrast) and `github.min.css` (light).

#### `assets/icons/`

SVG icons per language: `cpp.svg`, `go.svg`, `python.svg`, `typescript.svg`, `scala.svg`.

#### `assets/manifest.json`

Web App Manifest for PWA installation (standalone display, offline capable).

---

### 5.5 `templates/`

#### `templates/base.html`

The **single HTML template** for all pages. Builder substitutes `{{ title }}`, `{{ asset_prefix }}`, `{{ mode_switcher }}`, `{{ navigation_sidebar }}`, `{{ content }}`, `{{ breadcrumbs }}`, `{{ pager_nav }}`, and other placeholders.

Key structural elements:
- **Anti-flash script** (inline, blocking): reads `localStorage` and sets theme/palette/style/selection attributes on `<html>` before first paint
- `<link id="theme-css">` for active theme stylesheet (swapped by `app.js`)
- `<link id="hljs-theme">` for active HLJS theme
- Navbar with: logo + mode-switcher dropdown, single/double view control with inline swap, style picker dropdown, palette picker dropdown, theme toggle
- Left sidebar (navigation), main content area, right sidebar (topic TOC)

---

### 5.6 `scripts/`

The folder currently exists but is empty (all migration helper scripts were removed after migration cleanup).

---

### 5.7 `.github/workflows/`

Three GitHub Actions workflows — see `CI_CD_GUIDE.md` for full documentation.

| File | Trigger | Purpose |
|---|---|---|
| `build.yml` | Push to main/develop, PRs | Full build + schema validation + dead link check + deploy to GitHub Pages |
| `dead-links.yml` | Daily 2AM UTC, manual | Checks all external URLs; opens a GitHub issue if broken links are found |
| `validate-pr.yml` | PR opened/updated | Validates JSON schema of changed content files only |

---

### 5.8 `dist/`

**Build output — do not edit manually.** Regenerated on every `python build.py` run.

```
dist/
├── index.html              Home page
├── atlas/                  Atlas pages
├── course/                 Course pages (150+ files including interview chapters)
├── meta/                   Meta pages
├── content/
│   └── search-index.json   Full-text search index (generated at build time)
└── assets/                 Copied from assets/
```

---

## 6. Content System Deep Dive

### 6.1 Page JSON format

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
| `code_defaults` | object | | Default `display_name` and `is_collapse` for code blocks |
| `content` | array | | Array of block objects |

### 6.2 Block types

| Type | Renders as | Notes |
|---|---|---|
| `title` | `<h1>` | Use once per page at the top |
| `h1`–`h6` | `<h1>`–`<h6>` | Nesting inside `blocks` auto-adjusts the tag level |
| `text` | `<p>` | Supports inline markdown (bold, italic, `code`, links) |
| `note` | Styled callout box | For warnings, tips, important notices |
| `insight` | Highlighted insight card | For pro-tips and key takeaways |
| `link` | `<a>` | Explicit link block |
| `code` | Syntax-highlighted `<pre><code>` | Supports `language`, `path` (snippet), `lines` (range), `diff` |
| `image` | `<img>` | Supports `@images/` refs (base64-inlined) |
| `list` | `<ul>` or `<ol>` | Nested lists supported |
| `blocks` | `<section>` container | **Recursive.** Each nested `blocks` becomes a collapsible section. |
| `table` / `sheet` / `matrix` | `<table>` | 2D data. `content_renderers.js` adds a Transpose toggle at runtime. |
| `dynamic` / `lang_content` | Per-language variants | Content that changes based on selected language |
| `keyword_grid` | Keyword comparison table | Renders keyword definitions side-by-side across languages |

### 6.3 `$ref` resolution

| Prefix | Resolves to |
|---|---|
| `@core/<name>` | `content/core/<name>.json` |
| `@keywords/<lang>` | `content/keywords/<lang>.json` |
| `@snippets/<path>` | Raw text content of `content/snippets/<path>` |
| `@images/<name>` | Base64-encoded content of `assets/images/<name>` |
| `#/json/pointer` | JSON Pointer into the same page document |

### 6.4 Code snippets

Snippets live in `content/snippets/<lang>/<category>/<filename>.<ext>`.  
The builder groups files **by name across languages** to produce comparison columns. A code block references them with `"path": "<category>/<filename>"`.

Example — all four files below produce a single four-column block:
```
content/snippets/cpp/language_basics/variables.cpp
content/snippets/go/language_basics/variables.go
content/snippets/python/language_basics/variables.py
content/snippets/typescript/language_basics/variables.ts
```

---

## 7. Build System Deep Dive

The build runs in this order inside `AtlasBuilder.build()`:

1. **Clean** `dist/` (selective — preserves `.git` if present)
2. **Copy assets** from `assets/` to `dist/assets/`
3. **Scan pages** — walks `content/pages/`, builds `site_registry`
4. **For each page:**
   a. Load and validate JSON against `content/schemas/page_schema.json`
   b. Resolve all `$ref` pointers recursively
   c. Render each block in the `content` array to HTML
   d. Build sidebar HTML (highlighting the current page; folder-local for nested sections)
   e. Build breadcrumbs and folder-local prev/next pager links
   f. Substitute all variables into `templates/base.html`
   g. Write to `dist/<mode>/<page>.html`
5. **Generate search index** — writes `dist/content/search-index.json`
6. **Validate internal links** — checks all `href` and `src` in generated HTML
7. **Print summary** — page count, warning count, any errors

---

## 8. Frontend Architecture

The app is a **single-page-style experience built from static HTML**. There is no client-side routing — each page is a full HTML document. JavaScript only adds:

- Persistent state (theme, language selection) via `localStorage`
- DOM class toggling to show/hide language columns (`data-lang-*` attributes)
- Client-side search against the pre-built `search-index.json`
- Minor UX enhancements (permalinks, sheet transpose, scroll-spy)

**Zero external runtime dependencies.** Highlight.js and all CSS are bundled under `assets/`.

**PWA support** via `service_worker.js` and `assets/manifest.json`. The app is installable and works offline after first load.

**Theme system:** `data-theme` on `<html>` drives CSS variable values via attribute selectors in `main.css` + `themes/*.css`. Switching themes updates the attribute and swaps the `<link id="theme-css">` href — no page reload needed.

**Header controls:**
- Mode switcher: dropdown on the app title, links to each mode's index
- View toggle: merged Single/Double pill — click label to toggle, click `⇄` to swap languages in double mode
- Style picker: dropdown showing current geometric style icon (Sharp/Round/Airy)
- Palette picker: dropdown showing current accent color dot (9 palettes)
- Theme toggle: cycles Dark → Light → High-Contrast

---

## 9. CI/CD

See `CI_CD_GUIDE.md` for full documentation.

| Workflow | When | What |
|---|---|---|
| `build.yml` | Push/PR to main/develop | Build, validate, dead-link check, deploy to GitHub Pages |
| `dead-links.yml` | Daily + manual | Check all external URLs |
| `validate-pr.yml` | PR | Fast JSON schema validation of changed files |

---

## 10. Known Issues & Next Steps

| Issue | File(s) | Action |
|---|---|---|
| Missing `exercises/intermediate/*` snippets | `content/snippets/*/exercises/` | Author intermediate exercise snippets |
| Missing `example-setup` snippet | `content/pages/meta/getting_started.json` | Add snippet or remove the reference |

