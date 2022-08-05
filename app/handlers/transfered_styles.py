from repositories.transformation import transformation


class TransferedStylesHandler:
    def handle(self, db):
        return transformation.get_multi(db=db)


transfered_styles_handler = TransferedStylesHandler()
