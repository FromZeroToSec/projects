from pathlib import Path

# Dictionary mapping file extensions to destination folder names
categories = {
    '.mp3': 'Music',
    '.wav': 'Music',
    '.flac': 'Music',
    '.avi': 'Videos',
    '.mp4': 'Videos',
    '.gif': 'Videos',
    '.txt': 'Documents',
    '.pptx': 'Documents',
    '.csv': 'Documents',
    '.xls': 'Documents',
    '.odp': 'Documents',
    '.pages': 'Documents',
    '.bmp': 'Images',
    '.png': 'Images',
    '.jpg': 'Images'
}

# Path to the source folder containing files to sort
source_folder = Path('~/Github/Python-training/07-file-sorter/data').expanduser()

# Iterate over all items in the source folder
for file in source_folder.iterdir():
    if file.is_file():
        extension = file.suffix
        # If extension is not in the dictionary, use 'Others' as fallback
        folder_name = categories.get(extension, 'Others')
        dest_folder = source_folder / folder_name
        # Create destination folder if it doesn't exist
        dest_folder.mkdir(exist_ok=True)
        # Move file to the destination folder
        file.rename(dest_folder / file.name)