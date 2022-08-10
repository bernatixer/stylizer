from typing import Optional

from pydantic import BaseModel


class Users(BaseModel):
    id: int = None

    class Config:
        orm_mode = True
