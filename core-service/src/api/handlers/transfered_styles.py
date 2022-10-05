from src.repositories.transformation import transformations_repository
from src.schemas.user import User


class TransferedStylesHandler:
    def handle(self, db, current_user: User):
        return transformations_repository.get_by_user(db=db, user_id=current_user.id)


transfered_styles_handler = TransferedStylesHandler()
