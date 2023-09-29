import os
from utils import logger, format_number
from execution.instance import Instance

class SelectBFPRTInstanceExecutor:
    def __init__(self, algorithm_collection, dataset_group):
        self.algorithm_collection = algorithm_collection
        self.dataset_group = dataset_group
        self.create_instances()

    def create_instances(self):
        self.instances = []

        for i in self.dataset_group.get_datasets():
            for j in self.algorithm_collection.get_algorithms():
                instance = Instance(j, i)
                self.instances.append(instance)

        return self.instances        

    def execute(self):
        instances = self.instances

        for i, instance in enumerate(instances):
            dataset = instance.get_dataset()
            dataset_data = dataset.get_data()

            n = instance.get_dataset().get_input_size()
            k = n // 2

            instance.set_input([n, k])

            uuid = instance.get_uuid()
            dataset = instance.get_dataset()
            dataset_name = dataset.get_name()
            algorithm_name = instance.get_algorithm().get_name()


            output = instance.execute()
            error = instance.get_error()
            formated_execution_time = instance.get_formated_execution_time()

            with open(f'data/output.csv', 'a') as file:
                file.write(f"{uuid},{algorithm_name},{dataset_name},{n},{k},{output},{formated_execution_time},{error}\n")

            logger.info(f"Instance {i + 1} of {len(instances)}")
            logger.info(f"Algorithm: {instance.get_algorithm().get_name()}")
            logger.info(f"Dataset: {instance.get_dataset().get_name()}")
            logger.info(f"Input: {instance.get_input()}")
            
            if error:
                logger.error(f"Error Handled: {error}")

            logger.info(f"Output: {output}")
            logger.info(f"Execution Time: {formated_execution_time}")
            logger.info(f'{"-" * 50}')

            del dataset_data
