import logging
import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from app.api import send_group_msg


async def handle_group_message(websocket, msg):
    if msg["message_type"] == "group":
        group_id = msg["group_id"]
        user_id = msg["user_id"]
        raw_message = msg["raw_message"]
        logging.info(
            f"处理群消息, 群ID: {group_id}, 用户ID: {user_id}, 消息: {raw_message}"
        )
        if raw_message["message"] == "test":
            await send_group_msg(websocket, group_id, "test")
