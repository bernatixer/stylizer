import logging

from db.session import SessionLocal
from core.logger import LOG
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(LOG, logging.INFO),
    after=after_log(LOG, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        LOG.error(e)
        raise e


def main() -> None:
    LOG.info("Initializing service")
    init()
    LOG.info("Service finished initializing")


if __name__ == "__main__":
    main()
