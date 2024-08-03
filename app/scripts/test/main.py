import logging
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )  # 添加到系统路径
)

from app.api import send_group_msg  # 导入发送群消息的函数


# 写一个用来接收消息的函数
async def handle_group_message(websocket, msg):
    if msg["message_type"] == "group":  # 判断消息类型是否为群消息
        group_id = msg["group_id"]  # 获取群ID
        user_id = msg["user_id"]  # 获取用户ID
        raw_message = msg["raw_message"]  # 获取原始消息
        logging.info(
            f"处理群消息, 群ID: {group_id}, 用户ID: {user_id}, 消息: {raw_message}"  # 打印日志
        )
        if raw_message["message"] == "test":  # 判断消息是否为“test”
            await send_group_msg(websocket, group_id, "Test Successful")  # 发送群消息
