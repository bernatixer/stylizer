from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    email: str
    tokens: int

    class Config:
        orm_mode = True
