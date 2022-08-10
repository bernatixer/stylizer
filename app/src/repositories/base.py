from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from db.base_class import Base
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.core.logger import LOG
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, SchemaType]):
    def __init__(self, model: Type[ModelType], schema: SchemaType):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.schema = schema

    def get(self, db: Session, id: Any) -> Optional[SchemaType]:
        obj = db.query(self.model).filter(self.model.id == id).first()
        return self.model_to_schema(obj)

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[SchemaType]:
        results = db.query(self.model).offset(skip).limit(limit).all()
        return [self.model_to_schema(elem) for elem in results]

    def create(self, db: Session, *, obj_in: ModelType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[ModelType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return self.schema(**obj_data)

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        obj_in_data = jsonable_encoder(obj)
        return self.model(**obj_in_data)

    def model_to_schema(self, model: ModelType):
        obj_in_data = jsonable_encoder(model)
        return self.schema(**obj_in_data) if obj_in_data else None
