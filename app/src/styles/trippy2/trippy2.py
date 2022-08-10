from src.styles.style_base import StyleBase


class Trippy2(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "trippy2"
        self.DISPLAY_NAME = "Trippy2"
        self.MODEL_PATH = "src/styles/trippy2/trippy2.pth"
        self.DISPLAY_IMAGE = "{}/trippy2.jpg".format(self.STATIC_PATH)
