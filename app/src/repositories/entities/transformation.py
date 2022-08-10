from db.base_class import Base
from sqlalchemy import Column, Integer, String
from src.core.logger import LOG


class TransformationsEntity(Base):
    __tablename__ = 'transformations'

    id = Column(Integer, primary_key=True, index=True)
    style = Column(String(256), nullable=False)
