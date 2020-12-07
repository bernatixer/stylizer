from config import settings


class Base:

    def __init__(self):
        self.STATIC_PATH = "{}/{}".format(settings.domain, settings.static_folder)
