# 기본 설정들이 들어가는 파일

import sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv()

sqlalchemy_database_url = f'postgresql://{os.getenv("asd")}:{os.getenv("db_passwordo")}@{os.getenv("db_host")}/{os.getenv("db_name")}'
