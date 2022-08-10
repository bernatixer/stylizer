from src.styles.style_base import StyleBase


class Wave(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "wave"
        self.DISPLAY_NAME = "Wave"
        self.MODEL_PATH = "src/styles/wave/wave.pth"
        self.DISPLAY_IMAGE = "{}/wave.jpg".format(self.STATIC_PATH)
