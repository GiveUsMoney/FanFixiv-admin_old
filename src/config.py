import jwt
import datetime
from datetime import timedelta
import pika
import os


class Config:
    secret_key = os.environ.get("SECRET_KEY")

    rabbit_id = os.environ.get("RABBITMQ_DEFAULT_USER")
    rabbit_pw = os.environ.get("RABBITMQ_DEFAULT_PASS")
    rabbit_ex = os.environ.get("RABBITMQ_EXCHANGE")


config = Config()


class AuthHandler:
    secret_key = config.secret_key

    def __call__(self, request):  # 보완해야함.
        authorization = request.headers.get("Authorization")

        return authorization


# rabbit connect
class RabiitHandler:
    def __init__(self):
        self.credentai = pika.PlainCredentials(config.rabbit_id, config.rabbit_pw)
        self.parmeters = pika.ConnectionParameters("mq", 5672, "/", self.credentai)
        self.connection = pika.BlockingConnection(self.parmeters)

    # https://blog.dudaji.com/general/2020/05/25/rabbitmq.html
    def rabbit_channel(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=config.rabbit_ex, exchange_type="topic")
        return self.connection.channel()

    def push(self, queue, body):
        try:
            channel = self.rabbit_channel()
            channel.queue_declare(queue=queue)
            channel.basic_publish(
                exchange=config.rabbit_ex, routing_key="admin", body=body
            )
            channel.close()
        except Exception as e:
            print(e)
            return False
        return True

    def get(self, queue):
        try:
            channel = self.rabbit_channel()
            channel.queue_declare(queue=queue)
            method_frame, header_frame, body = channel.basic_get(queue=queue)
        except Exception as e:
            print(e)
            return False
        print(method_frame, header_frame, body)
        # if method_frame:
        #     print(method_frame, header_frame, body)
        #     self.channel.basic_ack(method_frame.delivery_tag)
        # else:
        #     print("No message returned")
        return True 
