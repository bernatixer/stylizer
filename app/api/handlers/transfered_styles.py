from repositories.transformation import transformation_repository
from core.logger import LOG


class TransferedStylesHandler:
    def handle(self, db):
        return transformation_repository.get_multi(db=db)


transfered_styles_handler = TransferedStylesHandler()
