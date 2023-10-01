import os
from instances.read_instances import get_instance_path, get_data_from_file
from instances.generate_instances import create_instance, generate_instance
from instances.config import SETTINGS

def get_instances_folder_path():
    return SETTINGS['INSTANCES_PATH']

def get_instances_quantity():
    instances_folder_path = get_instances_folder_path()
    instances_amount = len(os.listdir(instances_folder_path))
    return instances_amount
