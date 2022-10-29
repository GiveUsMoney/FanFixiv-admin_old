# fastapi database connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from dotenv import load_dotenv
import sqlalchemy
import os

# load_dotenv()

sqlalchemy_database_url = os.environ["DATABASE_URL"]
# sqlalchemy_database_url = f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOST"]}/postgres'
# sqlalchemy_database_url = f'postgresql://{os.getenv("db_user")}:{os.getenv("db_password")}@{os.getenv("db_host")}/{os.getenv("db_name")}'
print(sqlalchemy_database_url)

engine = create_engine(
    sqlalchemy_database_url,  # connect_args={"check_same_thread": False}
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


base = declarative_base()


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close
