from src.core.config import settings


class StyleBase:
    def __init__(self):
        self.STATIC_PATH = "{}/{}".format(settings.DOMAIN, settings.STATIC_FOLDER)

    def get_representation(self):
        return {
            "name": self.NAME,
            "display_name": self.DISPLAY_NAME,
            "display_image": self.DISPLAY_IMAGE,
        }
