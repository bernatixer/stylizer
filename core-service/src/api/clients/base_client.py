import requests
from requests.exceptions import HTTPError
from src.api.exceptions.client_exception import ClientException
from src.core.logger import LOG


class BaseClient:

    def __init__(self, url: str) -> None:
        self.URL = url
        self.PROTOCOL = "http"
        self.BASE_URL = "{}://{}".format(self.PROTOCOL, self.URL)

    def _parse_call(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except HTTPError as e:
                LOG.error(str(e))
                raise ClientException(e.response.json()["detail"], e.response.status_code)
        return wrapper

    @_parse_call
    def get(self, path: str):
        response = requests.get(self.BASE_URL + path)
        response.raise_for_status()
        return {"data": response.json(), "status_code": response.status_code}

    @_parse_call
    def post(self, path: str, body, filename):
        response = requests.post(
            self.BASE_URL + path,
            files={"file": open(filename, "rb")},
            data=body
        )
        return {"data": response.content, "status_code": response.status_code}
