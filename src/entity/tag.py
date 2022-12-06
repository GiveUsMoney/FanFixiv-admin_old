
from src.entity.base import Base
from sqlalchemy import Table

from src.database import engine

class Tag(Base):
    __table__ = Table('tb_tag', Base.metadata,
                    autoload=True, autoload_with=engine)