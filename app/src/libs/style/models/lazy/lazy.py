from src.libs.style.models.style_base import StyleBase


class Lazy(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "lazy"
        self.DISPLAY_NAME = "Lazy"
        self.MODEL_PATH = "src/libs/style/models/lazy/lazy.pth"
        self.DISPLAY_IMAGE = "{}/lazy.jpg".format(self.STATIC_PATH)