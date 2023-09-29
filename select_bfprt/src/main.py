import os
import multiprocessing
import signal
from utils import logger, format_number

from algorithms import select_bfprt_factory
from instances import create_instance, get_instances_folder_path, get_instances_quantity

NUM_PROCESSES = 3

processes = []
pids = []

def worker(start_instance_id, end_instance_id, pid_list):
    pid = os.getpid()
    pid_list.append(pid)  # Adicione o PID à lista
    os.system(f"python src/worker.py {start_instance_id} {end_instance_id}")

def execute_instances_screen():
    num_processes = int(input('> Digite a quantidade de processos paralelos que deseja utilizar: '))

    if num_processes <= 0:
        print("[ERRO] O número de processos deve ser maior que 0!")
        return

    execute_instances(num_processes)

def execute_instances(num_processes=NUM_PROCESSES):
    total_instances = get_instances_quantity()
    instances_per_process = total_instances // num_processes

    for i in range(NUM_PROCESSES):
        start_instance_id = i * instances_per_process
        end_instance_id = (i + 1) * instances_per_process - 1

        process = multiprocessing.Process(target=worker, args=(start_instance_id, end_instance_id, pids))
        process.start()
        processes.append(process)

    remainder = total_instances % NUM_PROCESSES

    if remainder > 0:
        last_process_start_instance_id = NUM_PROCESSES * instances_per_process
        last_process_end_instance_id = last_process_start_instance_id + remainder - 1

        process = multiprocessing.Process(target=worker, args=(last_process_start_instance_id, last_process_end_instance_id, pids))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

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
    try:
        while True:
            print("===== Select BFPRT =====")
            print("1 - Executar algoritmos para as Instâncias")
            print("2 - Criar Instâncias")
            print("3 - Limpar Instâncias")
            print("0 - Sair")

            option = int(input("> Opção: "))

            if option == 1:
                execute_instances_screen()
            elif option == 2:
                create_instances()
            elif option == 3:
                clear_instances()
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
