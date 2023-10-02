import uuid
import time
from utils.logger import logger
from instances import generate_instance

class Dataset:
    def __init__(self, id, instance_size):
        self.id = id
        self.instance_size = instance_size

    def get_name(self):
        return self.id

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def get_input_size(self):
        return self.instance_size

class RandomDataset(Dataset):
    def get_data(self):
        self.data, _ = generate_instance(self.instance_size)
        return self.data

class DatasetGroup:
    def __init__(self, instances_quantity, instance_size, instances=[]):
        self.instances_quantity = instances_quantity
        self.instance_size = instance_size
        self.instances = instances

    def get_datasets(self):
        datasets = []

        if len(self.instances) == 0:
            return self.create_random_datasets()

        return self.create_group_from_instances()

    def create_random_datasets(self):
        datasets = []

        for instance_id in range(self.instances_quantity):
            dataset = RandomDataset(instance_id, self.instance_size)
            datasets.append(dataset)

        return datasets

    def create_group_from_instances(self):
        datasets = []

        for instance_id, instance in enumerate(self.instances):
            dataset = Dataset(instance_id, len(instance))
            dataset.set_data(instance)
            datasets.append(dataset)

        return datasets
