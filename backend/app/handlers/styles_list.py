from styles.styles import styles_class
import logging


logger = logging.getLogger(__name__)


class StylesListHandler:
    def __init__(self):
        pass

    def handle(self, db):
        results = db.execute("SELECT 1")
        print([row[0] for row in results])
        return {"styles": styles_class.STYLES_REPRESENTATIONS}

styles_list_handler = StylesListHandler()
