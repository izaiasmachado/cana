import uuid
import time
import tracemalloc
from utils.logger import logger
from utils import get_data_from_file, format_number

class Instance:
    def __init__(self, algorithm, dataset):
        self.uuid = uuid.uuid4()
        self.algorithm = algorithm
        self.dataset = dataset
        self.input = None
        self.error_name = None

    def get_uuid(self):
        return self.uuid

    def get_algorithm(self):
        return self.algorithm

    def get_dataset(self):
        return self.dataset

    def get_params(self):
        data = self.dataset.get_data()
        params = [data]

        if self.input is None:
            return params

        if isinstance(self.input, list):
            params.extend(self.input)
        else:
            params.append(self.input)

        return params

    def set_input(self, input):
        self.input = input

    def get_input(self):
        return self.input

    def execute(self):
        try:
            params = self.get_params()

            tracemalloc.start()
            start = time.time()
            self.output = self.algorithm.run(*params)
            end = time.time()

            _, self.peak_memory_usage = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            self.execution_time = end - start
            return self.output
        except Exception as e:
            error_name = e.__class__.__name__
            self.set_error(error_name)

    def get_execution_time(self):
        return self.execution_time

    def get_peak_memory_usage(self):
        return self.peak_memory_usage
    
    def set_error(self, error_name):
        self.error_name = error_name

    def get_error(self):
        return self.error_name

    def get_formated_execution_time(self):
        if hasattr(self, 'execution_time'):
            return format_number(self.execution_time)
        
        return None

    def get_formated_peak_memory_usage(self):
        if hasattr(self, 'peak_memory_usage'):
            return format_number(self.peak_memory_usage)
        
        return None