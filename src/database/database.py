# fastapi database connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = "postgresql://postgres:O1Ja1H5pmvG62dT0QYEc@fanfixiv-dev.ccvt0wdggzcm.ap-northeast-2.rds.amazonaws.com/fanfixiv"

engine = create_engine(
    sqlalchemy_database_url,  # connect_args={"check_same_thread": False}
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()
