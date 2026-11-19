@echo off
setlocal
cd /d "%~dp0"
title Hostel Maintenance Dashboard
if not exist ".venv\Scripts\python.exe" (
  echo Python environment not found. Run setup.bat first.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" dashboard.py
pause
