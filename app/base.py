from infrastructure.config import settings


class Base:
    def __init__(self):
        self.STATIC_PATH = "{}/{}".format(settings.DOMAIN, settings.STATIC_FOLDER)
