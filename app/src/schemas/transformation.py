from typing import Optional

from pydantic import BaseModel


class Transformation(BaseModel):
    id: int = None
    style: str

    class Config:
        orm_mode = True
