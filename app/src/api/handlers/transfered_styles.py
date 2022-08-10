from src.repositories.transformation import transformations_repository
from src.core.logger import LOG


class TransferedStylesHandler:
    def handle(self, db):
        return transformations_repository.get_multi(db=db)


transfered_styles_handler = TransferedStylesHandler()
