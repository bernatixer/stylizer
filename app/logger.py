import logging
from datetime import datetime

from infrastructure.config import settings
from pythonjsonlogger import jsonlogger


class Logger:
    def __init__(self):
        self.setup_logs()
        self.logger = logging.getLogger()

    def setup_logs(self):
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

            logHandler = None
            if settings.isLocal():
                logHandler = logging.StreamHandler()
            else:
                logHandler = logging.FileHandler(filename="/var/log/stylizer.log")

            formatter = LogJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')

            logHandler.setFormatter(formatter)
            logger.addHandler(logHandler)


class LogJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(LogJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

        log_record['env'] = settings.ENVIRONMENT


LOG = Logger().logger
