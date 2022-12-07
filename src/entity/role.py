
from src.entity.base import Base
from sqlalchemy import Table

from src.database import engine

class Role(Base):
    __table__ = Table('tb_role', Base.metadata,
                    autoload=True, autoload_with=engine)