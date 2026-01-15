#!/bin/bash

# Clear terminal screen
clear

echo "=========================================="
echo "     LAUNCHING PASSWORD AUDITOR TOOL      "
echo "=========================================="
echo

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "[!] ERROR: Python 3 could not be found."
    echo "    Please install it using: sudo apt install python3"
    echo
    read -p "Press Enter to exit..."
    exit 1
fi

# Run the script
python3 auditor.py

# Keep terminal open after exit
echo
echo "=========================================="
read -p "Press Enter to close this window..."