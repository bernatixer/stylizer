import logging
from pythonjsonlogger import jsonlogger


class Logger:
    def __init__(self):
        logHandler = logging.FileHandler(filename='/var/log/stylizer.log')
        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)

        appLogger = logging.getLogger()
        appLogger.addHandler(logHandler)
        appLogger.setLevel(logging.INFO)

        uviCornLogger = logging.getLogger("uvicorn.access")
        uviCornLogger.addHandler(logHandler)

        self.logger = appLogger

LOG = Logger().logger
