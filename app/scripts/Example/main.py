# script/example/main.py
# 示例脚本
# 本脚本写好了基本的函数，直接在函数中编写逻辑即可，必要的时候可以修改函数名
# 注意：Example 是具体功能，请根据实际情况一键替换即可
# 注意：function 是函数名称，请根据实际情况一键替换即可

import logging
import os
import sys
import asyncio

# 添加项目根目录到sys.path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from app.config import owner_id
from app.api import *
from app.scripts.GroupSwitch.main import load_switch, save_switch

# 数据存储路径，实际开发时，请将Example替换为具体的数据存放路径
DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "Example",
)


# 查看功能开关状态
def load_function_status(group_id):
    return load_switch(
        group_id, "function_status"
    )  # 注意：function_status 是开关名称，请根据实际情况修改


# 保存功能开关状态
def save_function_status(group_id, status):
    save_switch(
        group_id, "function_status", status
    )  # 注意：function_status 是开关名称，请根据实际情况修改


# 群消息处理函数
async def handle_Example_group_message(websocket, msg):
    try:
        user_id = msg.get("user_id")
        group_id = msg.get("group_id")
        raw_message = msg.get("raw_message")
        role = msg.get("sender", {}).get("role")
        message_id = msg.get("message_id")

    except Exception as e:
        logging.error(
            f"处理Example群消息失败: {e}"
        )  # 注意：Example 是具体功能，请根据实际情况修改
        return


# 群通知处理函数
async def handle_Example_group_notice(websocket, msg):
    try:
        user_id = msg.get("user_id")
        group_id = msg.get("group_id")
        raw_message = msg.get("raw_message")
        role = msg.get("sender", {}).get("role")
        message_id = msg.get("message_id")

    except Exception as e:
        logging.error(
            f"处理Example群通知失败: {e}"
        )  # 注意：Example 是具体功能，请根据实际情况修改
        return


# 私聊消息处理函数
async def handle_Example_private_message(websocket, msg):
    try:
        user_id = msg.get("user_id")
        raw_message = msg.get("raw_message")

    except Exception as e:
        logging.error(f"处理xxx私聊消息失败: {e}")
        return


async def Example_main(websocket, msg):

    # 确保数据目录存在
    os.makedirs(DATA_DIR, exist_ok=True)

    # 根据消息类型执行不同的函数，一般按照消息类型写不同的功能，这里一般只需要一个函数，删除多余即可
    # 如果需要多个函数，请使用asyncio.gather并发执行
    await handle_Example_group_message(websocket, msg)
    await handle_Example_group_notice(websocket, msg)
    await handle_Example_private_message(websocket, msg)
