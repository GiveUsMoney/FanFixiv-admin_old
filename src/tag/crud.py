from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.dto.tag import TagBody, TagUpdateBody

from src.entity.tag import Tag
from src.entity.user import User
from src.entity.notice import Notice
from src.entity.profile import Profile
from src.enum.tag_type import TagType

from src.dto.result import Result
from src.exception.exception import BadRequestException

# 일반 태그


def get_tag_list(db: Session, skip=0, limit=10):
    # TODO 검색 기능 추가 필요...
    return (
        db.query(Tag, User)
        .join(User, Tag.requester == User.seq, isouter=True)
        .filter(Tag.type != TagType.EXTRA.value)
        .order_by(Tag.seq.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def add_tag(db: Session, tag: TagBody, user_seq: int):
    t = Tag(
        type=tag.type.value,
        name=tag.name,
        description=tag.description,
        status=tag.status,
        requester=user_seq,
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


def tag_delete(db: Session, seq: int) -> Result:
    result = db.query(Tag).filter(Tag.seq == seq).delete()
    if result == 0:
        return BadRequestException(detail="존재하지 않는 태그입니다.")
    db.commit()
    return Result(status=200, detail="성공적으로 삭제되었습니다.") 



def tag_update(db: Session, seq: int, body: TagUpdateBody) -> Result:
    if not any([v for v in body.__dict__.values()]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="수정할 데이터가 없습니다."
        )
    result = db.query(Tag).filter(Tag.seq == seq).update({k: v for k, v in body.__dict__.items() if v is not None})
    if result == 0:
        return BadRequestException(detail="존재하지 않는 태그입니다.")
    db.commit()
    return Result(status=200, detail="성공적으로 수정되었습니다.") 


def status_update(db: Session, seq: int, status: bool):
    ori_stauts = db.query(Tag.status).filter(Tag.seq == seq).scalar()

    if ori_stauts != status:
        result = db.query(Tag).filter(Tag.seq == seq).update({"status": status})
        
        if result == 0:
            return BadRequestException(detail="존재하지 않는 태그입니다.")

        tag = db.query(Tag).filter(Tag.seq == seq).one()

        if status:
            user = db.query(User.seq, Profile.nickname) \
                .join(Profile, Profile.seq == User.profile_seq) \
                .filter(User.seq == tag.requester).one()
            notice = Notice(
                content=f"{user.nickname}님이 요청하신 태그({tag.name})의 사용이 허가 되었습니다.",
                to_all=False,
                user_seq=tag.requester,
            )
            db.add(notice)
        db.commit()
    
    if status:
        return Result(status=200, detail="성공적으로 사용이 허가되었습니다.")
    else:
        return Result(status=200, detail="성공적으로 사용이 중지되었습니다.")



# ex 태그


def get_tag_ex_list(db: Session, skip=0, limit=10):
    # TODO 검색 기능 추가 필요...
    return (
        db.query(Tag)
        .filter(Tag.type == TagType.EXTRA.value)
        .order_by(Tag.seq.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
