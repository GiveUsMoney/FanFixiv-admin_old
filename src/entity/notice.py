
from src.entity.base import Base
from sqlalchemy import Table

from src.database import engine

class Notice(Base):
    __table__ = Table('tb_notice', Base.metadata,
                    autoload=True, autoload_with=engine)