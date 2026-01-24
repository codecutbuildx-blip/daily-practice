# LEARNING OBJECTIVE:
# This tutorial teaches you how to automate file organization using Python.
# You will learn to scan a specified directory, identify files by their type (extension),
# and move them into categorized subfolders, making your file system tidier and more organized.

import os
from pathlib import Path  # pathlib offers an object-oriented way to handle file paths, making code cleaner and cross-platform compatible.
import shutil  # shutil provides high-level operations on files and collections of files, like moving them.

# 1. Define File Categories:
# This dictionary maps a category name (which will become a folder name) to a list of file extensions.
# This is easily customizable. You can add more categories or extensions as needed.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".php", ".sh"],
    # Files with extensions not listed above will be moved into an 'Other' folder.
}

def get_file_category(file_path):
    """
    Determines the category (e.g., 'Images', 'Documents') for a given file
    based on its file extension.

    WHAT: This function takes a file's Path object and returns a string representing its category.
    WHY: We need a way to classify each file so we know which subfolder to move it into.
    """
    # Get the file's extension. Path.suffix returns the extension including the dot (e.g., '.txt').
    # We convert it to lowercase to ensure case-insensitive matching (e.g., '.JPG' matches '.jpg').
    extension = file_path.suffix.lower()

    # Iterate through our defined categories.
    for category, extensions in FILE_CATEGORIES.items():
        # Check if the file's extension is in the list of extensions for the current category.
        if extension in extensions:
            return category  # If a match is found, return the category name.

    # If no matching category is found after checking all defined categories,
    # assign the file to a general 'Other' category.
    return "Other"

def organize_files(source_directory):
    """
    Scans the specified source_directory, identifies files by type, and moves them
    into appropriately named subfolders.

    WHAT: This is the main function that orchestrates the file organization process.
    WHY: It encapsulates all the steps: checking directory, iterating files, categorizing,
         creating folders, and moving files.
    """
    # Convert the input string path to a Path object. This makes file operations easier and safer.
    source_path = Path(source_directory)

    # Validate the source directory: Check if it exists and is indeed a directory.
    # WHAT: Ensures we're not trying to organize files in a non-existent or invalid location.
    # WHY: Prevents errors and provides clear feedback to the user.
    if not source_path.is_dir():
        print(f"ERROR: Source directory '{source_directory}' does not exist or is not a directory.")
        return # Exit the function if the directory is invalid.

    print(f"Starting file organization in: '{source_path}'")

    # Iterate over all items (files and subdirectories) directly within the source directory.
    # `iterdir()` is a clean way provided by pathlib to list directory contents.
    for item in source_path.iterdir():
        # We only want to process actual files, not subdirectories or system files.
        if item.is_file():
            # Determine which category this file belongs to using our helper function.
            category = get_file_category(item)

            # Construct the path for the target category folder.
            # Example: If source_path is 'Downloads' and category is 'Images', this creates 'Downloads/Images'.
            target_category_dir = source_path / category

            # Create the target category directory if it doesn't already exist.
            # `exist_ok=True` prevents an error if the directory already exists,
            # which is useful if we run the script multiple times.
            try:
                target_category_dir.mkdir(exist_ok=True)
                # WHAT: Creates the folder if it's not there.
                # WHY: Files need a place to go before they can be moved.
            except OSError as e:
                print(f"ERROR: Could not create directory '{target_category_dir}': {e}")
                continue # Skip to the next file if folder creation fails.

            # Construct the full destination path for the file (new folder + original filename).
            # Example: 'Downloads/Images/my_picture.jpg'
            destination_path = target_category_dir / item.name

            # Move the file from its current location to the new categorized folder.
            # shutil.move handles moving files, even across different file systems.
            try:
                # `str(item)` and `str(destination_path)` convert Path objects to strings,
                # ensuring compatibility with older versions of `shutil.move` or underlying OS calls.
                shutil.move(str(item), str(destination_path))
                print(f"Moved '{item.name}' to '{category}/'")
                # WHAT: Physically moves the file.
                # WHY: This is the core action of organization.
            except shutil.Error as e:
                print(f"ERROR: Could not move '{item.name}' to '{destination_path}': {e}")
            except Exception as e:
                print(f"AN UNEXPECTED ERROR occurred while moving '{item.name}': {e}")

    print("File organization complete!")

# 2. Example Usage: How to run the script.
# This block ensures the code inside it only runs when the script is executed directly,
# not when imported as a module into another script.
if __name__ == "__main__":
    # --- IMPORTANT NOTE FOR TESTING ---
    # It is HIGHLY recommended to use a *temporary* directory for testing this script
    # to avoid accidentally reorganizing your important personal files.
    # The example below creates a 'test_files_to_organize' directory
    # within the same directory where this script is located.

    # Define the name of our temporary test directory.
    test_directory_name = "test_files_to_organize"
    test_path = Path(test_directory_name)

    # Clean up any previous test runs by removing the test directory and its contents.
    # WHAT: Ensures a clean slate for each test run.
    # WHY: Prevents old files from interfering with new tests and keeps your system tidy.
    if test_path.exists():
        print(f"Cleaning up previous test directory: '{test_path}'...")
        shutil.rmtree(test_path) # `rmtree` removes a directory and all its contents recursively.
        print("Cleanup complete.")

    # Create the fresh test directory for this run.
    test_path.mkdir()
    print(f"Created new test directory: '{test_path}'")

    # Create some dummy files inside the test directory for demonstration purposes.
    # These files simulate a cluttered download folder.
    dummy_files = {
        "document_report.pdf": "Content of a PDF report.",
        "vacation_pic.jpg": "Content of a JPG image.",
        "my_photo.png": "Content of a PNG image.",
        "meeting_notes.docx": "Content of a Word document.",
        "promo_video.mp4": "Content of an MP4 video.",
        "favorite_song.mp3": "Content of an MP3 audio file.",
        "project_archive.zip": "Content of a ZIP archive.",
        "script_tool.py": "print('Hello, Organizer!')",
        "plain_text_info.txt": "Some basic text information.",
        "miscellaneous_item.xyz": "Content of an unknown file type.", # This will go into 'Other'
        "another_image.gif": "Content of a GIF image.",
        "spreadsheet_data.csv": "col1,col2\nval1,val2",
    }

    # Write the dummy file contents into the test directory.
    for filename, content in dummy_files.items():
        (test_path / filename).write_text(content)
        print(f"Created dummy file: '{filename}'")

    print("\n--- Running File Organization Script ---\n")
    # Call our main organization function with the path to the test directory.
    organize_files(test_directory_name)

    print("\n--- Verification: Contents of the organized directory ---")
    # After organization, list the contents of the test directory to verify the results.
    # `rglob('*')` recursively finds all files and directories within `test_path`.
    for item in sorted(test_path.rglob('*')):
        # Print the path relative to our test directory for cleaner output.
        print(f"- {item.relative_to(test_path)}")

    # You can now manually check the 'test_files_to_organize' folder
    # to see how the files have been sorted into subfolders like 'Images', 'Documents', etc.

    # Uncomment the following lines if you want the script to automatically
    # clean up the test directory after verification.
    # print(f"\nCleaning up final test directory: '{test_path}'...")
    # shutil.rmtree(test_path)
    # print("Final test cleanup complete.")