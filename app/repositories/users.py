from repositories.entities.users import UsersEntity
from repositories.base import BaseRepository
from repositories.schemas.users import Users


class UsersRepository(BaseRepository[UsersEntity, Users]):
    pass


users_repository = UsersRepository(UsersEntity, Users)
