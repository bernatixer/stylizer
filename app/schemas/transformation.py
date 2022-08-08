from typing import Optional

from pydantic import BaseModel


class Transformation(BaseModel):
    style: str

    class Config:
        orm_mode = True
