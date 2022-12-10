
from src.entity.base import Base
from sqlalchemy import Table

from src.database import engine

class Profile(Base):
    __table__ = Table('tb_profile', Base.metadata,
                    autoload=True, autoload_with=engine)