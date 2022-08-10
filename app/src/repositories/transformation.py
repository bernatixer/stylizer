from src.repositories.base import BaseRepository
from src.schemas.transformation import Transformations
from src.repositories.entities.transformation import TransformationsEntity


class TransformationsRepository(BaseRepository[TransformationsEntity, Transformations]):
    pass


transformations_repository = TransformationsRepository(TransformationsEntity, Transformations)
