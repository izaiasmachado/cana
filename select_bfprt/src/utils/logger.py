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
