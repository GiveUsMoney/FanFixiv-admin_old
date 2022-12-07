
from src.entity.base import Base
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from src.database import engine

class User(Base):
    __table__ = Table('tb_user', Base.metadata,
                    autoload=True, autoload_with=engine)