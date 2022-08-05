import logging
from pythonjsonlogger import jsonlogger


class Logger:
    def __init__(self):
        setup_log()
        map_levelname_to_status()

        self.logger = appLogger

    def setup_log(self):
    loggers = [
        logging.getLogger("uvicorn.access"),
        logging.getLogger("uvicorn.error"),
        logging.getLogger("uvicorn"),
        logging.getLogger(),
    ]
    for logger in loggers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
        logger.level = logging.INFO
        logHandler = logging.FileHandler(filename='/var/log/stylizer.log')
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(name)s %(message)s"
        )
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)

    def map_levelname_to_status() -> None:
        oldFactory = logging.getLogRecordFactory()

        def record_factory(*args: str, **kwargs: str) -> logging.LogRecord:
            record = oldFactory(*args, **kwargs)
            record.status = record.levelname
            return record

        logging.setLogRecordFactory(record_factory)


LOG = Logger().logger
