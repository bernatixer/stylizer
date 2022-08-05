from entities.transformation import Transformation
from repositories.base import CRUDBase
from schemas.transformation import TransformationCreate, TransformationUpdate


class CRUDTransformation(
    CRUDBase[Transformation, TransformationCreate, TransformationUpdate]
):
    pass


transformation = CRUDTransformation(Transformation)
