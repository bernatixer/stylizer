from styles.style_base import StyleBase


class Trippy(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "trippy"
        self.DISPLAY_NAME = "Trippy"
        self.MODEL_PATH = "styles/trippy/trippy.pth"
        self.DISPLAY_IMAGE = "{}/trippy.jpg".format(self.STATIC_PATH)
