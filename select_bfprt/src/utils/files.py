import os

class Folder:
    def __init__(self, folder_path):
        self.set_path(folder_path)

    def set_path(self, folder_path):
        self.path = folder_path

    def get_path(self):
        return self.path

    def get_name(self):
        folder_path = self.get_path()
        possible_folder_names = folder_path.split("/")
        possible_folder_names = list(filter(lambda folder_name: folder_name != "", possible_folder_names))
        folder_name = possible_folder_names[-1]
        return folder_name

    def get_files_from_directory(self):
        path = self.get_path()
        folder_path = self.get_path()
        files_in_directory = os.listdir(folder_path)
        
        files = []
        for file_name in files_in_directory:
            file_path = f"{folder_path}/{file_name}"
            file = File(file_path)
            files.append(file)
        
        return files

class File:
    def __init__(self, file_path):
        self.set_path(file_path)

    def set_path(self, file_path):
        self.path = file_path
        self.name = self.path.split("/")[-1]

        folder_path = self.get_path()
        self.folder = Folder(folder_path)

    def set_name(self, name):
        self.name = name

    def get_path(self):
        folder_path = self.path.replace(f'/{self.name}', "")
        return folder_path

    def get_name(self):
        return self.name

def get_data_from_file(file_path):
    numbers = []
    with open(file_path, "r") as file:
        for line in file:
            row = line.strip().split(",")
            if len(row) == 10:
                numbers.extend(map(int, row))
    return numbers