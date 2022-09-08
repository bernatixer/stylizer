from src.libs.style.models.style_base import StyleBase


class Testmodel(StyleBase):
    def __init__(self):
        super().__init__()
        self.NAME = "testmodel"
        self.DISPLAY_NAME = "Testmodel"
        self.MODEL_PATH = "src/libs/style/models/testmodel/testmodel.pth"
        self.DISPLAY_IMAGE = "{}/testmodel.jpg".format(self.STATIC_PATH)
