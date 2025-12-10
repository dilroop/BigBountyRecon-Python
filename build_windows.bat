@echo off
REM Build script for Windows executable
REM This creates a BigBountyRecon.exe file

echo Building Windows executable...
echo.

REM Check if PyInstaller is installed
python -m pip install pyinstaller

REM Clean previous builds
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist BigBountyRecon.spec del BigBountyRecon.spec

REM Build the executable
pyinstaller --name=BigBountyRecon ^
    --onefile ^
    --windowed ^
    --paths=src ^
    --add-data "src\recon_searches.py;." ^
    --hidden-import=tkinter ^
    --hidden-import=tkinter.ttk ^
    --hidden-import=tkinter.messagebox ^
    --hidden-import=webbrowser ^
    --hidden-import=urllib.parse ^
    --hidden-import=platform ^
    --hidden-import=recon_searches ^
    src\main.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Build successful!
    echo Executable is in the 'dist' folder: dist\BigBountyRecon.exe
    echo.
) else (
    echo.
    echo Build failed!
    echo.
)

pause

