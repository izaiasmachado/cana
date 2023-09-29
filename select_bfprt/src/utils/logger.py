import logging

FORMAT = "%(asctime)s [%(levelname)s]: %(message)s (%(filename)s:%(lineno)d)"

logging.basicConfig(format=FORMAT)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
