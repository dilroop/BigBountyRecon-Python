# Project Context - BigBountyRecon Python Port

This document provides context on the project structure, changes made, and key decisions during development.

## Project Overview

BigBountyRecon is a Python Tkinter port of the original C# Windows Forms application. It's a reconnaissance tool with 58+ techniques using Google dorks and open source tools for penetration testing and bug hunting.

## Project Structure

```
PythonRecon/
├── src/                          # Source code directory
│   ├── main.py                   # Main application entry point
│   └── recon_searches.py         # All reconnaissance search functions
├── run.bat                       # Windows launcher script
├── run.command                   # macOS launcher script
├── run.sh                        # Linux launcher script
├── build_windows.bat             # Windows build script (creates .exe)
├── build_macos.sh                # macOS build script (creates .app/.dmg)
├── build_linux.sh                # Linux build script (creates binary)
├── requirements.txt              # Dependencies documentation
├── README.md                     # User documentation
├── BUILD.md                      # Build instructions
├── .gitignore                   # Git ignore rules
├── .vscode/                     # VS Code configuration
│   ├── launch.json              # Debug configuration
│   └── tasks.json               # Task definitions
└── CONTEXT.md                   # This file
```

## Key Changes Made

### 1. UI Layout Restructuring
- **Changed from**: Complex 13-column layout with left/right sidebars and main grid
- **Changed to**: Simple 12-column uniform grid layout
- **Reason**: User requested simpler grid without special sorting/organization
- **Implementation**: All 58 buttons now fill left-to-right, top-to-bottom in a 12-column grid

### 2. Text Field Improvements
- **Centered**: Domain input field now centered in the frame
- **Font size**: Increased from 11 to 16 for better visibility
- **Implementation**: Changed from `pack(side=tk.LEFT)` to `pack(expand=True)`

### 3. Project Structure Reorganization
- **Created `src/` folder**: All Python source files moved into `src/`
  - `main.py` → `src/main.py`
  - `recon_searches.py` → `src/recon_searches.py`
- **Updated all scripts**: Run scripts and build scripts updated to reference `src/` paths
- **Reason**: Better project organization, separating source code from build/run scripts

### 4. Build System Setup
- **Added PyInstaller support**: Created build scripts for Windows, macOS, and Linux
- **Windows**: Creates `BigBountyRecon.exe` (single file executable)
- **macOS**: Creates `BigBountyRecon.app` bundle and optionally `BigBountyRecon.dmg`
- **Linux**: Creates `BigBountyRecon` binary
- **Build scripts**: Automated scripts handle PyInstaller installation and building

### 5. VS Code Configuration
- **Launch configuration**: Set up for debugging with Python 3.13.9
- **Issue resolved**: Fixed Python 3.14.0 beta compatibility issues by specifying stable Python version
- **Task configuration**: Added task to run shell scripts

### 6. Documentation
- **README.md**: Updated with new structure and build instructions
- **BUILD.md**: Comprehensive build guide with troubleshooting
- **requirements.txt**: Documents all dependencies (all standard library, no external packages needed)

## Technical Details

### Dependencies
All dependencies are part of Python standard library:
- `tkinter` - GUI framework
- `tkinter.ttk` - Themed widgets
- `tkinter.messagebox` - Message dialogs
- `webbrowser` - Opening URLs in browser
- `urllib.parse` - URL encoding/parsing
- `platform` - Platform detection for Chrome browser

**Build dependency**: `pyinstaller` (only needed for creating executables)

### Build Configuration
- **PyInstaller options used**:
  - `--windowed`: No console window (GUI only)
  - `--onefile` (Windows/Linux): Single executable
  - `--onedir` (macOS): Application bundle
  - `--paths=src`: Add src directory to Python path
  - `--add-data`: Include `recon_searches.py` in bundle
  - `--hidden-import`: Ensure all modules are included
  - `--osx-bundle-identifier`: macOS app identifier

### File Organization Decisions

1. **Source code in `src/`**: 
   - Keeps source code separate from build artifacts
   - Makes project structure cleaner
   - Follows common Python project conventions

