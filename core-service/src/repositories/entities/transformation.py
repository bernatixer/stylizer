from db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class TransformationsEntity(Base):
    __tablename__ = 'transformations'

    id = Column(Integer, primary_key=True, index=True)
    style = Column(String(256), nullable=False)
    user = Column(Integer, ForeignKey("users.id"))
