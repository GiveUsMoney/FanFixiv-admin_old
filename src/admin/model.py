from src.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from src.database import engine


class ActionLog:
    __tablename__ = "action_log"
    id = Column(Integer, primary_key=True, index=True)

    ip = Column(String(20), nullable=False)
    user = Column(String(20), nullable=False)
    action_type = Column(String(20), nullable=False)
    action_link = Column(String(20), nullable=True)
    created_at = Column()


Base.metadata.create_all(bind=engine)
