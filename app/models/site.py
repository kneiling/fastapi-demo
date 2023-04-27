from sqlalchemy import Column, Integer, String

from app.database.base_class import Base


class Site(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    multiplier = Column(Integer, nullable=False)
