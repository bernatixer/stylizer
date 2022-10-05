from src.libs.style.models.style_base import StyleBase


class Wave(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "wave"
        self.DISPLAY_NAME = "Wave"
        self.MODEL_PATH = "src/libs/style/models/wave/wave.pth"
        self.DISPLAY_IMAGE = "{}/wave.jpg".format(self.STATIC_PATH)
