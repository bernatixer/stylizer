import logging
from pythonjsonlogger import jsonlogger


class Logger:
    logHandler = logging.FileHandler(filename='/var/log/stylizer.log')
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)

LOG = logging.getLogger()
