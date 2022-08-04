
# from db.init_db import init_db
from db.session import SessionLocal
from logger import LOG


def init() -> None:
    db = SessionLocal()
    # init_db(db)


def main() -> None:
    LOG.info("Creating initial data")
    init()
    LOG.info("Initial data created")


if __name__ == "__main__":
    main()
