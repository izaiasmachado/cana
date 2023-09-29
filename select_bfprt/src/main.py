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

def execute_instances():
    algorithm_collection = create_algorithm_collection()
    dataset_group = create_dataset_group()
    
    executor = SelectBFPRTInstanceExecutor(algorithm_collection, dataset_group)
    executor.execute()

def create_instances():
    instances_amount = int(input("> Digite a quantidade de instâncias que deseja criar: "))

    for _ in range(instances_amount):
        create_instance()

def clear_instances():
    instances_folder_path = get_instances_folder_path()
    instances_amount = len(os.listdir(instances_folder_path))

    flag_delete = input(f"> Tem certeza que deseja deletar {format_number(instances_amount)} instâncias? [S/n]: ")
    should_delete = flag_delete == "S" or flag_delete == "s"

    if should_delete:
        os.system(f"rm -rf {instances_folder_path}/*")
        print("Instâncias deletadas com sucesso!")

def main_menu():
    while True:
        print("===== Select BFPRT =====")
        print("1 - Executar algoritmos para as Instâncias")
        print("2 - Crias Instâncias")
        print("3 - Limpar Instâncias")
        print("0 - Sair")

        option = int(input("> Opção: "))

        if option == 1:
            execute_instances()
        elif option == 2:
            create_instances()
        elif option == 3:
            clear_instances()
        elif option == 0:
            break
        else:
            print("[ERRO] Opção Inválida!")

if __name__ == "__main__":
    main_menu()
