from pathlib import Path
import shutil

# Folder to organize
SOURCE_FOLDER = Path("test_directory")

# File extension categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Python": [".py"],
}


def get_category(extension):
    """Return the folder category for a file extension."""

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """Create a new filename if the file already exists."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files():
    """Organize files according to their extensions."""

    if not SOURCE_FOLDER.exists():
        print(f"Error: '{SOURCE_FOLDER}' folder does not exist.")
        return

    moved_files = 0

    for file in SOURCE_FOLDER.iterdir():

        # Skip folders
        if not file.is_file():
            continue

        # Find category
        category = get_category(file.suffix)

        # Create category folder
        destination_folder = SOURCE_FOLDER / category
        destination_folder.mkdir(exist_ok=True)

        # Create safe destination path
        destination = destination_folder / file.name
        destination = get_unique_path(destination)

        # Move file
        shutil.move(str(file), str(destination))

        print(f"Moved: {file.name} -> {category}/")
        moved_files += 1

    print("\n==============================")
    print("File organization completed!")
    print(f"Total files moved: {moved_files}")
    print("==============================")


if __name__ == "__main__":
    organize_files()
    