from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, TIMESTAMP, func

class BaseEntity:
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )

Base = declarative_base(cls=BaseEntity)
