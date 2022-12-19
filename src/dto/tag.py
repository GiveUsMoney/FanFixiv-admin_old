
from typing import Optional, Union
from pydantic import BaseModel
from src.dto.base import BaseInfo, CBase
from src.dto.user import UserInfo

from src.enum.tag_type import TagType

class StatusUpdate(BaseModel):
    status: bool = True

class TagBody(BaseModel):
    type: TagType
    description: str
    status: bool
    name: str
    is_adult: bool


class TagUpdateBody(BaseModel):
    description: Optional[str]
    status: Optional[bool]
    name: Optional[str]
    is_adult: Optional[bool]

class TagInfo(BaseInfo, TagBody):
    pass

class TagWithUser(CBase):
    Tag: TagInfo
    User: Union[UserInfo, None]