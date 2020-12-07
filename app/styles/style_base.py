from base import Base


class StyleBase(Base):

    def __init__(self):
        super().__init__()


    def get_representation(self):
        return {
            "name": self.NAME,
            "display_name": self.DISPLAY_NAME,
            "display_image": self.DISPLAY_IMAGE
        }
