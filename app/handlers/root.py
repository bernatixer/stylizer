class RootHandler:

    def __init__(self):
        self.SUCCESS_RESPONSE = { "status": "OK" }


    def handle(self):
        return self.SUCCESS_RESPONSE
