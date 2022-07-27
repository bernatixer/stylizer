import logging

# from db.init_db import init_db
from db.session import SessionLocal

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

from pythonjsonlogger import jsonlogger
logger = logging.getLogger()

logHandler = logging.FileHandler(filename='/var/log/stylizer_logs.json')
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)


def init() -> None:
    db = SessionLocal()
    # init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
