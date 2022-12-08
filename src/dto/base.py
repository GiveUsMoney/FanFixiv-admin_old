
from pydantic import BaseModel
from datetime import datetime

class CBase(BaseModel):
    class Config:
        orm_mode = True

class BaseInfo(CBase):
    seq: int
    created_at: datetime
    updated_at: datetime