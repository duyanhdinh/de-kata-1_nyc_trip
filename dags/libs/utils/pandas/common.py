import os

def get_all_file_in_folder(folder):
    file_names = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    return file_names