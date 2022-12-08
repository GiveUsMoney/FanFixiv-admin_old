from sqlalchemy.orm import Session
from src.dto.tag import TagBody, TagUpdateBody

from src.entity.tag import Tag
from src.entity.user import User
from src.enum.tag_type import TagType

# 일반 태그

def get_tag_list(db: Session, skip = 0, limit=10):
    return db.query(Tag, User) \
    .join(User, Tag.requester == User.seq, isouter=True) \
    .filter(Tag.type != TagType.EXTRA.value) \
    .offset(skip) \
    .limit(limit) \
    .all()

def add_tag(db: Session, tag: TagBody, user_seq: int):
    t = Tag(
        type=tag.type.value, 
        name=tag.name, 
        description=tag.description, 
        status=tag.status, 
        requester=user_seq
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

def tag_delete(db: Session, seq):
    db.query(Tag).filter(Tag.seq == seq).delete()
    db.commit()

def tag_update(db: Session, seq, body: TagUpdateBody):
    db.query(Tag).filter(Tag.seq == seq).update(body.__dict__)
    db.commit()

def status_update(db: Session, seq, status=True):
    db.query(Tag).filter(Tag.seq == seq).update({"status": status})
    db.commit()

# ex 태그

def get_tag_ex_list(db: Session, skip = 0, limit=10):
    return db.query(Tag) \
    .filter(Tag.type == TagType.EXTRA.value) \
    .offset(skip) \
    .limit(limit) \
    .all()