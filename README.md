# Pyorganizer

A Python script to organize image files on your desktop into categorized folders based on their file extensions.

## Features

- Automatically scans your Desktop directory for image files
- Supports common image formats: JPG, JPEG, PNG, GIF, BMP, TIFF, WEBP
- Creates organized subfolders (e.g., JPG/, PNG/) on the Desktop
- Moves image files into their respective category folders
- Safe operation with error handling for file moves

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/johfleming93/Pyorganizer.git
   cd Pyorganizer
   ```

2. Make the script executable (optional):
   ```bash
   chmod +x organizer.py
   ```

## Usage

Run the script from the command line:

```bash
python organizer.py
```

Or if executable:

```bash
./organizer.py
```

The script will:
1. Scan your Desktop for image files
2. Create folders named after file types (JPG, PNG, etc.)
3. Move the images into their respective folders
4. Display progress and any errors

## Example Output

```
Scanning Desktop: /home/user/Desktop
Moving 5 JPG files to JPG/
  Moved: photo1.jpg
  Moved: vacation.jpg
  ...
Moving 3 PNG files to PNG/
  ...
Organization complete!
```

## Supported File Types

- .jpg / .jpeg → JPG folder
- .png → PNG folder
- .gif → GIF folder
- .bmp → BMP folder
- .tiff → TIFF folder
- .webp → WEBP folder

## Safety Notes

- Only image files are moved; other files remain untouched
- Folders are created on the Desktop
- If a folder with the same name already exists, files are added to it
- The script handles file move errors gracefully

## Contributing

Feel free to submit issues or pull requests for improvements!
