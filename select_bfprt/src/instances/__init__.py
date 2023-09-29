from instances.read_instances import get_instance_path, get_data_from_file
from instances.generate_instances import create_instance
from instances.config import SETTINGS

def get_instances_folder_path():
    return SETTINGS['INSTANCES_PATH']
