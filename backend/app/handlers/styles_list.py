from styles.styles import styles_class
import logging


logger = logging.getLogger(__name__)


class StylesListHandler:
    def __init__(self):
        pass

    def handle(self):
        return {"styles": styles_class.STYLES_REPRESENTATIONS}

styles_list_handler = StylesListHandler()
