# fastapi database connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 디렉토리
from ..config.const import sqlalchemy_database_url

engine = create_engine(
    sqlalchemy_database_url,  # connect_args={"check_same_thread": False}
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()
