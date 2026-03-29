# Improvements Roadmap

This document summarizes the recommended improvements for the Polyglot Dev Atlas, grouped into six strategic phases.

**Phase 1 — Schema Normalization & Modularity**
- **Blocks-Based Architecture:** Transition to a `Blocks` array in `page_schema.json`. Every block must inherit from a `base_block` (ID, title, optional `is_collapsible`).
- **Recursive `$ref` Resolution:** Update `build.py` to resolve JSON pointers. Shared definitions (e.g., standard language icons or common headers) should live in a `core/` folder.
- **External Asset Injection:** Support `@snippets/` or `@images/` aliases in JSON. The build script should read external file paths and inject raw text/base64 into the page JSON before rendering.
- **Schema Versioning:** Add a `schema_version` field to `page.json` to allow the build script to handle legacy formats gracefully as the project evolves.

**Phase 2 — Generic Component Rendering**
- **Flexible Sheet Renderer:** A JS helper for 2D arrays with a "Transpose" toggle (swap rows/columns) and automatic header-row detection.
- **Renderer Registry:** Map JSON `type` strings to JS functions. This allows pluggable support for `mermaid`, `mathjax`, or `interactive_demo`.
- **Advanced Code Block:** Add support for line-range highlighting and "diff" mode to visually emphasize syntax differences between compared languages.
- **Fragment Aligner:** Implement a vertical alignment tool that uses semantic metadata to keep related code steps (e.g., "Variable Declaration") aligned across side-by-side columns.

**Phase 3 — Automated Content Discovery & Integrity**
- **Auto-Scanning:** Remove manual `data.json` entries. `build.py` should scan `legacy_content/pages/` to auto-generate the site navigation and category hierarchy.
- **Strict Validation:** Use `jsonschema` to validate every `.page.json`. Include a build-time check for **Broken Internal Links** and **Missing Snippet Files**.
- **Breadcrumb Generation:** Automatically derive breadcrumbs and "Next/Previous" navigation based on the folder structure.

**Phase 4 — UX, Search & Interactivity**
- **Static Search Index:** Generate a `search-index.json` (titles, tags, excerpts) during build for instant client-side lookup.
- **Polyglot Filter:** Implement a client-side "Matrix Filter." Users can select specific languages (e.g., "Rust" and "Go") to hide columns/blocks irrelevant to their current comparison.
- **Permalinks:** Every block with an `id` should generate a hoverable anchor link for direct sharing of specific sections.
- **Mobile-First Comparison:** Add a "Card View" fallback for the Sheet Renderer to ensure tables remain readable on small screens.

**Phase 5 — Maintenance & Developer Workflow**
- **Hot Reloading:** Add a `--watch` mode to `build.py` (using `watchdog`) to rebuild the atlas instantly when local files change.
- **Theming Engine:** Move styles to SCSS/CSS variables. Enable theme switching (e.g., Light, Dark, High-Contrast) by injecting different CSS manifests during build.
- **Standardized Insight Blocks:** Create an `insight` block type (pro-tips, warnings, takeaways) with consistent iconography and styling.

**Phase 6 — Deployment & Quality Assurance**
- **Dead Link Checker:** A script to verify that external URLs in markdown/JSON are still active.
- **PWA Support:** Implement a basic Service Worker to allow the Atlas to be used offline—a critical feature for a developer reference tool.
- **CI/CD Integration:** Provide a `--lint` or `--validate-only` mode for use in GitHub Actions to prevent broken JSON from being merged.

---

## Strategic Recommendation

**Prioritize Phase 3 Validation:** 
Move the `jsonschema` validation and internal link checking to the top of your "to-do" list. As you transition to the `Blocks` architecture (Phase 1), the JSON files will become more complex. Having automated validation in place *during* the migration will prevent silent failures and hours of manual debugging in the JS renderers.

---

## Developer Trivia & Suggestions
*   **The "Polyglot" Metadata Challenge:** The hardest part of a comparison engine isn't the code, but the *metadata*. Consider adding `paradigm` tags (e.g., `functional`, `imperative`) to your blocks to allow for deeper search filtering.
*   **Lazy Rendering:** If you add heavy libraries like `Mermaid.js` or `MathJax`, implement a "Lazy Renderer" that only loads those scripts if the specific block type is detected on the page.
*   **Sync-Scroll:** For side-by-side code snippets, a "Sync-Scroll" feature (where scrolling the left pane moves the right pane) significantly improves the experience of comparing long files.
*   **Path Aliasing:** Using `@core/` or `@snippets/` instead of relative paths (`../../../`) in your JSON makes moving files much less painful during reorganization.

---
**Repository:** [https://github.com/Kegyi/polyglot_dev_atlas_ver2](https://github.com/Kegyi/polyglot_dev_atlas_ver2)