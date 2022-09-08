from src.libs.style.models.style_base import StyleBase


class Ross(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "ross"
        self.DISPLAY_NAME = "Ross"
        self.MODEL_PATH = "src/libs/style/models/ross/ross.pth"
        self.DISPLAY_IMAGE = "{}/ross.jpg".format(self.STATIC_PATH)
