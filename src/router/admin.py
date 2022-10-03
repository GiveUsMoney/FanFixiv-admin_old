from fastapi import APIRouter, Depends, Cookie
from typing import Optional


router = APIRouter(
    prefix="/admin",
)


@router.get("/")
async def admin_conect(refresh_token: Optional[str] = Cookie(None)):
    return {"Cookle의 값": refresh_token}
