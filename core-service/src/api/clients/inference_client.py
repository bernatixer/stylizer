from src.api.clients.base_client import BaseClient


class InferenceClient(BaseClient):

    INFERENCE_SERVICE_URL = "inference-service"
    STYLES_URL_PATH = "/api/styles"
    STYLYZE_URL_PATH = "/api/styles/transform"
    
    def __init__(self) -> None:
        super().__init__(self.INFERENCE_SERVICE_URL)

    def get_styles(self):
        response = self.get(self.STYLES_URL_PATH)
        return response["data"]

    def stylize(self, filename):
        response = self.post(
            self.STYLYZE_URL_PATH,
            body={"style": "starry"},
            filename=filename
        )
        return response["data"]
