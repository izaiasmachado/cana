import os
import logging

# Obtenha o PID do processo
pid = os.getpid()

# Configure o formato do log para incluir o PID
FORMAT = f"%(asctime)s [%(levelname)s]: [PID:{pid}] %(message)s (%(filename)s:%(lineno)d)"

# Configure o logger com o formato personalizado
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# Salve o log em um arquivo
file_handler = logging.FileHandler('data/logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)

