import uuid
import time
from utils.logger import logger
from utils import Folder, File
from instances import get_instance_path

from instances import get_instance_path, get_data_from_file, generate_instance

class Dataset:
    def __init__(self, id, instance_size):
        self.id = id
        self.instance_size = instance_size

    def get_name(self):
        return self.id

    def get_data(self):
        self.data, _ = generate_instance(self.instance_size)
        return self.data
    
    def get_input_size(self):
        return self.instance_size

class DatasetGroup:
    def __init__(self, instances_quantity, instance_size):
        self.instances_quantity = instances_quantity
        self.instance_size = instance_size

    def get_datasets(self):
        datasets = []

        for instance_id in range(self.instances_quantity):
            dataset = Dataset(instance_id, self.instance_size)
            datasets.append(dataset)

        return datasets
