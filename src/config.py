import os

class Config:
    secret_key = os.environ.get("SECRET_KEY")

    AMQP_URI = os.environ.get("AMQP_URI")
    rabbit_ex = os.environ.get("RABBITMQ_EXCHANGE")


config = Config()


class AuthHandler:
    secret_key = config.secret_key

    def __call__(self, request):  # 보완해야함.
        authorization = request.headers.get("Authorization")

        return authorization
 