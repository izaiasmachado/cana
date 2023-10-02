import os
import sys
import random

def generate_instance(instance_size):
    instance = []

    # Gera uma lista preenchida com valores de 0 a instance_size - 1
    for i in range(instance_size):
        instance.append(i)
    
    # Embaralha a lista
    random.shuffle(instance)
    return instance, instance_size
