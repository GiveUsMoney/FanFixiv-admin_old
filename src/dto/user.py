
from src.dto.base import BaseInfo

from pydantic import EmailStr


class UserInfo(BaseInfo):
    email: EmailStr
    is_social: bool
