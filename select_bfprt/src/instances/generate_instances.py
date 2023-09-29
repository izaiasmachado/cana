# Generate instances of the problem

import os
import sys
import random

from instances.config import SETTINGS

INSTANCES_PATH = SETTINGS["INSTANCES_PATH"]
INSTANCE_SIZE = SETTINGS["INSTANCE_SIZE"]
NUMBERS_EACH_LINE = SETTINGS["NUMBERS_EACH_LINE"]

def create_instance():
    instance, instance_size = generate_instance()
    instance_name = next_instance_name(instance_size)
    print(f"Creating instance {instance_name} with {instance_size} elements")
    write_instance(instance, instance_size, instance_name)

def generate_instance():
    instance = []
    instance_size = INSTANCE_SIZE

    # Gera uma lista preenchida com valores de 0 a instance_size - 1
    for i in range(instance_size):
        instance.append(i)
    
    # Embaralha a lista
    random.shuffle(instance)
    return instance, instance_size

def write_instance(instance, instance_size, instance_name):
    instance_string = instance_to_string(instance, instance_size)
    instance_path = os.path.join(INSTANCES_PATH, instance_name)

    with open(instance_path, "w") as f:
        for string_row in instance_string:
            if string_row:
                f.write(f"{string_row}\n")

def instance_to_string(instance, instance_size):
    instance_string = []
    numbes_each_line = NUMBERS_EACH_LINE
    total_lines = instance_size // NUMBERS_EACH_LINE

    instance_string.append(str(instance_size))

    # Escreve os elementos em linhas de tamanho NUMBERS_EACH_LINE
    for i in range(0, total_lines):
        line_elements = instance[i * numbes_each_line : (i + 1) * numbes_each_line]
        line_elements = [str(x) for x in line_elements]
        line_elements = ",".join(line_elements)

        instance_string.append(line_elements)

    return instance_string

def next_instance_name(instance_size):
    index = get_next_index()
    file_name = format_instance_filename(instance_size, index)
    return file_name

def get_next_index():
    instances_path = INSTANCES_PATH
    files = os.listdir(instances_path)

    max_index = -1

    for file_name in files:
        if file_name.endswith(".txt"):
            file_name = file_name.split("_")
            index = file_name[-1]
            index = index.split(".")[0]

            if index.isdigit():
                index = int(index)

                if index > max_index:
                    max_index = index

    return max_index + 1

def format_instance_filename(instance_size, index):
    file_name = f"instance_{instance_size}_{index}.txt"
    return file_name

if __name__ == "__main__":
    # for i in range(10000):
    create_instance()
