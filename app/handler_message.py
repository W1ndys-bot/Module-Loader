# handlers/message_handler.py

import json
import logging
import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.test.main import handle_group_message


# 处理消息事件的逻辑
async def handle_message_event(websocket, msg):
    try:
        # 处理群消息
        if msg.get("message_type") == "group":
            group_id = msg["group_id"]
            logging.info(f"处理群消息,群ID:{group_id}")
            logging.info(f"原消息内容:{msg}")
            await handle_group_message(websocket, msg)

        # 处理群通知事件
        elif msg.get("post_type") == "notice":
            pass
        # 处理私聊消息
        elif msg["message_type"] == "private":
            pass
            # await handle_private_message()
            # await handle_anonymous_message(websocket, user_id, raw_message) # 关闭匿名系统
        else:
            logging.info(f"收到未知消息类型: {msg}")

    except KeyError as e:
        logging.error(f"处理消息事件的逻辑错误: {e}")


# 处理通知事件的逻辑
async def handle_notice_event(websocket, msg):
    pass


# 处理请求事件的逻辑
async def handle_request_event(websocket, msg):
    pass


# 处理元事件的逻辑
async def handle_meta_event(websocket, msg):
    pass


# 处理消息
async def handle_message(websocket, message):

    msg = json.loads(message)

    logging.info(f"处理消息: {msg}")

    if "post_type" in msg:
        if msg["post_type"] == "message" or msg["post_type"] == "notice":
            # 处理消息事件，以及通知事件
            await handle_message_event(websocket, msg)
        elif msg["post_type"] == "request":
            # 处理请求事件
            await handle_request_event(websocket, msg)
        elif msg["post_type"] == "meta_event":
            # 处理元事件
            await handle_meta_event(websocket, msg)
    # 收到非事件消息
    else:
        pass
