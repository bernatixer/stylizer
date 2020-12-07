from styles.style_base import StyleBase


class Lazy(StyleBase):

    def __init__(self):
        self.NAME = "lazy"
        self.DISPLAY_NAME = "Lazy"
        self.MODEL_PATH = "styles/lazy/lazy.pth"
        self.DISPLAY_IMAGE = "https://via.placeholder.com/300"
