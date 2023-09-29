import uuid
import time
from utils.logger import logger
from utils import Folder, File
from instances import get_instance_path

from instances import get_instance_path, get_data_from_file

class Dataset:
    def __init__(self, file):
        self.set_file(file)

    def set_file(self, file):
        self.file = file

    def get_file(self):
        return self.file

    def get_name(self):
        file_name = self.file.get_name()
        name = file_name.replace(".txt", "")
        return name

    def get_path(self):
        file = self.get_file()
        folder_path = file.get_path()
        file_name = file.get_name()
        path = f"{folder_path}/{file_name}"
        return path

    def get_data(self):
        if hasattr(self, "data"):
            return self.data

        file_path = self.get_path()
        data, dataset_size = get_data_from_file(file_path)

        self.set_dataset_size(dataset_size)
        self.data = data

        return data

    def set_dataset_size(self, input_size):
        self.input_size = input_size
    
    def get_input_size(self):
        return self.input_size

class DatasetGroup:
    def __init__(self, folder_path, start_instance_id, end_instance_id):
        self.folder = Folder(folder_path)
        self.start_instance_id = start_instance_id
        self.end_instance_id = end_instance_id

    def get_datasets(self):
        datasets = []
        files = self.folder.get_files_from_directory()
        text_files = list(filter(lambda file: file.get_name().endswith(".txt"), files))
        sorted_text_files = sorted(text_files, key=lambda file: file.get_name())
        
        # Usando os indices de início e fim para selecionar apenas um subconjunto de instâncias
        sorted_text_files = sorted_text_files[self.start_instance_id : self.end_instance_id + 1]

        for file in sorted_text_files:
            dataset = Dataset(file)
            datasets.append(dataset)

        return datasets
