from styles.styles import Styles


class StylesListHandler:
    def __init__(self, styles: Styles):
        self.styles = styles

    def handle(self):
        return {"styles": self.styles.STYLES_REPRESENTATIONS}
