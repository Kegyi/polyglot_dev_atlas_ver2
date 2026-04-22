# Polyglot Dev Atlas v2 - Frontend Architecture Summary

## Overview
The polyglot_dev_atlas_ver2 is a **language-agnostic learning platform** that renders multi-language code examples and documentation with dynamic, side-by-side comparisons. The architecture separates **build-time** (Python) from **runtime** (JavaScript) to enable zero-flash rendering with client-side language selection.

---

## 1. File Structure & Key Directories

```
polyglot_dev_atlas_ver2/
├── content/                    # Source content (JSON-based pages)
│   ├── pages/                  # Page definitions by mode
│   │   ├── atlas/              # Atlas mode pages
│   │   │   └── playground_setup.json
│   │   ├── course/             # Course mode pages
│   │   └── meta/               # Meta documentation
│   ├── core/                   # Shared definitions
│   │   ├── languages.json      # Language metadata (names, colors)
│   │   ├── page_base.json      # Page schema
│   │   └── ...
│   ├── definitions/            # Language definitions
│   ├── snippets/               # Code snippets by language
│   ├── keywords/               # Keyword registries
│   └── modules/                # Reusable content modules
│
├── playground/                 # Language-specific setup guides (symlink targets)
│   ├── cpp/
│   │   ├── README.md           # C++ playground overview
│   │   ├── .setup/README.md    # Detailed setup guide
│   │   ├── threadpool/         # Example mini-project
│   │   └── linkage_demo/
│   ├── go/
│   ├── python/
│   ├── typescript/
│   └── scala/
│
├── dist/                       # Generated HTML output
│   ├── index.html              # Main entry (project mode)
│   ├── atlas/
│   │   ├── index.html          # Atlas home
│   │   ├── playground_setup.html  # Generated from JSON
│   │   ├── design_patterns.html
│   │   ├── keywords.html
│   │   └── ...
│   ├── course/
│   ├── meta/
│   └── assets/
│       ├── css/
│       │   ├── main.css        # Layout & typography
│       │   ├── ui_states.css   # View modes & themes
│       │   ├── themes/         # dark.css, light.css, high-contrast.css
│       │   └── ...
│       └── js/
│           ├── app.js          # Main UI controller
│           ├── selection_engine.js  # Language selection & dynamic rendering
│           ├── content_renderers.js # Phase 2 render helpers (sheet transpose, etc.)
│           ├── polyglot_filter.js   # Code block filtering
│           ├── search_ui.js         # Search functionality
│           ├── permalinks.js        # URL navigation
│           └── service_worker.js    # PWA support
│
├── templates/
│   └── base.html               # Master template for all pages
│
├── build.py                    # Build entry point
├── build_system/
│   └── core.py                 # AtlasBuilder class (main renderer)
│
└── requirements.txt            # Python dependencies (jsonschema, watchdog)
```

### Markdown File Locations
- **Playground guides**: `playground/{language}/README.md`, `playground/{language}/.setup/README.md`
- **Legacy documentation**: `legacy_content/docs/` (migrated content)
- **Markdown links in JSON**: Referenced via `<a href="../playground/{lang}/README.md">` in content blocks

---

## 2. Frontend JavaScript Architecture

### Core Files & Their Roles

#### `selection_engine.js` - Language Selection & Dynamic Rendering ⭐
**Main Controller for "dynamic" content type**

```javascript
// State Management
const AtlasState = {
    viewMode: 'single' | 'double',    // Single or dual-language view
    primaryLang: string,               // Currently selected language
    secondaryLang: null | string,      // Comparison language (when double-mode)
    languages: ['cpp', 'go', 'python', 'typescript', 'scala2', 'scala3']
};

// Key Functions
initSelectionEngine()              // Initialize state from localStorage
handleSelection(langId, side)      // Handle language button clicks
setViewMode(mode)                  // Toggle single/double view
refreshDynamicLanguageContent()    // Render all dynamic blocks (key function!)
renderDynamicLanguageSlot(block, slotName, langId)  // Render single slot
findDynamicVariantTemplate(block, langId)  // Find template by language
```

