import os
import sys
from execution import DatasetGroup, SelectBFPRTInstanceExecutor
from algorithms import create_algorithm_collection

def random_execution(worker_id, instance_size, instances_quantity, output_file_name):
    algorithm_collection = create_algorithm_collection()
    dataset_group = DatasetGroup(instances_quantity, instance_size)

    executor = SelectBFPRTInstanceExecutor(algorithm_collection, dataset_group, worker_id=worker_id, output_file_name=output_file_name)
    executor.execute()

def manual_execution(instance):
    algorithm_collection = create_algorithm_collection()
    dataset_group = DatasetGroup(1, len(instance), instances=[instance])

    executor = SelectBFPRTInstanceExecutor(algorithm_collection, dataset_group)
    executor.execute()

if __name__ == "__main__":
    try:
        execute_instances()
    except KeyboardInterrupt:
        logger.info("Programa finalizado!")