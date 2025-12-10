#!/bin/bash

# BigBountyRecon Launcher Script
# This script launches the BigBountyRecon Python Tkinter application

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the script directory
cd "$SCRIPT_DIR"

# Try to use python3, fallback to python if python3 is not available
if command -v python3 &> /dev/null; then
    python3 src/main.py
elif command -v python &> /dev/null; then
    python src/main.py
else
    echo "Error: Python is not installed or not in PATH"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

