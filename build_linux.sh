#!/bin/bash

# Build script for Linux executable
# This creates a BigBountyRecon binary

echo "Building Linux executable..."
echo

# Check if PyInstaller is installed
if ! python3 -m pip show pyinstaller &> /dev/null; then
    echo "Installing PyInstaller..."
    python3 -m pip install pyinstaller
fi

# Clean previous builds
rm -rf dist build BigBountyRecon.spec

# Build the executable
pyinstaller --name=BigBountyRecon \
    --onefile \
    --windowed \
    --paths=src \
    --add-data "src/recon_searches.py:." \
    --hidden-import=tkinter \
    --hidden-import=tkinter.ttk \
    --hidden-import=tkinter.messagebox \
    --hidden-import=webbrowser \
    --hidden-import=urllib.parse \
    --hidden-import=platform \
    --hidden-import=recon_searches \
    src/main.py

if [ $? -eq 0 ]; then
    echo
    echo "Build successful!"
    echo "Executable is in the 'dist' folder: dist/BigBountyRecon"
    echo
    chmod +x dist/BigBountyRecon
else
    echo
    echo "Build failed!"
    echo
fi