**How it works:**
1. User clicks language button (left-click = primary, right-click = secondary)
2. `handleSelection()` updates `AtlasState`
3. `updateUI()` calls `refreshDynamicLanguageContent()`
4. For each `.dynamic-language-block`:
   - Find `<template data-dynamic-variant="{langId}">`
   - Clone its innerHTML into `.dynamic-language-slot-body`
   - Update slot name/color from button metadata

#### `app.js` - Global UI Controller
- **Theme toggling**: dark/light/high-contrast
- **Palette selection**: Zinc, Red, Orange, Yellow, Green, Ocean, Blue, Indigo, Violet
- **Geometric style**: Sharp, Round, Airy (Phase 3 feature)
- **Sidebar management**: Collapse/expand left & right sidebars
- **View mode control**: All vs Focused topic display
- **Scroll spy**: Auto-highlight sidebar items based on scroll position

#### `content_renderers.js` - Phase 2 Render Helpers
- **Sheet transpose**: Swap rows/columns in tables with toggle button
- **Code highlighting**: Line-range highlighting using `data-highlight-ranges` attribute
- **Diff mode**: Side-by-side diff visualization with `data-diff-mode="true"`
- **Fragment alignment**: Vertically align related code blocks using `data-fragment-key`

#### `polyglot_filter.js`
- Filter code blocks by tag/feature
- Multi-select filtering

#### `search_ui.js`
- Search across pages/sections
- Real-time results with keyboard shortcuts (/ or Ctrl+K)

---

## 3. How "dynamic" Content Type is Rendered

### JSON Schema (Backend Definition)
```json
{
  "type": "dynamic",
  "id": "playground-setup-by-language",
  "primary_label": "Selected language",
  "secondary_label": "Comparison language",
  "variants": {
    "cpp": [
      { "type": "h3", "text": "C++ Playground Setup" },
      { "type": "text", "text": "Read full guides: ..." },
      { "type": "list", "items": [...] }
    ],
    "go": [...]
    // ... more languages
  },
  "fallback": [
    { "type": "note", "variant": "info", "text": "No setup guidance yet" }
  ]
}
```

### Build-Time Rendering (Python: `build_system/core.py`)
```python
def _render_dynamic(self, item, depth=2, inherited_style="", context=None):
    variants = item.get("variants", {})  # Dict of {lang_id: [content_blocks]}
    
    # For each language variant:
    for lang_id, variant_content in variants.items():
        blocks = self._coerce_content_list(variant_content)
        rendered = self.render_content(blocks, ...)  # Recursive render
        templates.append(
            f'<template data-dynamic-variant="{lang_id}" 
                       data-lang-name="{lang_name}">
                {rendered}
            </template>'
        )
    
    # Build grid structure with empty slots
    return f'''
    <section id="{item_id}" class="dynamic-language-block">
        <div class="dynamic-language-grid">
            <article class="dynamic-language-slot" data-slot="primary">
                <header>...</header>
                <div class="dynamic-language-slot-body"></div>
            </article>
            <article class="dynamic-language-slot" data-slot="secondary" class="is-hidden">
                <header>...</header>
                <div class="dynamic-language-slot-body"></div>
            </article>
        </div>
        {templates.join()}
        {fallback_template}
    </section>
    '''
```

### HTML Output Example
From `dist/atlas/playground_setup.html`:
```html
<section id="playground-setup-by-language" class="dynamic-language-block"
         data-primary-label="Selected language"
         data-secondary-label="Comparison language">
  <div class="dynamic-language-grid">
    <article class="dynamic-language-slot" data-slot="primary">
      <header class="dynamic-language-slot-header">
        <span class="dynamic-language-slot-role">Selected language</span>
        <span class="dynamic-language-slot-name"></span>
      </header>
      <div class="dynamic-language-slot-body"></div>
    </article>
    <article class="dynamic-language-slot" data-slot="secondary" class="is-hidden">
      <header>...</header>
      <div class="dynamic-language-slot-body"></div>
    </article>
  </div>
  
  <!-- Templates with variant content (filled at runtime) -->
  <template data-dynamic-variant="cpp" data-lang-name="C++">
    <h3>C++ Playground Setup</h3>
    <p>Read full guides: ...</p>
    <ul>
      <li>Start with a CMake-first mini project layout...</li>
      ...
    </ul>
  </template>
  
  <template data-dynamic-variant="go" data-lang-name="Go">
    <h3>Go Playground Setup</h3>
    ...
  </template>
  
  <!-- Fallback for unsupported languages -->
  <template data-dynamic-fallback="true">
    <div class="note note-info">
      <div class="note-content">No setup guidance yet</div>
    </div>
  </template>
</section>
```

