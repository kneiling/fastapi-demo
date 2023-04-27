from datetime import datetime

from pydantic import BaseModel


class TimestampMixinModel(BaseModel):
    create_time: datetime
    update_time: datetime


class SoftDeleteMixinModel(BaseModel):
    delete_time: datetime | None
