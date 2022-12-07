from fastapi import APIRouter, Depends
from src.auth import get_current_user

router = APIRouter(prefix="/admin", tags=["admin"])

#  jwt 토큰 검증
@router.get("/test")
async def admin_conect(access_token = Depends(get_current_user)):
    return {"user_info": access_token}