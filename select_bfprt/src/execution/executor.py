import os
import random
from utils import logger, format_number
from execution.instance import Instance

class SelectBFPRTInstanceExecutor:
    def __init__(self, algorithm_collection, dataset_group, worker_id=None, output_file_name=None):
        self.algorithm_collection = algorithm_collection
        self.dataset_group = dataset_group
        self.worker_id = worker_id
        self.output_file_path = output_file_name
        self.create_instances()

    def create_instances(self):
        self.instances = []

        for dataset in self.dataset_group.get_datasets():
            n = dataset.get_input_size()
            k = random.randint(1, n)

            for algorithm in self.algorithm_collection.get_algorithms():
                instance = Instance(algorithm, dataset)
                instance.set_input([n, k])
                self.instances.append(instance)

        return self.instances

    def execute(self):
        instances = self.instances

        for i, instance in enumerate(instances):
            instance.execute()

            logger.info(f"Instance {i + 1} of {len(instances)}")
            instance.log_results()
            logger.info(f'{"-" * 50}')
            self.print_results_to_file(instance)

    def print_results_to_file(self, instance):
        uuid = instance.get_uuid()
        worker_id = self.worker_id
        dataset_name = instance.get_dataset().get_name()
        algorithm_name = instance.get_algorithm().get_name()
        n, k = instance.get_input()
        output = instance.output
        formated_execution_time = instance.get_formated_execution_time()
        error = instance.get_error()

        if self.output_file_path is None:
            return

        with open(f'data/{self.output_file_path}', 'a') as file:
            file.write(f"{uuid},{worker_id},{dataset_name},{algorithm_name},{n},{k},{output},{formated_execution_time},{error}\n")
