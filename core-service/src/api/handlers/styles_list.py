from src.api.clients.inference_client import InferenceClient


class StylesListHandler:
    def __init__(self):
        self.INFERENCE_CLIENT = InferenceClient()

    def handle(self):
        return self.INFERENCE_CLIENT.get_styles()


styles_list_handler = StylesListHandler()
