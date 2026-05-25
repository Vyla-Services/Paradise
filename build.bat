@echo off
echo Building Paradise...

rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del *.spec 2>nul

pyinstaller --onefile paradise_cli/main.py --name paradise

pyinstaller --onefile paradise_ui/app.py --name Paradise ^
    --add-data "paradise_ui/assets;paradise_ui/assets"

echo Build complete.
pause
