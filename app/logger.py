import logging

from config import settings
from pythonjsonlogger import jsonlogger


class Logger:
    def __init__(self):
        self.setup_log()
        self.personalize_logs()

        self.logger = logging.getLogger()

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

            logger.info(f"Env: {settings.ENVIRONMENT}")
            logHandler = logging.FileHandler(filename="/var/log/stylizer.log")
            # logHandler = logging.StreamHandler()
            # if not settings.isLocal:
            #     logHandler = logging.FileHandler(filename="/var/log/stylizer.log")

            formatter = jsonlogger.JsonFormatter(
                "%(asctime)s %(name)s %(message)s"
            )
            logHandler.setFormatter(formatter)
            logger.addHandler(logHandler)

    def personalize_logs(self) -> None:
        oldFactory = logging.getLogRecordFactory()

        def record_factory(*args: str, **kwargs: str) -> logging.LogRecord:
            record = oldFactory(*args, **kwargs)
            record.level = record.levelname
            record.env = settings.ENVIRONMENT
            return record

        logging.setLogRecordFactory(record_factory)


LOG = Logger().logger
