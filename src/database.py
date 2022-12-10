# fastapi database connection
import os

from src.config import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.entity.base as base

sqlalchemy_database_url = config.DB_URI

engine = create_engine(
    sqlalchemy_database_url,  # connect_args={"check_same_thread": False}
    echo=config.ENV == "dev"
)

import src.entity.action_log
import src.entity.tag
import src.entity.user
import src.entity.role
import src.entity.notice
import src.entity.profile

base.Base.metadata.create_all(engine, checkfirst=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = SessionLocal()
    try:
        yield session
    except:
        session.close()
