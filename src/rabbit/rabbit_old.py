
from src.config import config

import pika

# rabbit connect
class RabiitHandler:
    def __init__(self):
        self.credential = pika.PlainCredentials(config.rabbit_id, config.rabbit_pw)
        self.parmeters = pika.ConnectionParameters("mq", 5672, "/", self.credential)
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
