from fastapi import HTTPException


class InsufficientTokensException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=400, detail="Insufficient tokens")
