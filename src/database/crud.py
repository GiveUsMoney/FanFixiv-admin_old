from . import model, schemas
from sqlalchemy.orm import Session


def get_user(db: Session, num: int):
    return db.query(model.UserTest).filter(model.UserTest.num == num).first()


def create_user(db: Session, num: schemas.UserTest):
    num = 5
    db_user = model.User(num=5)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
