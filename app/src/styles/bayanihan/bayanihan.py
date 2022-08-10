from src.styles.style_base import StyleBase


class Bayanihan(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "bayanihan"
        self.DISPLAY_NAME = "Bayanihan"
        self.MODEL_PATH = "src/styles/bayanihan/bayanihan.pth"
        self.DISPLAY_IMAGE = "{}/bayanihan.jpg".format(self.STATIC_PATH)
