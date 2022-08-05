from db.base_class import Base
from sqlalchemy import Column, Integer, String


class Transformation(Base):
    id = Column(Integer, primary_key=True, index=True)
    style = Column(String(256), nullable=False)
