#!/bin/bash

# Build script for macOS application bundle and DMG
# This creates a BigBountyRecon.app and BigBountyRecon.dmg file

echo "Building macOS application bundle..."
echo

# Check if PyInstaller is installed
if ! python3 -m pip show pyinstaller &> /dev/null; then
    echo "Installing PyInstaller..."
    python3 -m pip install pyinstaller
fi

# Clean previous builds
rm -rf dist build BigBountyRecon.spec

# Build the application bundle
pyinstaller --name=BigBountyRecon \
    --windowed \
    --onedir \
    --paths=src \
    --add-data "src/recon_searches.py:." \
    --hidden-import=tkinter \
    --hidden-import=tkinter.ttk \
    --hidden-import=tkinter.messagebox \
    --hidden-import=webbrowser \
    --hidden-import=urllib.parse \
    --hidden-import=platform \
    --hidden-import=recon_searches \
    --osx-bundle-identifier=com.bigbountyrecon.app \
    src/main.py

if [ $? -eq 0 ]; then
    echo
    echo "Application bundle created successfully!"
    echo "Location: dist/BigBountyRecon.app"
    echo
    
    # Create DMG if create-dmg is available
    if command -v create-dmg &> /dev/null; then
        echo "Creating DMG file..."
        create-dmg \
            --volname "BigBountyRecon" \
            --window-pos 200 120 \
            --window-size 800 400 \
            --icon-size 100 \
            --icon "BigBountyRecon.app" 200 190 \
            --hide-extension "BigBountyRecon.app" \
            --app-drop-link 600 185 \
            "dist/BigBountyRecon.dmg" \
            "dist/BigBountyRecon.app"
        
        if [ $? -eq 0 ]; then
            echo "DMG created successfully: dist/BigBountyRecon.dmg"
        else
            echo "DMG creation failed. Install create-dmg: brew install create-dmg"
        fi
    else
        echo "To create a DMG, install create-dmg: brew install create-dmg"
        echo "Then run this script again, or manually create a DMG from dist/BigBountyRecon.app"
    fi
else
    echo
    echo "Build failed!"
    echo
fi

