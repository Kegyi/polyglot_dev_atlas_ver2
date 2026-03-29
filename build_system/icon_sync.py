import os
import json
import requests
import time

# Simple Icons often uses full names. 
# Mapping our 'languages.json' keys to their specific slugs.
SLUG_MAP = {
    "cpp": "cplusplus",
    "csharp": "dotnet",    # Simple Icons uses 'dotnet' for the C# logo
    "java": "openjdk",     # Simple Icons uses 'openjdk' or 'oracle'
    "scala2": "scala",     # Map both Scala versions to the base Scala icon
    "scala3": "scala",
    "js": "javascript",
    "ts": "typescript",
    "py": "python",
    "rs": "rust"
}

def sync_icons(languages_def_path, icons_dir):
    """
    Checks languages.json and downloads missing icons from the Simple Icons CDN.
    """
    if not os.path.exists(icons_dir):
        os.makedirs(icons_dir, exist_ok=True)

    with open(languages_def_path, 'r', encoding='utf-8') as f:
        langs = json.load(f)

    print("\n--- Starting Icon Sync ---")
    
    for lang_id, meta in langs.items():
        # Get filename from the 'icon' path defined in languages.json
        # e.g., "assets/icons/cpp.svg" -> "cpp.svg"
        icon_filename = os.path.basename(meta['icon'])
        local_path = os.path.join(icons_dir, icon_filename)

        if os.path.exists(local_path):
            print(f"  [OK] {lang_id} already exists.")
            continue 

        # Use the slug map or fallback to the ID itself
        slug = SLUG_MAP.get(lang_id, lang_id)
        
        # Simple Icons CDN URL (Returns the SVG directly)
        url = f"https://cdn.simpleicons.org/{slug}"
        
        try:
            print(f"  [DOWNLOADING] {lang_id} (slug: {slug})...")
            # Adding a User-Agent header is good practice for automated requests
            headers = {'User-Agent': 'PolyglotDevAtlas/2.0'}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                with open(local_path, 'wb') as f:
                    f.write(response.content)
                print(f"  [SAVED] {icon_filename}")
                # Brief sleep to be polite to the CDN
                time.sleep(0.1)
            else:
                print(f"  [FAILED] Could not find slug '{slug}' (Status {response.status_code})")
        
        except Exception as e:
            print(f"  [ERROR] Failed to download {lang_id}: {e}")

    print("--- Icon Sync Complete ---\n")

if __name__ == "__main__":
    # Ensure this runs from the root of your project
    sync_icons("content/definitions/languages.json", "assets/icons")