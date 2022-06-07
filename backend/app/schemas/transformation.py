from typing import Optional

from pydantic import BaseModel


# Shared properties
class TransformationBase(BaseModel):
    style: Optional[str] = None


# Properties to receive on Transformation creation
class TransformationCreate(TransformationBase):
    style: str


# Properties to receive on Transformation update
class TransformationUpdate(TransformationBase):
    pass


# Properties shared by models stored in DB
class TransformationInDBBase(TransformationBase):
    id: int
    style: str

    class Config:
        orm_mode = True


# Properties to return to client
class Transformation(TransformationInDBBase):
    pass


# Properties properties stored in DB
class TransformationInDB(TransformationInDBBase):
    pass
