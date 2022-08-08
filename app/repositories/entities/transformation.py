from db.base_class import Base
from sqlalchemy import Column, Integer, String
from core.logger import LOG


class TransformationEntity(Base):
    __tablename__ = 'transformation'

    id = Column(Integer, primary_key=True, index=True)
    style = Column(String(256), nullable=False)
