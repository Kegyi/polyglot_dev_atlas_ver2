# Phase 1: Schema Normalization & Modularity

## Completed ✅

### 1. Core Schema Files Created
- **base_block.json** - Foundation schema for all content blocks
  - Defines required/optional properties
  - Supports nested blocks, $ref pointers, metadata, style presets
  - Enables schema validation for all content

- **page_base.json** - Root page schema
  - Standardizes page metadata (title, description, category)
  - Adds `schema_version` field for graceful backwards compatibility
  - Defines `code_defaults` for page-level code block configuration

- **language_icons.json** - Shared language icon definitions
  - Single source of truth for language metadata
  - Can be imported via `$ref: "@core/language_icons"`
  - Prevents duplication across pages

### 2. JSON Reference Resolution System
Added `_resolve_json_ref()` method supporting:

**Format 1: Core References** (`@core/...`)
```json
{
  "$ref": "@core/language_icons"
}
```
Loads shared definitions from `content/core/` folder.

**Format 2: Snippet References** (`@snippets/...`)
```json
{
  "$ref": "@snippets/common_code_example.cpp"
}
```
Inlines external code/text files.

**Format 3: Image References** (`@images/...`)
```json
{
  "$ref": "@images/diagram.png"
}
```
Embeds images as base64 data URIs.

**Format 4: JSON Pointers** (`#/...`)
```json
{
  "$ref": "#/content/0/items"
}
```
References other content within the same document (RFC 6901 compliant).

### 3. Content Resolution Pipeline
Added `_process_content_with_refs()` method:
- Recursively walks content and blocks arrays
- Resolves all `$ref` pointers before rendering
- Merges resolved content with existing block properties (block properties override ref)
- Handles nested content/blocks structures

### 4. Build System Integration
Updated `process_page()` to:
- Call `_process_content_with_refs()` immediately after loading page JSON
- Ensures all references are resolved before rendering
- Happens transparently in the build pipeline

## Usage Examples

### Example 1: Reuse Shared Language Icons
**Before:** Each page duplicates language metadata
**After:** Single reference resolves to shared definition
```json
{
  "title": "Shared Language Definitions",
  "content": [
    {
      "type": "text",
      "text": "Using shared language icons:"
    },
    {
      "$ref": "@core/language_icons"
    }
  ]
}
```

### Example 2: Embed Code Snippets
```json
{
  "id": "factory_pattern_cpp",
  "title": "Factory Pattern - C++",
  "type": "code",
  "$ref": "@snippets/patterns/factory.cpp"
}
```

### Example 3: Inline Images as Data URIs
```json
{
  "id": "architecture_diagram",
  "type": "image",
  "$ref": "@images/architecture.png"
}
```

### Example 4: Merge with Overrides
```json
{
  "$ref": "@core/language_icons",
  "title": "Custom Title Override"
}
```
The resolved reference provides base properties, but `title` is overridden by the local value.

## Directory Structure

```
content/
├── core/                    ← New: Shared definitions
│   ├── base_block.json     ← Block schema
│   ├── page_base.json      ← Page schema
│   └── language_icons.json ← Shared language metadata
├── pages/
│   ├── atlas/
│   ├── course/
│   └── meta/
├── definitions/
├── schemas/
└── snippets/               ← External assets referenced via @snippets/
```

## API Reference

### `_resolve_json_ref(ref, base_path=None) → dict|str|None`
- **ref** (str): Reference string (@core/, @snippets/, @images/, or #/)
- **base_path** (str): Current page path (for JSON pointer resolution)
- **Returns**: Resolved data (dict), text (str), or base64 image URI

### `_process_content_with_refs(content_list, page_path=None) → list`
- **content_list** (list): Array of content blocks
- **page_path** (str): Current page path
- **Returns**: Processed content with all $refs resolved
- **Side effects**: Recursively processes nested content and blocks

## Benefits

1. **Content Reusability**: Eliminate duplicate definitions across pages
2. **Maintainability**: Single source of truth for shared content
3. **Modularity**: Split monolithic pages into composable blocks
4. **External Assets**: Reference code/images without embedding in JSON
5. **Scalability**: Add new shared definitions without code changes
6. **Backwards Compatible**: Non-$ref pages work identically before/after Phase 1

## Next Steps (Phase 2+)

- **Phase 2**: Generic Component Rendering system
  - Build flexible renderers for tables, mermaid, mathjax
  - Implement renderer registry for pluggable types

- **Validation**: Add `jsonschema` validation using `base_block.json` and `page_base.json`
  - Prevent malformed blocks at build time
  - Detect broken $ref pointers

- **Import Optimization**: Lazy load core definitions only when referenced
  - Reduce initial JSON parse time for large pages
  - Cache resolved references

---

**Implementation Date**: April 20, 2026  
**Status**: Stable - Ready for Phase 2
