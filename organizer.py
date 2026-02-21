#!/usr/bin/env python3
"""
Pyorganizer: Desktop Image Organizer

This script scans the user's Desktop directory for image files and organizes them
into subfolders based on their file extensions (e.g., JPG, PNG, GIF).

Supported image extensions: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp

Usage:
    python organizer.py

The script will create folders like 'JPG', 'PNG', etc., on the Desktop and move
the corresponding image files into them.
"""

import os
import shutil
from pathlib import Path

# Define supported image extensions (lowercase for case-insensitive matching)
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

def get_desktop_path():
    """Get the path to the user's Desktop directory."""
    home = Path.home()
    desktop = home / 'Desktop'
    return desktop

def organize_images():
    """Organize image files on the Desktop into categorized folders."""
    desktop = get_desktop_path()

    if not desktop.exists():
        print(f"Desktop directory not found: {desktop}")
        return

    print(f"Scanning Desktop: {desktop}")

    # Dictionary to hold files by extension
    files_by_ext = {}

    # Scan the desktop for image files
    for item in desktop.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            if ext in IMAGE_EXTENSIONS:
                if ext not in files_by_ext:
                    files_by_ext[ext] = []
                files_by_ext[ext].append(item)

    if not files_by_ext:
        print("No image files found on the Desktop.")
        return

    # Create folders and move files
    for ext, files in files_by_ext.items():
        # Create folder name (remove the dot and uppercase)
        folder_name = ext[1:].upper()
        folder_path = desktop / folder_name

        # Create the folder if it doesn't exist
        folder_path.mkdir(exist_ok=True)

        print(f"Moving {len(files)} {folder_name} files to {folder_name}/")

        for file_path in files:
            try:
                shutil.move(str(file_path), str(folder_path / file_path.name))
                print(f"  Moved: {file_path.name}")
            except Exception as e:
                print(f"  Error moving {file_path.name}: {e}")

    print("Organization complete!")

if __name__ == "__main__":
    organize_images()