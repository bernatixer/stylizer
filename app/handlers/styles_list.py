from styles.styles import styles_class


class StylesListHandler:
    def __init__(self):
        pass

    def handle(self, db):
        return {"styles": styles_class.STYLES_REPRESENTATIONS}

styles_list_handler = StylesListHandler()
