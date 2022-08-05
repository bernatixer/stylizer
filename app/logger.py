import logging
from datetime import datetime

from config import settings
from pythonjsonlogger import jsonlogger


class Logger:
    def __init__(self):
        self.setup_log()
        # self.personalize_logs()

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


            logHandler = None
            if settings.isLocal():
                logHandler = logging.StreamHandler()
            else:
                logHandler = logging.FileHandler(filename="/var/log/stylizer.log")

            # formatter = jsonlogger.JsonFormatter("%(name)s %(message)s")
            formatter = LogJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')

            logHandler.setFormatter(formatter)
            logger.addHandler(logHandler)

    def personalize_logs(self) -> None:
        oldFactory = logging.getLogRecordFactory()

        def record_factory(*args: str, **kwargs: str) -> logging.LogRecord:
            record = oldFactory(*args, **kwargs)
            record.level = record.levelname
            record.env = settings.ENVIRONMENT
            record.timestamp = record.created
            # record.name = record.name
            return record

        logging.setLogRecordFactory(record_factory)


class LogJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(LogJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

        log_record['env'] = settings.ENVIRONMENT


LOG = Logger().logger
