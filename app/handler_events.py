# handlers/message_handler.py

import json
import logging
import os
import sys
import asyncio


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# 总开关
from app.switch import handle_GroupSwitch_group_message

# 菜单
from app.menu import handle_Menu_group_message


# 处理消息事件的逻辑
async def handle_message_event(websocket, msg):
    try:
        # 处理群消息
        if msg.get("message_type") == "group":

            group_id = msg["group_id"]
            logging.info(f"处理群消息,群ID:{group_id}")

            # 并发执行群消息处理函数
            await asyncio.gather()

        # 处理私聊消息
        elif msg.get("message_type") == "private":
            user_id = msg.get("user_id")
            # 并发执行私聊消息处理函数
            await asyncio.gather()

        else:
            logging.info(f"收到未知消息类型: {msg}")

    except KeyError as e:
        logging.error(f"处理消息事件的逻辑错误: {e}")


# 处理通知事件的逻辑
async def handle_notice_event(websocket, msg):

    # 处理群通知
    if msg.get("post_type") == "notice":
        group_id = msg["group_id"]
        logging.info(f"处理群通知事件, 群ID: {group_id}")

        await asyncio.gather()


# 处理请求事件的逻辑
async def handle_request_event(websocket, msg):

    await asyncio.gather()


# 处理元事件的逻辑
async def handle_meta_event(websocket, msg):
    pass


# 处理定时任务，每个心跳周期检查一次
async def handle_cron_task(websocket):
    try:
        await asyncio.gather()
    except Exception as e:
        logging.error(f"处理定时任务的逻辑错误: {e}")


# 处理ws消息
async def handle_message(websocket, message):

    msg = json.loads(message)

    # 排除回应消息
    if msg.get("status") == "ok":
        return

    logging.info(f"处理消息: {msg}")

    # 处理事件
    if "post_type" in msg:
        if msg["post_type"] == "message":
            # 处理消息事件
            await handle_message_event(websocket, msg)
        elif msg["post_type"] == "notice":
            # 处理通知事件
            await handle_notice_event(websocket, msg)
        elif msg["post_type"] == "request":
            # 处理请求事件
            await handle_request_event(websocket, msg)
        elif msg["post_type"] == "meta_event":
            # 处理元事件
            await handle_meta_event(websocket, msg)
            # 处理定时任务，每个心跳周期检查一次
            await handle_cron_task(websocket)
