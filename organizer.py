import os
import sys
import shutil

if len(sys.argv) < 2:
    print("\nUsage: python organizer.py <foler_name>")
    sys.exit(1)


organize_dict = {
    ".mp3": "Music",
    ".jpg": "Photos",
    ".png" : "Photos",
    ".webp" : "Photos",
    ".jpeg" : "Photos",
    ".pdf": "Office",
    ".py": "Python Scripts",
    ".mp4" : "Videos",
    ".exe" : "Applications",
    ".dox" : "Office",
    ".ACCDA" : "Office",
    ".ecf" : "Office",
    ".pptx" : "Office",
    ".ppt" : "Office",
    ".xls" : "Office",
    ".doc": "Office",
    ".docm" : "Office",
    ".docx" : "Office",
    ".txt" : "Office"
}


folder_to_organize = sys.argv[1]

for folder_name in organize_dict.values():
    os.makedirs(os.path.join(folder_to_organize, folder_name), exist_ok=True)

for filename in os.listdir(folder_to_organize):
    if os.path.isfile(os.path.join(folder_to_organize, filename)):
        file_extension = os.path.splitext(filename)[1]
        if file_extension in organize_dict:
            folder_name = organize_dict[file_extension]
            source_path = os.path.join(folder_to_organize, filename)
            destination_path = os.path.join(folder_to_organize, folder_name, filename)
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to {folder_name}")
            except shutil.Error as e:
                print(f"Error moving {filename}: {e}")
