from sqlalchemy import Integer, Column
from .database import base


class UserTest(base):
    __tablename__ = "user_test"
    num: int = Column(Integer, primary_key=True)
