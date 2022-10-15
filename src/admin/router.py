from fastapi import APIRouter, Depends, Cookie
from typing import Optional
from src.database import get_db

router = APIRouter(
    prefix="/admin",
)


#  jwt 토큰 검증
@router.get("/")
async def admin_conect(refresh_token: Optional[str] = Cookie(None)):
    return {"Cookle의 값": refresh_token}
