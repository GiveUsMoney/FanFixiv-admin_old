import jwt
import datetime
from datetime import timedelta
import pika


class AuthHandler:
    secret_key = ""  # 나중에 추가해야함.

    def __call__(self, request):  # 보완해야함.
        authorization = request.headers.get("Authorization")

        return authorization

    def encode_token(self, user_id: int):
        try:
            payload = {
                "exp": datetime.utcnow() + timedelta(days=0, seconds=5),
                "iat": datetime.utcnow(),
                "sub": user_id,
            }
            return jwt.encode(payload, self.secret_key, algorithm="HS256")
        except Exception as e:
            return e

    def decode_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, self.secret_key)
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."


# rabbit connect
class RabiitHandler:
    def __init__(self):
        self.credentai = pika.PlainCredentials("admin", "admin@1234")
        self.parmeters = pika.ConnectionParameters("mq", 5672, "/", self.credentai)
        self.connection = pika.BlockingConnection(self.parmeters)
        self.channel = self.connection.channel()

    def push(self, queue, body):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange="", routing_key="admin", body=body)
        return "Good"

    def get(self, queue):
        self.channel.queue_declare(queue="hello")
        method_frame, header_frame, body = self.channel.basic_get(queue="hello")
        print(method_frame, header_frame, body)
        # if method_frame:
        #     print(method_frame, header_frame, body)
        #     self.channel.basic_ack(method_frame.delivery_tag)
        # else:
        #     print("No message returned")
        return "Good"
