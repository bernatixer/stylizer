from src.styles.style_base import StyleBase


class Starry(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "starry"
        self.DISPLAY_NAME = "Starry"
        self.MODEL_PATH = "src/styles/starry/starry.pth"
        self.DISPLAY_IMAGE = "{}/starry.jpg".format(self.STATIC_PATH)
