from .assemblers import assemble_keyword_sheet, assemble_code_comparison
from .navigation import assemble_language_picker, assemble_sidebar

# This maps the "type" field in your page.json to the assembler function
BLOCK_REGISTRY = {
    "keyword_sheet": assemble_keyword_sheet,
    "code_comparison": assemble_code_comparison,
    "ui_lang_picker": assemble_language_picker,
    "ui_sidebar": assemble_sidebar
}

def get_assembler(block_type):
    """Returns the function associated with a block type."""
    return BLOCK_REGISTRY.get(block_type)