from src.database import base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from src.database import engine
from src.admin.router import router as admin_router

Base = declarative_base()

Base.metadata.create_all(bind=engine)


class TestUser(Base):
    __tablename__ = "test_user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
