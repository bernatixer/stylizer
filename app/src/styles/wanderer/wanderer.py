from src.styles.style_base import StyleBase


class Wanderer(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "wanderer"
        self.DISPLAY_NAME = "Wanderer"
        self.MODEL_PATH = "src/styles/wanderer/wanderer.pth"
        self.DISPLAY_IMAGE = "{}/wanderer.jpg".format(self.STATIC_PATH)
