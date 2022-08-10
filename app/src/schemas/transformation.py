from typing import Optional

from pydantic import BaseModel


class Transformations(BaseModel):
    id: int = None
    style: str

    class Config:
        orm_mode = True
