from src.repositories.base import BaseRepository
from src.schemas.transformation import Transformation
from src.repositories.entities.transformation import TransformationsEntity


class TransformationsRepository(BaseRepository[TransformationsEntity, Transformation]):
    pass


transformations_repository = TransformationsRepository(TransformationsEntity, Transformation)
