from styles.style_base import StyleBase


class Testmodel(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "testmodel"
        self.DISPLAY_NAME = "Testmodel"
        self.MODEL_PATH = "styles/testmodel/testmodel.pth"
        self.DISPLAY_IMAGE = "{}/testmodel.jpg".format(self.STATIC_PATH)
