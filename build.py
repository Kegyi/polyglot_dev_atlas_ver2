#!/usr/bin/env python3
import sys
import os
import traceback

# Ensure the script can find the build_system package in the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """
    Polyglot Dev Atlas - Build Entry Point
    Triggers the refactored 'Smart Brain' to perform a recursive, 
    data-driven build of the Atlas and Course modes.
    """
    print("="*50)
    print("   POLYGLOT DEV ATLAS - GENERATOR v2.0")
    print("="*50)

    try:
        # Import the refactored core logic
        from build_system.core import AtlasBuilder
        
        # Initialize the builder
        builder = AtlasBuilder()
        
        # Execute the recursive build process
        # This handles: 
        # 1. Path Registration (Atlas vs Course)
        # 2. Sidebar/Navigation assembly
        # 3. Snippet Comparison injection
        # 4. Final HTML stitching with Anti-Flash logic
        builder.build()

        print("-" * 50)
        print("✨ SUCCESS: Build completed.")
        print(f"📂 Output directory: {builder.dist_dir}")
        print("💡 Hint: Open 'dist/index.html' in a browser to test.")
        print("="*50)

    except ImportError as e:
        print("\n❌ CRITICAL ERROR: Build system modules not found.")
        print(f"Details: {e}")
        sys.exit(1)
        
    except Exception as e:
        print("\n❌ BUILD FAILED")
        print(f"Error Type: {type(e).__name__}")
        print(f"Message: {str(e)}")
        print("\nDebug Stack Trace:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()