from src.enum.action_type import ActionType
from src.entity.base_entity import Base
from src.database import engine

from sqlalchemy import Column, Integer, String, DateTime, Enum

class ActionLog(Base):
    __tablename__ = "tb_log"

    ip = Column(String(20), nullable=False)
    user = Column(Integer, nullable=False)
    action_type = Column(Enum(ActionType), nullable=False)
    action_link = Column(String(200), nullable=True)
    execute_at = Column(DateTime, nullable=False)

Base.metadata.create_all(engine)