import os
from utils import logger, format_number

from algorithms import select_bfprt_factory
from instances import create_instance, get_instances_folder_path
from execution import AlgorithmCollection, DatasetGroup, SelectBFPRTInstanceExecutor

def create_algorithm_collection():
    algorithm_collection = AlgorithmCollection()
    partition_sizes = [3, 5, 7, 9, 11]

    for r in partition_sizes:
        algorithm_collection.add_algorithm(f"Select BFPRT - r = {r}", select_bfprt_factory(r))

    return algorithm_collection

def create_dataset_group():
    dataset_group_path = get_instances_folder_path()
    dataset_group = DatasetGroup(dataset_group_path)
    return dataset_group

if __name__ == "__main__":
    # for _ in range(1000):
    #     create_instance()

    algorithm_collection = create_algorithm_collection()
    dataset_group = create_dataset_group()
    
    executor = SelectBFPRTInstanceExecutor(algorithm_collection, dataset_group)
    executor.execute()
