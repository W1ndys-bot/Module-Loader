# script/example/main.py
# 示例脚本
# 本脚本写好了基本的函数，直接在函数中编写逻辑即可，必要的时候可以修改函数名

import logging
import os
import sys

# 数据存储路径
# 实际开发时，请将example替换为具体的数据存放路径
DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "example",
)

# 添加项目根目录到sys.path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from app.config import owner_id
from app.api import *


# 群消息处理函数
async def handle_group_message(websocket, msg):
    try:
        user_id = msg.get("user_id")
        group_id = msg.get("group_id")
        raw_message = msg.get("raw_message")
        role = msg.get("sender", {}).get("role")
        message_id = msg.get("message_id")

    except Exception as e:
        logging.error(f"处理xxx群消息失败: {e}")
        return


# 群通知处理函数
async def handle_group_notice(websocket, msg):
    try:
        user_id = msg.get("user_id")
        group_id = msg.get("group_id")
        raw_message = msg.get("raw_message")
        role = msg.get("sender", {}).get("role")
        message_id = msg.get("message_id")

    except Exception as e:
        logging.error(f"处理xxx群消息失败: {e}")
        return


# 私聊消息处理函数
async def handle_private_message(websocket, msg):
    try:
        user_id = msg.get("user_id")
        raw_message = msg.get("raw_message")

    except Exception as e:
        logging.error(f"处理xxx私聊消息失败: {e}")
        return
