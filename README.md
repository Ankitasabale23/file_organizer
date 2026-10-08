# File Organizer

## 1. Objective
Create a Python script that scans a folder and automatically organizes files into different folders based on their file extensions.

## 2. Tools Used
- Python
- pathlib
- shutil
- VS Code

## 3. How It Works
- The program scans the `test_directory` folder.
- Files are identified by their extensions.
- Files are moved into folders such as Images, Documents, Audio, Videos, and Python.
- Duplicate filenames are handled safely by creating a unique filename.

## 4. How to Run
1. Keep `file_organizer.py` and `test_directory` in the same folder.
2. Add test files inside `test_directory`.
3. Open the terminal in the project folder.
4. Run:
   `python file_organizer.py`
5. The program automatically creates the required folders and moves the files into the correct folders.