from styles.style_base import StyleBase


class Bayanihan(StyleBase):

    def __init__(self):
        super().__init__()
        self.NAME = "bayanihan"
        self.DISPLAY_NAME = "Bayanihan"
        self.MODEL_PATH = "styles/bayanihan/bayanihan.pth"
        self.DISPLAY_IMAGE = "{}/lazy.jpg".format(self.STATIC_PATH)
