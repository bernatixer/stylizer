from src.repositories.base import BaseRepository
from src.schemas.transformation import Transformation
from src.repositories.entities.transformation import TransformationsEntity
from sqlalchemy.orm import Session
from typing import Optional


class TransformationsRepository(BaseRepository[TransformationsEntity, Transformation]):
    def get_by_user(self, db: Session, user_id: int) -> Optional[Transformation]:
        obj = db.query(self.model).filter(self.model.user == user_id).first()
        return self.model_to_schema(obj)


transformations_repository = TransformationsRepository(TransformationsEntity, Transformation)
