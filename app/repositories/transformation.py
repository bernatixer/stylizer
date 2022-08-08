from repositories.base import BaseRepository
from schemas.transformation import Transformation
from repositories.entities.transformation import TransformationEntity


class TransformationRepository(BaseRepository[TransformationEntity, Transformation]):
    pass


transformation_repository = TransformationRepository(TransformationEntity, Transformation)
