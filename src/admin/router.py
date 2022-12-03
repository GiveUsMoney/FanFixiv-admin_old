from fastapi import APIRouter, Depends, Cookie, Header, HTTPException, Response, status
from typing import Optional
from src.database import get_db
from src.config import RabiitHandler

from src.admin.model import ActionLog
from src.admin import schema

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
    # dependencies =
)

# header 점검
def get_token_header(token: Optional[str] = Header(...)):
    # 나중에 jwt를 검증할 API를 넣어야함.
    # 만약 jwt 검증이 에러가 발생할 시 분기를 나눠야 함.
    print("get_token_header가 실행됨.")
    if token is None:
        raise HTTPException(status_code=400, detail="JWT 토큰이 없습니다.")
    return token


#  jwt 토큰 검증
@router.get("/")
async def admin_conect(access_token: get_token_header = Depends()):
    return {"access token 의 값": access_token}


# mq push
@router.get("/mq")
def mq_push():
    mq = RabiitHandler()
    mq.push("hello", "hello world")
    mq.get("hello")
    print(mq.get("hello"))
    return "Good"


# Log Search
@router.get("/log")
def log_search(q: schema.LogSearch = Depends(), db: get_db = Depends()):
    # user로 검색할 때
    if q.user:
        print("user")

    # action으로 검색할 때
    else:
        print("action")
    return "Hello"