### Runtime Rendering (JavaScript)
```javascript
// When user selects language (e.g., clicks "Python" button)
handleSelection('python', 'left');  // Sets AtlasState.primaryLang = 'python'
updateUI();
refreshDynamicLanguageContent();

// Inside refreshDynamicLanguageContent:
function renderDynamicLanguageSlot(block, 'primary', 'python') {
    const slot = block.querySelector('[data-slot="primary"]');
    const variantTemplate = block.querySelector(
        'template[data-dynamic-variant="python"]'
    );
    
    if (variantTemplate) {
        slot.querySelector('.dynamic-language-slot-body').innerHTML = 
            variantTemplate.innerHTML;  // Clone template content
    }
    
    // Update language name & color
    slot.querySelector('.dynamic-language-slot-name').textContent = 'Python';
    slot.style.setProperty('--active-lang-color', '#3776AB');  // From button
}
```

### CSS Logic (Zero-Flash)
```css
/* Root attributes drive visibility via data attributes */
:root {
    --data-primary: 'python';           /* Set by selection_engine.js */
    --data-selection-mode: 'single';    /* Or 'double' */
}

/* Anti-Flash: Set early in blocking script in <head> */
<script>
    const primary = localStorage.getItem('atlas-primary-lang') || 'cpp';
    document.documentElement.setAttribute('data-primary', primary);
</script>

/* CSS uses these attributes for instant rendering without JavaScript */
.dynamic-language-slot[data-slot="primary"] {
    display: block;  /* Always visible */
}

.dynamic-language-slot[data-slot="secondary"] {
    display: none;  /* Hidden in single mode */
}

.dynamic-language-slot[data-slot="secondary"].is-hidden {
    display: none;
}

/* When in double-mode, show secondary */
:root[data-selection-mode="double"] .dynamic-language-slot[data-slot="secondary"]:not(.is-hidden) {
    display: block;
}
```

---

## 4. Language Definitions & Metadata

### Location: `content/definitions/languages.json`
```json
{
  "cpp": {
    "name": "C++",
    "color": "#00599C",
    "aliases": ["cpp", "c++", "cplusplus"]
  },
  "go": {
    "name": "Go",
    "color": "#00ADD8",
    "aliases": ["go", "golang"]
  },
  "python": {
    "name": "Python",
    "color": "#3776AB",
    "aliases": ["python", "py"]
  },
  "typescript": {
    "name": "TypeScript",
    "color": "#3178C6",
    "aliases": ["typescript", "ts"]
  },
  "scala2": {
    "name": "Scala 2",
    "color": "#DE3423",
    "aliases": ["scala2", "scala"]
  },
  "scala3": {
    "name": "Scala 3",
    "color": "#DE3423",
    "aliases": ["scala3"]
  }
}
```

### Used in:
- Language button generation (navbar)
- Dynamic slot name/color updates
- Language-aware snippet loading

---

## 5. Markdown File Locations & Integration

### Source Markdown Files
| Language | Path | Purpose |
|----------|------|---------|
| C++ | `playground/cpp/README.md` | Overview & mini-project guide |
| C++ | `playground/cpp/.setup/README.md` | Detailed tier-based setup (CMake, Conan, etc.) |
| Go | `playground/go/README.md` | Go-specific setup |
| Go | `playground/go/.setup/README.md` | Go modules & testing |
| Python | `playground/python/README.md` | Python environment setup |
| Python | `playground/python/.setup/README.md` | venv, pip, pytest |
| TypeScript | `playground/typescript/README.md` | Node.js & npm |
| TypeScript | `playground/typescript/.setup/README.md` | tsconfig & build tools |
| Scala | `playground/scala/README.md` | sbt-based setup |

