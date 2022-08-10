from src.styles.style_base import StyleBase


class Mosaic(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "mosaic"
        self.DISPLAY_NAME = "Mosaic"
        self.MODEL_PATH = "src/styles/mosaic/mosaic.pth"
        self.DISPLAY_IMAGE = "{}/mosaic.jpg".format(self.STATIC_PATH)
