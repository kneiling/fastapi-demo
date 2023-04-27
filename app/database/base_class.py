from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import as_declarative, declared_attr


class TimestampMixin:
    create_time = Column(DateTime(), default=datetime.utcnow, nullable=False)
    update_time = Column(DateTime(), default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)


class SoftDeleteMixin:
    delete_time = Column(DateTime(), index=True)
    

@as_declarative()
class Base(TimestampMixin, SoftDeleteMixin):
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
