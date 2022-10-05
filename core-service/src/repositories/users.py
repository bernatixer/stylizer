from src.core.logger import LOG
from src.repositories.entities.users import UsersEntity
from src.repositories.base import BaseRepository
from src.schemas.user import User
from sqlalchemy.orm import Session
from typing import Optional
from fastapi.encoders import jsonable_encoder


class UsersRepository(BaseRepository[UsersEntity, User]):
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        obj = db.query(self.model).filter(self.model.email == email).first()
        return self.model_to_schema(obj)

    def substract_user_tokens(self, db: Session, user_id: int, tokens: int):
        updated_objs = db.query(self.model).filter(self.model.id == user_id).update({self.model.tokens: self.model.tokens - tokens})
        db.commit()
        return updated_objs

    def add_user_tokens(self, db: Session, user_id: int, tokens: int):
        updated_objs = db.query(self.model).filter(self.model.id == user_id).update({self.model.tokens: self.model.tokens + tokens})
        db.commit()
        return updated_objs

users_repository = UsersRepository(UsersEntity, User)
