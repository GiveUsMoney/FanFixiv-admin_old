
from pydantic import BaseModel

class Result(BaseModel):
    status: int
    detail: str