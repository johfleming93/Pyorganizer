#!/usr/bin/env python3
"""
Desktop App Organizer

This script scans the user's Desktop directory for .desktop application shortcut files
and organizes them alphabetically by renaming them with numerical prefixes and moving
them to an "Apps" folder on the Desktop.

Usage:
    python desktop_app_organizer.py

The script will create an "Apps" folder on the Desktop and move the .desktop files
into it, renamed as 01_AppName.desktop, 02_AnotherApp.desktop, etc., sorted alphabetically.
"""

import os
import shutil
from pathlib import Path

def get_desktop_path():
    """Get the path to the user's Desktop directory."""
    home = Path.home()
    desktop = home / 'Desktop'
    return desktop

def organize_desktop_apps():
    """Organize .desktop files on the Desktop alphabetically."""
    desktop = get_desktop_path()

    if not desktop.exists():
        print(f"Desktop directory not found: {desktop}")
        return

    print(f"Scanning Desktop: {desktop}")

    # Collect all .desktop files
    desktop_files = []
    for item in desktop.iterdir():
        if item.is_file() and item.suffix.lower() == '.desktop':
            desktop_files.append(item)

    if not desktop_files:
        print("No .desktop files found on the Desktop.")
        return

    # Sort the files alphabetically by name (case-insensitive)
    desktop_files.sort(key=lambda x: x.name.lower())

    # Create Apps folder
    apps_folder = desktop / 'Apps'
    apps_folder.mkdir(exist_ok=True)

    print(f"Moving {len(desktop_files)} .desktop files to Apps/ (sorted alphabetically)")

    # Move and rename files with numerical prefixes
    for i, file_path in enumerate(desktop_files, start=1):
        # Create new name with zero-padded number prefix
        new_name = f"{i:02d}_{file_path.name}"
        new_path = apps_folder / new_name

        try:
            shutil.move(str(file_path), str(new_path))
            print(f"  Moved and renamed: {file_path.name} -> {new_name}")
        except Exception as e:
            print(f"  Error moving {file_path.name}: {e}")

    print("Desktop app organization complete!")

if __name__ == "__main__":
    organize_desktop_apps()