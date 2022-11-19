from src.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from src.database import engine
from src.admin.router import router as admin_router



class TestUser(Base):
    __tablename__ = "test_user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # asda






Base.metadata.create_all(bind=engine)
