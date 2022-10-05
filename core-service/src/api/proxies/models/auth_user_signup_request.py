from pydantic import BaseModel


class UserSignupRequest(BaseModel):
    email: str

    class Config:
        orm_mode = True
