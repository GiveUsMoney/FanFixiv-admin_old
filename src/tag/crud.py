from sqlalchemy.orm import Session
from src.dto.tag import TagBody, TagUpdateBody

from src.entity.tag import Tag
from src.entity.user import User
from src.entity.notice import Notice
from src.entity.profile import Profile
from src.enum.tag_type import TagType

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


def tag_delete(db: Session, seq: int):
    result = db.query(Tag).filter(Tag.seq == seq).delete()
    db.commit()
    return result


def tag_update(db: Session, seq: int, body: TagUpdateBody):
    result = db.query(Tag).filter(Tag.seq == seq).update({k: v for k, v in body.__dict__.items() if v is not None})
    db.commit()
    return result


def status_update(db: Session, seq: int, allow: bool):
    result = db.query(Tag).filter(Tag.seq == seq).update({"status": allow})
    tag = db.query(Tag).filter(Tag.seq == seq).one()

    if allow:
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
    
    return result


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
