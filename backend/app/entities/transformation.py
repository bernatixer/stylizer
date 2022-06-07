from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Transformation(Base):
    id = Column(Integer, primary_key=True, index=True)
    style = Column(String(256), nullable=False)
