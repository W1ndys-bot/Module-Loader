# script/Menu/main.py
# 示例脚本
# 本脚本写好了基本的函数，直接在函数中编写逻辑即可，必要的时候可以修改函数名
# 注意：Menu 是具体功能，请根据实际情况一键替换即可
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
from app.scripts.GroupSwitch.main import *

# 数据存储路径，实际开发时，请将Menu替换为具体的数据存放路径
DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "Menu",
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


# 群管系统菜单
async def GroupManager(websocket, group_id, message_id):
    message = (
        f"[CQ:reply,id={message_id}]"
        + """
GroupManager 群管理系统

ban@ 时间 禁言x秒，默认60秒
unban@ 解除禁言
banme 随机禁言自己随机秒
banrandom 随机禁言一个群友随机秒
banall 全员禁言
unbanall 全员解禁
t@ 踢出指定用户
recall 撤回消息(需要回复要撤回的消息)
vc-on 开启视频监控
vc-off 关闭视频监控
wf-on 开启欢迎欢送
wf-off 关闭欢迎欢送
"""
    )
    await send_group_msg(websocket, group_id, message)


async def menu(websocket, group_id, message_id):
    message = (
        f"[CQ:reply,id={message_id}]"
        + """
卷卷bot功能列表

groupswitch 查看群功能开关
groupmanager 群管理命令
blacklist 黑名单系统
banwords 违禁词系统
invitechain 邀请链系统
qasystem 问答系统
"""
    )

    await send_group_msg(websocket, group_id, message)


async def Blacklist(websocket, group_id, message_id):
    message = (
        f"[CQ:reply,id={message_id}]"
        + """
黑名单系统

bl-add 添加黑名单
bl-rm 删除黑名单
bl-list 查看黑名单
bl-check 检查黑名单

黑名单系统默认开启，无开关
"""
    )
    await send_group_msg(websocket, group_id, message)


async def BanWords(websocket, group_id, message_id):
    message = (
        f"[CQ:reply,id={message_id}]"
        + """
违禁词系统

bw-on 开启违禁词监控
bw-off 关闭违禁词监控
bw-list 查看违禁词列表
bw-add 添加违禁词
bw-rm 删除违禁词
"""
    )
    await send_group_msg(websocket, group_id, message)


async def InviteChain(websocket, group_id, message_id):
    message = (
        f"[CQ:reply,id={message_id}]"
        + """
邀请链系统

ic-on 开启邀请链
ic-off 关闭邀请链
ic-list @ 查看邀请链
"""
    )
    await send_group_msg(websocket, group_id, message)


# 群消息处理函数
async def handle_Menu_group_message(websocket, msg):
    try:
        group_id = msg.get("group_id")
        raw_message = msg.get("raw_message")
        message_id = msg.get("message_id")
        self_id = msg.get("self_id")
        if raw_message == "menu" or f"[CQ:at,qq={self_id}" in raw_message:
            await menu(websocket, group_id, message_id)
        elif raw_message == "groupmanager":
            await GroupManager(websocket, group_id, message_id)
        elif raw_message == "blacklist":
            await Blacklist(websocket, group_id, message_id)
        elif raw_message == "banwords":
            await BanWords(websocket, group_id, message_id)
        elif raw_message == "invitechain":
            await InviteChain(websocket, group_id, message_id)

    except Exception as e:
        logging.error(f"处理Menu群消息失败: {e}")
        return
