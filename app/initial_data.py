import logging

# from db.init_db import init_db
from db.session import SessionLocal

logger = logging.getLogger()

def init() -> None:
    db = SessionLocal()
    # init_db(db)


def main() -> None:
    logger = logging.getLogger()
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
