import os
import time
import multiprocessing
import signal
from utils import logger, format_number

from algorithms import select_bfprt_factory
from instances import create_instance, get_instances_folder_path, get_instances_quantity

from execution.execution import manual_execution

processes = []
pids = []

def worker(worker_id, instance_size, instances_quantity, output_file_name, pid_list):
    pid = os.getpid()
    pid_list.append(pid)
    os.system(f"python src/worker.py {worker_id} {instance_size} {instances_quantity} {output_file_name}")

def execute_instances_screen():
    num_processes = int(input('> Digite a quantidade de processos paralelos que deseja utilizar: '))
    instance_size = int(input('> Digite o tamanho das instâncias que deseja criar: '))
    instances_quantity = int(input('> Digite a quantidade de instâncias que deseja criar: '))

    if num_processes <= 0:
        print("[ERRO] O número de processos deve ser maior que 0!")
        return

    execute_instances(num_processes, instance_size, instances_quantity)

def execute_instances(num_processes=3, instance_size=100000, instances_quantity=1):
    instances_per_process = instances_quantity // num_processes
    output_file_name = f'{instances_quantity}_{instance_size}_{time.strftime("%Y%m%d-%H%M%S")}.csv'

    for worker_id in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(worker_id, instance_size, instances_per_process, output_file_name, pids))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

def execute_one_instance_screen():
    instance_size = int(input('> Digite o tamanho da instância que você vai digitar: '))
    input_values = list(map(int, input('> Digite (ou cole) os valores da instância separados por vírgula (,): ').split(',')))

    while len(input_values) < instance_size:
        additional_input_values = list(map(int, input(f'> Digite (ou cole) os outros {instance_size - len(input_values)} valores: ').split(',')))
        input_values.extend(additional_input_values)

    instance = input_values[:instance_size]

    manual_execution(instance)

    input_option = input('> Deseja executar outra instância? [S/n]: ')

    if input_option.lower() == 's' or input_option.lower() == 'S':
        execute_one_instance_screen()

def main_menu():
    try:
        while True:
            print("===== Select BFPRT =====")
            print("1 - Executar várias instâncias")
            print("2 - Executar uma instância")
            print("0 - Sair")

            option = int(input("> Opção: "))

            if option == 1:
                execute_instances_screen()
            elif option == 2:
                execute_one_instance_screen()
            elif option == 0:
                break
            else:
                print("[ERRO] Opção Inválida!")

    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

def signal_handler(signum, frame):
    logger.info(f"Recebido sinal {signum}. Terminando os processos filhos...")

    for process in processes:
        process.terminate()  # Termine os processos filhos
    for process in processes:
        process.join()  # Aguarde o término do processo filho

    logger.info("Processos filhos terminados. Encerrando o programa principal.")
    exit(0)

if __name__ == "__main__":
    main_menu()
