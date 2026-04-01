import os

# Base Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
DIST_DIR = os.path.join(BASE_DIR, "dist")

# Build Settings
SETTINGS = {
    "title": "Polyglot Dev Atlas",
    "base_template": "base.html",
    "modules_path": os.path.join(CONTENT_DIR, "modules"),
    "locales_path": os.path.join(CONTENT_DIR, "locales"),
}

# Ensure dist exists
if not os.path.exists(DIST_DIR):
    os.makedirs(DIST_DIR)