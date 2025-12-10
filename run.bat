@echo off
REM BigBountyRecon Launcher Script for Windows
REM This script launches the BigBountyRecon Python Tkinter application

REM Change to the script directory
cd /d "%~dp0"

REM Try to use python, fallback to py if python is not available
python src\main.py 2>nul
if errorlevel 1 (
    py src\main.py 2>nul
    if errorlevel 1 (
        echo Error: Python is not installed or not in PATH
        echo Please install Python 3.6 or higher
        pause
        exit /b 1
    )
)

pause

