import os

def create_folders(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

folder_paths = ["folder1", "folder2/subfolder", "folder3"]
create_folders(folder_paths)