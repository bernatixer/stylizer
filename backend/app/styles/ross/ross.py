from styles.style_base import StyleBase


class Ross(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "ross"
        self.DISPLAY_NAME = "Ross"
        self.MODEL_PATH = "styles/ross/ross.pth"
        self.DISPLAY_IMAGE = "{}/ross.jpg".format(self.STATIC_PATH)