### How They're Linked
**In JSON content blocks:**
```json
{
  "type": "text",
  "text": "Read full guides: <a href=\"../playground/cpp/README.md\" target=\"_blank\">cpp/README.md</a> and <a href=\"../playground/cpp/.setup/README.md\" target=\"_blank\">cpp/.setup/README.md</a>."
}
```

**In HTML output (playground_setup.html):**
```html
<p>
  Read full guides: 
  <a href="../playground/cpp/README.md" target="_blank">cpp/README.md</a> 
  and 
  <a href="../playground/cpp/.setup/README.md" target="_blank">cpp/.setup/README.md</a>
</p>
```

### Build-Time Handling
- Markdown files are **copied** from `playground/` to `dist/playground/` during build
- No parsing/rendering happens; they're served as-is (browser displays raw markdown or via GitHub's markdown viewer if open in GitHub)
- Links use relative paths: `../playground/{lang}/README.md`

---

## 6. Existing Rendering Libraries & Utilities

### No Explicit Markdown Parser
The project **does not** include a markdown-to-HTML parser in the frontend or backend.
- Python dependencies: only `jsonschema` and `watchdog`
- No `markdown`, `marked`, or `pandoc` dependencies

### Code Highlighting
**Library**: `highlight.js` (HLJS)
- Files: `assets/hljs/` (atom-one-dark.min.css, github.min.css)
- Usage: Applied to `<code>` blocks in content via `window.hljs.highlightElement(codeEl)`
- Themes switch with theme toggle (dark/light)

### Table Rendering
**Built-in**:
- `content_renderers.js` provides `sheet-transpose` toggle
- Tables use `data-label` attributes for mobile card view
- Matrix transposition via `transposeMatrix()` utility

### No Markdown Rendering Libraries Found
- Markdown files are **not embedded** in pages
- They're provided as external links for users to download/view separately
- This keeps the build lightweight and allows documentation to evolve independently

---

## 7. Key Rendering Patterns

### 1. Recursive Content Rendering
```python
def render_content(self, content_list, depth=2, inherited_style=""):
    html = ""
    for item in content_list:
        html += self.render_item(item, depth, inherited_style)
    return html

def render_item(self, item, depth, inherited_style):
    renderer = self.renderers.get(item['type'])
    if renderer:
        return renderer(item, depth, inherited_style)
    return '<!-- Unknown type -->'
```

### 2. Style Inheritance
Styles cascade through nested content:
```json
{
  "type": "blocks",
  "style": "text_style",
  "content": [
    {
      "type": "title",
      "text": "Cascades style: text_style"
    },
    {
      "type": "blocks",
      "style": "code_style",
      "content": [
        { "type": "code", "text": "Uses overridden: code_style" }
      ]
    }
  ]
}
```

### 3. Collapsible Blocks (Depth-Based Visibility)
```python
should_collapse = depth > 3  # Level 1 & 2 visible; Level 3+ collapsed

html = f'''
<div id="{block_id}" class="topic-section {collapsed_class}">
    <div class="topic-header" onclick="app.toggleTopic('{block_id}')">
        <h{h_tag}>{title}</h{h_tag}>
        <div class="arrow">^</div>
    </div>
    <div class="topic-body {body_class}">
        {self.render_content(content, depth+1, style)}
    </div>
</div>
'''
```

### 4. Code Comparison Grids
```json
{
  "type": "code_comparison",
  "snippets": [
    { "lang": "cpp", "code": "@snippets/cpp/design_patterns/factory.cpp" },
    { "lang": "python", "code": "@snippets/python/design_patterns/factory.py" }
  ]
}
```

---

## 8. Build Process

### Entry Point: `build.py`
```python
from build_system.core import AtlasBuilder

builder = AtlasBuilder()
builder.build()  # Main orchestration
```

