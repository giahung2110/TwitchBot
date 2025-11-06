@echo off
title Auto Install Python Dependencies by GiaHung
echo ===============================================
echo 🚀 Installing Required Python Libraries...
echo ===============================================
python -m pip install --upgrade pip
pip install selenium webdriver-manager colorama
echo.
echo ✅ Installation Complete!
echo Press any key to exit...
pause >nul
