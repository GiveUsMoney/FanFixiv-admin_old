import os

class Config:

    ENV = os.environ.get("ENV")
    DEV_SERV = os.getenv("DEV_SERV")

    SECRET = os.environ.get("SECRET")

    DB_USER = os.environ.get('DB_USER')
    DB_PW = os.environ.get('DB_PW')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')

    DB_URI = f"postgresql://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    AMQP_URI = os.environ.get("AMQP_URI")


config = Config()


class AuthHandler:
    secret_key = config.SECRET

    def __call__(self, request):  # 보완해야함.
        authorization = request.headers.get("Authorization")

        return authorization
 