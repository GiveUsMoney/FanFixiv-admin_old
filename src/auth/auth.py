from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from pydantic import BaseModel

from src.config import config
from src.database import get_db
from src.entity.role import Role
from src.entity.user import User

SECRET_KEY = config.SECRET
ALGORITHM = "HS256"

class TokenHeader(BaseModel):
    scheme: str
    credentials: str

security = HTTPBearer() 

async def get_current_user(token: TokenHeader = Depends(security)):
    session = get_db().send(None)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        seq: int = int(payload.get("sub"))
        if seq is None:
            raise credentials_exception
    except (JWTError, ValueError):
        raise credentials_exception
    user = session.query(User) \
                .join(Role) \
                .filter(User.seq == seq, Role.role == 'ROLE_ADMIN').one()
    if user is None:
        raise credentials_exception
    return user