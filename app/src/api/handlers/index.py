from src.core.config import settings

class IndexHandler:
    def __init__(self):
        self.SUCCESS_RESPONSE = {"status": "OKI"}

    def handle(self):
        return self.SUCCESS_RESPONSE
