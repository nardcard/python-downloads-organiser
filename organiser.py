from pathlib import Path
import shutil

# Folder to organise
downloads_folder = Path(r"C:\Users\comp5292379\Desktop\python downloads organiser\downloads")

# File type categories
file_categories = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp3": "Music",
    ".txt": "Text Files",
    ".doc": "Word Documents",
    ".pptx": "PowerPoint Presentations",
    ".ppt": "PowerPoint Presentations",
}

print("SCRIPT STARTED")

# Check every item in the folder
for file in downloads_folder.iterdir():

    # Get file extension
    file_extension = file.suffix.lower()

    # Find matching category
    category = file_categories.get(file_extension, "Other Files")

    # Create destination folder if needed
    target_folder = downloads_folder / category
    target_folder.mkdir(exist_ok=True)

    # Move file to destination folder
    shutil.move(str(file), str(target_folder / file.name))

    # Display what happened
    print(f"Moved: {file.name} -> {category}")

print("SORT COMPLETE")