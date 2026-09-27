"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Joy Nisperos]
Date: [September 27,2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[I have a file sorting script using Python os and shutil modules. 
The script checks the files inside a folder and 
sorts them into different folders based on their file extensions.
For example, .txt files are moved to the Documents folder, 
.jpg and .png files are moved to the Images folder, 
and .pdf files are moved to the PDFs folder. 
If the required folders do not exist, 
the script creates them first.]


============================================
KEY VOCABULARY
============================================
- os module:  A Python module that lets me work with files, folders, and paths on the computer.
- shutil module: A Python module that provides functions for moving and copying files.
- file path: The location of a file or folder on the computer.
- directory: Another name for a folder that can contain files and other folders.
(add more as needed)
- file extension: The part at the end of a filename that tells what type of file it is,
(.txt, .jpg, or .pdf.)

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "files"

folders = {
".txt": "Documents",
".pdf": "PDFs",
".jpg": "Images",
".png": "Images"
}

for folder in folders.values():
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

if os.path.isfile(file_path):
    extension = os.path.splitext(filename)[1].lower()

    if extension in folders:
        destination_folder = os.path.join(
            source_folder, folders[extension]
        )

        shutil.move(file_path, destination_folder)

print("Files sorted successfully!")

# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I had to be careful about the file path. 
If the folder name or path is incorrect, 
the program will not be able to find the files. 
I also learned that I need to check if something is actually a file 
before trying to move it, because the source folder 
can also contain other folders.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[This activity is similar to real automation scripts 
because a program can organize files automatically 
instead of making a person move each file one by one. 
For example, I could use something similar to organize documents, 
attendance files, or school requirements into separate folders. 
This could save time when there are many files to organize.]
"""
