from pydantic import BaseModel

from app.schemas.base import TimestampMixinModel, SoftDeleteMixinModel


# properties required to create
class SiteCreate(BaseModel):
    name: str
    multiplier: int


# properties required for update
class SiteUpdate(BaseModel):
    multiplier: int


# properties storted in db
class SiteInDB(TimestampMixinModel, SoftDeleteMixinModel):
    id: int
    name: str
    multiplier: int

    class Config:
        orm_mode = True


# properties returned for read requests
class Site(SiteInDB):
    pass
