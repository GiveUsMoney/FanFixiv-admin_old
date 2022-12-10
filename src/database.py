# fastapi database connection
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if os.environ.get("DB_URL") is None:
    sqlalchemy_database_url = "sqlite:///./tests/test.db"
else:
    sqlalchemy_database_url = os.environ["DB_URL"]


engine = create_engine(
    sqlalchemy_database_url,  # connect_args={"check_same_thread": False}
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        session = Session()
        yield session
    except:
        session.close()
