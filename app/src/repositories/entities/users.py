from db.base_class import Base
from sqlalchemy import Column, Integer, String


class UsersEntity(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), nullable=False)
    tokens = Column(Integer, nullable=False)
