import os

from instances.config import SETTINGS

INSTANCES_PATH = SETTINGS["INSTANCES_PATH"]
INSTANCE_SIZE = SETTINGS["INSTANCE_SIZE"]
NUMBERS_EACH_LINE = SETTINGS["NUMBERS_EACH_LINE"]

def get_instance_path(instance_name):
    instance_path = os.path.join(INSTANCES_PATH, instance_name)
    return instance_path

def get_data_from_file(file_path):
    instance = []

    with open(file_path, "r") as file:
        for line in file:
            row = line.strip().split(",")
            first_element = row[0]

            if len(row) == 1 and first_element.isdigit():
                instance_size = int(first_element)
            
            if len(row) > 1:
                instance.extend(map(int, row))

    return instance, instance_size
