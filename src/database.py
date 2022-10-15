# fastapi database connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import sqlalchemy
import os
from src.config import sqlalchemy_database_url

load_dotenv()
engine = create_engine(
    sqlalchemy_database_url,  # connect_args={"check_same_thread": False}
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


sqlalchemy_database_url = f'postgresql://{os.getenv("asd")}:{os.getenv("db_passwordo")}@{os.getenv("db_host")}/{os.getenv("db_name")}'


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close