class Algorithm:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def get_name(self):
        return self.name

    def run(self, *args):
        return self.function(*args)

    def __str__(self):
        return self.name

class AlgorithmCollection:
    def __init__(self):
        self.algorithms = []

    def add(self, algorithm):
        self.algorithms.append(algorithm)

    def add_algorithm(self, name, function):
        algorithm = Algorithm(name, function)
        self.add(algorithm)

    def get_algorithms(self):
        return self.algorithms

    def get_algorithm(self, name):
        for algorithm in self.algorithms:
            if algorithm.get_name() == name:
                return algorithm

        return None