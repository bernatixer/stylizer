from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    email: str
    tokens: int = 100

    class Config:
        orm_mode = True
