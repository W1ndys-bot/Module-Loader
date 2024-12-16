# script/Menu/main.py
# 示例脚本
# 本脚本写好了基本的函数，直接在函数中编写逻辑即可，必要的时候可以修改函数名
# 注意：Menu 是具体功能，请根据实际情况一键替换即可
# 注意：function 是函数名称，请根据实际情况一键替换即可

import logging
import asyncio


from config import owner_id
from api import *
from switch import *

# 数据存储路径，实际开发时，请将Menu替换为具体的数据存放路径
DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "Menu",
)

VERSION = "1.1.5"


# 菜单
async def menu(websocket, group_id, message_id):
    message = (
        f"[CQ:reply,id={message_id}]"
        + f"""bot功能列表

Version：{VERSION}"""
    )

    await send_group_msg(websocket, group_id, message)


# 群消息处理函数
async def handle_Menu_group_message(websocket, msg):
    try:
        group_id = str(msg.get("group_id"))
        raw_message = msg.get("raw_message")
        message_id = msg.get("message_id")

        if raw_message == "menu":
            await menu(websocket, group_id, message_id)

    except Exception as e:
        logging.error(f"处理Menu群消息失败: {e}")
        return
