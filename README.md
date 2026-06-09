# Automated File Organizer (Python)

##  Overview
This project is a simple Python automation tool that organises files in a folder by sorting them into categories based on file type.

It scans a folder, checks each file’s extension, creates folders if needed, and moves files into the correct location automatically.

---

##  Features
- Automatically sorts files by type
- Creates folders if they do not exist
- Supports multiple file types (images, documents, music, etc.)
- Displays a log of moved files

---

##  Folder Setup (IMPORTANT)

Before running the script, your folder structure must look like this:


python downloads organiser/
│
├─ organiser.py
└─ downloads/
├─ music.mp3
├─ photo.jpg
├─ report.pdf
├─ notes.txt


 All files you want to sort must go inside the `downloads` folder.

---

## How It Works

1. The script scans the `downloads` folder.
2. It reads each file’s extension (for example `.pdf`, `.jpg`).
3. It matches the extension to a category using a dictionary.
4. It creates a folder for that category if it doesn’t exist.
5. It moves the file into the correct folder.

---

##  How to Run

1. Install Python:
   https://www.python.org/downloads/

2. Open the project folder(I used vs code).

3. Open terminal and run:

python organiser.py
 Example Output
Moved: report.pdf -> PDFs
Moved: photo.jpg -> Images
Moved: music.mp3 -> Music
