from src.repositories.entities.users import UsersEntity
from src.repositories.base import BaseRepository
from src.schemas.user import User
from sqlalchemy.orm import Session
from typing import Any, Optional
from fastapi.encoders import jsonable_encoder


class UsersRepository(BaseRepository[UsersEntity, User]):
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        obj = db.query(self.model).filter(self.model.email == email).first()
        return self.model_to_schema(obj)

users_repository = UsersRepository(UsersEntity, User)
