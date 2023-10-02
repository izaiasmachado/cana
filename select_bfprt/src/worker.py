import os
import sys
from utils import logger, format_number

from algorithms import select_bfprt_factory
from instances import create_instance, get_instances_folder_path
from execution import AlgorithmCollection, DatasetGroup, SelectBFPRTInstanceExecutor
from algorithms import create_algorithm_collection

from execution.execution import manual_execution, random_execution

def execute_instances():
    worker_id = int(sys.argv[1])
    instance_size = int(sys.argv[2])
    instances_quantity = int(sys.argv[3])
    output_file_name = sys.argv[4]

    random_execution(worker_id, instance_size, instances_quantity, output_file_name)

if __name__ == "__main__":
    try:
        execute_instances()
    except KeyboardInterrupt:
        logger.info("Programa finalizado!")