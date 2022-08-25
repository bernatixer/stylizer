from pydantic import BaseModel


class User(BaseModel):
    email: str
    tokens: int

    class Config:
        orm_mode = True
