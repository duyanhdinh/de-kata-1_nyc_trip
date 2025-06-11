import os
from pathlib import Path

def get_all_file_in_folder(folder):
    file_names = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    return file_names

def path_create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def clean_folder(folder_path):
    folder_path = Path(folder_path)
    for file in folder_path.iterdir():
        if file.is_file():
            file.unlink()

def append_file_list(file_list, output_path):
    with open(output_path, "a", encoding="utf-8") as f:
        for filename in file_list:
            f.write(filename + "\n")

def load_file_list_from_txt(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]