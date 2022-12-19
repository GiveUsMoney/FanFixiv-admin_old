from src.entity.base import Base
from src.enum.action_type import ActionType

from sqlalchemy import Column, Integer, String, DateTime, Enum, TIMESTAMP, func

class ActionLog(Base):
    __tablename__ = "tb_log"
    
    seq = Column(Integer, primary_key=True, index=True)

    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )

    ip = Column(String(20), nullable=False)
    user = Column(Integer, nullable=False)
    action_type = Column(Enum(ActionType), nullable=False)
    action_link = Column(String(200), nullable=True)
    execute_at = Column(DateTime, nullable=False)