### Build Steps (AtlasBuilder)
1. **Scan pages**: Walk `content/pages/` recursively
2. **Validate**: Sanity checks + optional jsonschema validation
3. **Register**: Build site registry (TOC, navigation)
4. **Process pages**: For each page JSON:
   - Load & validate
   - Render content recursively
   - Resolve $ref pointers
   - Assemble navigation/sidebar
   - Inject into template
5. **Output**: Write final HTML to `dist/`

### Key Methods
- `_scan_and_register_pages()`: Discover all pages
- `process_page()`: Render single page to HTML
- `render_content()`: Recursive content rendering
- `render_item()`: Delegate to specific renderer
- `_render_dynamic()`: Build language-variant blocks
- `assemble_language_selector()`: Build navbar buttons
- `assemble_navigation()`: Build sidebar nav
- `assemble_topic_sidebar()`: Build right-side TOC

---

## 9. State Persistence

### LocalStorage Keys (set by JavaScript)
```javascript
localStorage.setItem('atlas-theme', 'dark');              // or 'light', 'high-contrast'
localStorage.setItem('atlas-palette', 'zinc');           // or 'red', 'ocean', etc.
localStorage.setItem('atlas-selection-mode', 'single');  // or 'double'
localStorage.setItem('atlas-primary-lang', 'cpp');
localStorage.setItem('atlas-secondary-lang', 'python');
localStorage.setItem('atlas-view-mode', 'all');          // or 'focused'
localStorage.setItem('atlas-global-style', 'round');     // or 'sharp', 'airy'
localStorage.setItem('atlas-sidebar-density', 'high');   // or 'minimal'
```

### Anti-Flash Script (in `<head>`)
Runs **before** DOM renders to prevent theme/language flashes:
```javascript
const savedPrimary = localStorage.getItem('atlas-primary-lang') || 'cpp';
document.documentElement.setAttribute('data-primary', savedPrimary);
// CSS is ready to apply saved state immediately
```

---

## 10. CSS Architecture

### Main Stylesheets
- **main.css**: Typography, layout, components
- **ui_states.css**: View modes, sidebar states, visibility
- **themes/{dark,light,high-contrast}.css**: Theme-specific colors
- **assets/hljs/*.css**: Syntax highlighting themes

### Key CSS Patterns
```css
/* Zero-flicker: Root attributes set in blocking script */
:root[data-primary="python"] .dynamic-language-slot-name {
    color: var(--lang-python, #3776AB);
}

/* View mode toggle */
:root[data-selection-mode="double"] .dynamic-language-slot[data-slot="secondary"] {
    display: block;
}

/* Theme switching */
:root[data-theme="dark"] { --bg: #0f0f0f; --text: #f0f0f0; }
:root[data-theme="light"] { --bg: #ffffff; --text: #000000; }

/* Geometric styles (Phase 3) */
:root[data-global-style="sharp"] .card { border-radius: 0; }
:root[data-global-style="round"] .card { border-radius: 12px; }
:root[data-global-style="airy"] .card { border-radius: 24px; }
```

---

## Summary: Key Takeaways

| Aspect | Details |
|--------|---------|
| **Dynamic Rendering** | Template cloning at runtime based on language selection |
| **Build vs Runtime** | JSON → HTML templates at build; slot-filling at runtime |
| **Markdown** | External links; no embedded parser (keeps build lightweight) |
| **State** | LocalStorage + root attributes for zero-flash |
| **Highlighting** | highlight.js for code syntax |
| **Selection** | Single/double view; left-click primary, right-click secondary |
| **Styling** | CSS attribute selectors; theme/palette/style via data attributes |
| **Playground Guides** | Located in `playground/{lang}/`, linked from JSON content |
| **No External Deps** | Only jsonschema & watchdog for Python; no markdown/render libs |

---

## Next Steps for Enhancement

1. **Embedded Markdown Rendering**: Add `markdown-it` or `marked.js` to render playground guides inline
2. **Server-Side Rendering (SSR)**: Pre-render common language combinations
3. **Search**: Extend search to include playground guide content
4. **Syntax Themes**: Add more HLJS themes
5. **Code Comparison Improvements**: Auto-detect line numbers, add "diff" mode highlighting
