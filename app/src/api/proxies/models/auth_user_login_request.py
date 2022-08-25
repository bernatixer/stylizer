from pydantic import BaseModel


class UserLoginRequest(BaseModel):
    email: str

    class Config:
        orm_mode = True