2. **Run scripts in root**:
   - Easy to find and execute
   - Platform-specific launchers (`.bat`, `.command`, `.sh`)
   - Simple for end users

3. **Build scripts in root**:
   - Easy to run from project root
   - Platform-specific build scripts
   - Automated PyInstaller setup

4. **Documentation in root**:
   - README.md for users
   - BUILD.md for developers/builders
   - CONTEXT.md for project history

## Issues Resolved

### 1. Python Version Compatibility
- **Problem**: Python 3.14.0 beta causing macOS version check errors
- **Solution**: Updated launch.json to use Python 3.13.9 (stable version)
- **Location**: `.vscode/launch.json`

### 2. PyInstaller Icon Error
- **Problem**: `--icon=NONE` was interpreted as a file path
- **Solution**: Removed `--icon` parameter from all build scripts
- **Result**: PyInstaller uses default icon (works fine)

### 3. Import Path Issues
- **Problem**: After moving files to `src/`, imports needed updating
- **Solution**: Added `--paths=src` and `--hidden-import=recon_searches` to build scripts
- **Result**: PyInstaller correctly finds and bundles all modules

## Git Configuration

### .gitignore Rules
- `__pycache__/` - Python cache (auto-generated)
- `build/` and `dist/` - PyInstaller build artifacts
- `*.spec` - PyInstaller spec files
- `.vscode/` - VS Code settings (optional)
- OS files (`.DS_Store`, `Thumbs.db`)

### Files NOT to Commit
- `__pycache__/` folders (auto-generated)
- `build/` directory (temporary build files)
- `dist/` directory (output executables)
- `*.spec` files (can be regenerated)

## Build Process

### Windows
```bash
build_windows.bat
```
- Creates: `dist/BigBountyRecon.exe`
- Type: Single file executable

### macOS
```bash
./build_macos.sh
```
- Creates: `dist/BigBountyRecon.app` (application bundle)
- Optional: `dist/BigBountyRecon.dmg` (if create-dmg is installed)

### Linux
```bash
./build_linux.sh
```
- Creates: `dist/BigBountyRecon` (executable binary)

## Button Layout

The UI contains 58 buttons arranged in a 12-column grid:
- Buttons fill left-to-right, top-to-bottom
- No special sorting or categorization
- All buttons have icons and text labels
- Buttons are in the order they appear in `recon_searches.py`

## Key Files

### `src/main.py`
- Main application entry point
- Creates Tkinter GUI
- Handles UI layout and button creation
- Validates domain input before running searches

### `src/recon_searches.py`
- Contains all 58+ reconnaissance search functions
- Each function opens a URL in Chrome browser
- Functions are called by button clicks in the UI

### Run Scripts
- `run.bat` (Windows): Double-click to run
- `run.command` (macOS): Double-click to run
- `run.sh` (Linux): Execute from terminal

### Build Scripts
- Automatically install PyInstaller if needed
- Clean previous builds
- Build platform-specific executables
- Handle all PyInstaller configuration

## Future Considerations

1. **Icons**: Currently using default PyInstaller icons. Could add custom `.icns` (macOS) or `.ico` (Windows) files
2. **Code Signing**: For distribution, consider code signing executables
3. **Versioning**: Add version numbers to release binaries
4. **CI/CD**: Could automate builds with GitHub Actions or similar
5. **Testing**: Could add unit tests for search functions

## Notes

- All searches open in Chrome browser (falls back to default if Chrome not available)
- Application requires Chrome browser to be installed for full functionality
- Some Google searches may trigger CAPTCHA - this is expected behavior
- The application is a GUI wrapper around web-based reconnaissance tools

## Development Environment

- **Python**: 3.13.9 (recommended), 3.6+ (minimum)
- **IDE**: VS Code with Python extension
- **Platform**: Developed on macOS, tested for cross-platform compatibility
- **Build Tool**: PyInstaller 6.17.0+

---

*This context file was created to document the project structure and decisions made during development.*

