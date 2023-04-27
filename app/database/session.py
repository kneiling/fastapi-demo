from contextvars import ContextVar

import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session

from app.core import settings

def get_db_url():
    return settings.SQLALCHEMY_DATABASE_URL

engine = sqlalchemy.create_engine(get_db_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
