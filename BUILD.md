# Building Executables for BigBountyRecon

This guide explains how to build standalone executables for Windows, macOS, and Linux.

## Prerequisites

1. **Python 3.6 or higher** installed
2. **PyInstaller** - Install with:
   ```bash
   pip install pyinstaller
   ```

3. **For macOS DMG creation** (optional):
   ```bash
   brew install create-dmg
   ```

## Building for Windows

### Option 1: Using the build script (Recommended)
```bash
build_windows.bat
```

### Option 2: Manual build
```bash
pyinstaller --name=BigBountyRecon --onefile --windowed --paths=src --add-data "src\recon_searches.py;." --hidden-import=recon_searches src\main.py
```

**Output:** `dist/BigBountyRecon.exe`

## Building for macOS

### Option 1: Using the build script (Recommended)
```bash
chmod +x build_macos.sh
./build_macos.sh
```

### Option 2: Manual build
```bash
pyinstaller --name=BigBountyRecon --windowed --onedir --paths=src --add-data "src/recon_searches.py:." --hidden-import=recon_searches --osx-bundle-identifier=com.bigbountyrecon.app src/main.py
```

**Output:** `dist/BigBountyRecon.app`

### Creating a DMG (Disk Image)

After building the app bundle, create a DMG:

```bash
# Install create-dmg if not already installed
brew install create-dmg

# Create DMG
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
```

**Output:** `dist/BigBountyRecon.dmg`

## Building for Linux

### Option 1: Using the build script (Recommended)
```bash
chmod +x build_linux.sh
./build_linux.sh
```

### Option 2: Manual build
```bash
pyinstaller --name=BigBountyRecon --onefile --windowed --paths=src --add-data "src/recon_searches.py:." --hidden-import=recon_searches src/main.py
chmod +x dist/BigBountyRecon
```

**Output:** `dist/BigBountyRecon`

## PyInstaller Options Explained

- `--name=BigBountyRecon`: Name of the executable/app
- `--onefile`: Creates a single executable file (Windows/Linux)
- `--onedir`: Creates a directory with the app (macOS bundle)
- `--windowed`: No console window (GUI only)
- `--paths=src`: Add src directory to Python path
- `--add-data`: Include additional files (src/recon_searches.py)
- `--hidden-import`: Ensure modules are included
- `--osx-bundle-identifier`: macOS app bundle identifier

## Troubleshooting

### "Module not found" errors
Add missing modules with `--hidden-import`:
```bash
--hidden-import=module_name
```

### Large file size
The executables will be large (50-100MB) because they include Python and all dependencies. This is normal.

### Antivirus warnings (Windows)
Some antivirus software may flag PyInstaller executables as suspicious. This is a false positive. You can:
- Submit to antivirus vendors for whitelisting
- Code sign the executable (requires certificate)

### macOS Gatekeeper warnings
To avoid "unidentified developer" warnings:
1. Code sign the app (requires Apple Developer account)
2. Notarize the app (for distribution outside App Store)

## Creating Release Binaries

### Recommended Structure:
```
releases/
├── BigBountyRecon-Windows-x64.exe
├── BigBountyRecon-macOS-x64.dmg
├── BigBountyRecon-Linux-x64
└── README.txt
```

### Steps:
1. Build for each platform
2. Test the executables on clean systems
3. Create a releases folder
4. Rename files with version numbers:
   - `BigBountyRecon-v1.0.0-Windows-x64.exe`
   - `BigBountyRecon-v1.0.0-macOS-x64.dmg`
   - `BigBountyRecon-v1.0.0-Linux-x64`
5. Create checksums (SHA256) for verification:
   ```bash
   # Windows
   certutil -hashfile BigBountyRecon.exe SHA256
   
   # macOS/Linux
   shasum -a 256 BigBountyRecon.dmg
   ```

## Advanced: Using a Spec File

For more control, create a spec file:
```bash
pyinstaller --name=BigBountyRecon src/main.py
```

Then edit `BigBountyRecon.spec` and rebuild:
```bash
pyinstaller BigBountyRecon.spec
```

## Notes

- Build on the target platform for best results (Windows exe on Windows, macOS app on macOS)
- The first build may take several minutes
- Subsequent builds are faster
- Always test executables on clean systems before distribution

