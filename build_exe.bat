@echo off
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --clean --onefile --windowed --name Preference_Distance --paths src run_app.py
