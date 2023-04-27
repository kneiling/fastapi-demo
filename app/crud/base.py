from datetime import datetime
from typing import Generic, TypeVar, Type, Optional, Dict, Any, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_many(self, db: Session, limit: int = 100) -> list[ModelType]:
        return db.query(self.model).filter(self.model.delete_time.is_(None)).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return db_obj

    
    def update(self, db: Session, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
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
        return db_obj
        

    def delete(self, db: Session, id: int) -> None:
        db_obj = db.query(self.model).get(id)
        
        if hasattr(db_obj, "delete_time"):
            db_obj.delete_time = datetime.utcnow()
            db.add(db_obj)
        else:
            db.delete(db_obj)
            
        db.commit()

    def restore(self):
        self.delete_time = None
