from pydantic import BaseModel, Field
from typing import Optional


class LogSearch(BaseModel):
    user: Optional[str] = None
    action: Optional[str] = None
