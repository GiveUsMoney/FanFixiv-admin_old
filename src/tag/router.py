from fastapi import APIRouter, Depends

from src.auth import get_current_user
from src.database import get_db
from src.dto.tag import StatusUpdate, TagBody, TagUpdateBody, TagWithUser, TagInfo
from src.tag.crud import add_tag, get_tag_ex_list, get_tag_list, status_update, tag_delete, tag_update

router = APIRouter(prefix="/tag", tags=["tag"])

#  태그 목록 전송
@router.get("/list", response_model=list[TagWithUser])
async def tag_list_api(user = Depends(get_current_user), session = Depends(get_db)):
    return get_tag_list(session)

# 태그 추가
@router.post("/", response_model=TagInfo)
async def add_tag_api(body: TagBody, user = Depends(get_current_user), session = Depends(get_db)):
    return add_tag(session, body, user.seq)

# 태그 status 수정
@router.put("/status")
async def update_status(body: StatusUpdate, user = Depends(get_current_user), session = Depends(get_db)):
    status_update(session, body.seq, body.status)
    return {"message" : "success"}

# 태그 수정
@router.put("/{seq}")
async def tag_update_api(seq, body: TagUpdateBody, user = Depends(get_current_user), session = Depends(get_db)):
    tag_update(session, seq, body)
    return {"message" : "success"}

# 태그 삭제
@router.delete("/{seq}")
async def tag_delete_api(seq, user = Depends(get_current_user), session = Depends(get_db)):
    tag_delete(session, seq)
    return {"message" : "success"}

#  ex 태그 목록 전송
@router.get("/ex_list", response_model=list[TagInfo])
async def ex_tag_list_api(user = Depends(get_current_user), session = Depends(get_db)):
    return get_tag_ex_list(session)