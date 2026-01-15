@echo off
title Password Auditor Tool v1.0
color 0A

echo ==========================================
echo      LAUNCHING PASSWORD AUDITOR TOOL
echo ==========================================
echo.

cd /d "%~dp0"

echo [*] Initializing python environment...
echo.

:: Check if Python is accessible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] ERROR: Python is not installed or not added to PATH.
    echo     Please install Python from python.org
    pause
    exit
)

:: Run the script
python src\auditor.py

echo.
echo ==========================================
echo [!] Program finished.
pause
