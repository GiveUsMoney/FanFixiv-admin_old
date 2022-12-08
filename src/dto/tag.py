
from typing import Union
from pydantic import BaseModel
from src.dto.base import BaseInfo, CBase
from src.dto.user import UserInfo

from src.enum.tag_type import TagType

class StatusUpdate(BaseModel):
    seq: int
    status: bool = True

class TagBody(BaseModel):
    type: TagType
    description: str
    status: bool
    name: str
    is_adult: bool


class TagUpdateBody(BaseModel):
    description: Union[str, None]
    status: Union[bool, None]
    name: Union[str, None]
    is_adult: Union[bool, None]

class TagInfo(BaseInfo, TagBody):
    pass

class TagWithUser(CBase):
    Tag: TagInfo
    User: Union[UserInfo, None]