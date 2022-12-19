from fastapi import APIRouter, Depends, Query, HTTPException, status

from src.auth import get_current_user
from src.database import get_db
from src.dto.tag import TagBody, TagUpdateBody, TagWithUser, TagInfo
from src.tag.crud import (
    add_tag,
    get_tag_ex_list,
    get_tag_list,
    status_update,
    tag_delete,
    tag_update,
)

router = APIRouter(prefix="/tag", tags=["tag"])

#  태그 목록 전송
@router.get("/list", response_model=list[TagWithUser])
async def tag_list_api(
    skip: int = Query(default=0),
    limit: int = Query(default=10),
    user=Depends(get_current_user),
    session=Depends(get_db),
):
    return get_tag_list(session, skip=skip, limit=limit)


# 태그 추가
@router.post("", response_model=TagInfo)
async def add_tag_api(
    body: TagBody, user=Depends(get_current_user), session=Depends(get_db)
):
    return add_tag(session, body, user.seq)


# 태그 status 수정
@router.put("/status/{seq}")
async def update_status(
    seq: int, status: bool, user=Depends(get_current_user), session=Depends(get_db)
):
    return status_update(session, seq, status)


# 태그 수정
@router.put("/{seq}")
async def tag_update_api(
    seq: int,
    body: TagUpdateBody,
    user=Depends(get_current_user),
    session=Depends(get_db),
):
    return tag_update(session, seq, body)


# 태그 삭제
@router.delete("/{seq}")
async def tag_delete_api(
    seq: int, user=Depends(get_current_user), session=Depends(get_db)
):
    return tag_delete(session, seq)


#  ex 태그 목록 전송
@router.get("/ex_list", response_model=list[TagInfo])
async def ex_tag_list_api(
    skip: int = Query(default=0),
    limit: int = Query(default=10),
    user=Depends(get_current_user),
    session=Depends(get_db),
):
    return get_tag_ex_list(session, skip=skip, limit=limit)
