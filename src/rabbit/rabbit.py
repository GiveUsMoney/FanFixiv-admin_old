import json
from aio_pika import connect_robust
from aio_pika.abc import AbstractIncomingMessage

from src.config import config
from src.database import SessionLocal
from src.entity.action_log import ActionLog
from src.enum.action_type import ActionType

__all__ = ["consume"]

def body2action(body):
  data = {}
  data['ip'] = body['ip']
  data['user'] = body['user']
  data['action_link'] = body['path']
  data['execute_at'] = body['time']
  return data

async def main_action(message: AbstractIncomingMessage):
    body = json.loads(message.body)
    with SessionLocal.begin() as session:
        session.add(ActionLog(**body2action(body), action_type=ActionType.MAIN))


async def user_action(message: AbstractIncomingMessage):
    body = json.loads(message.body)
    with SessionLocal.begin() as session:
        session.add(ActionLog(**body2action(body), action_type=ActionType.USER))


async def consume(loop):
    connection = await connect_robust(config.AMQP_URI, loop=loop)
    channel = await connection.channel()

    main_queue = await channel.get_queue("main.action")
    user_queue = await channel.get_queue("user.action")

    await main_queue.consume(main_action, no_ack=True)
    await user_queue.consume(user_action, no_ack=True)

    return connection
