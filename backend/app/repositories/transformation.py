from repositories.base import CRUDBase
from entities.transformation import Transformation
from schemas.transformation import TransformationCreate, TransformationUpdate


class CRUDTransformation(CRUDBase[Transformation, TransformationCreate, TransformationUpdate]):
    pass

transformation = CRUDTransformation(Transformation)
