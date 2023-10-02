from algorithms import select_bfprt_factory
from execution import AlgorithmCollection

def create_algorithm_collection():
    algorithm_collection = AlgorithmCollection()
    partition_sizes = [3, 5, 7, 9, 11]

    for r in partition_sizes:
        algorithm_collection.add_algorithm(f"Select BFPRT - r = {r}", select_bfprt_factory(r))

    return algorithm_collection