from src.repositories.entities.users import UsersEntity
from src.repositories.base import BaseRepository
from src.schemas.users import Users


class UsersRepository(BaseRepository[UsersEntity, Users]):
    pass


users_repository = UsersRepository(UsersEntity, Users)
