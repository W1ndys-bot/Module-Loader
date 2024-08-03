# 开发文档

## 机器人启动

```bash
python main.py
```

## 开发功能

在 `app/scripts` 中，你可以看到一个示例目录 `test/main.py`，这是一个用来测试的功能，群里发“test”，机器人会回复“Test Successful”。下面将以此为例，讲解如何开发功能。

### 如何开发功能

OneBot 11 标准已经支持了大部分功能，本项目已经将 OneBot 11 标准的所有功能全部集成出 API，你只需要导入到 `你的功能目录` 中，就可以直接引用函数

具体的 API 文档请参考：[onebot-11/api at master · botuniverse/onebot-11 (github.com)](https://github.com/botuniverse/onebot-11/tree/master/api)

### 如何确认收到的事件

文档里详细说明了 QQ 各种情况的发生会发出什么类型的消息，以便于功能开发者对症下药进行开发

具体的事件类型可以前往 OneBot 11 标准查看：[onebot-11/event/README.md at master · botuniverse/onebot-11 (github.com)](https://github.com/botuniverse/onebot-11/blob/master/event/README.md)

### 下面以 `test.py` 为例演示

```python
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

```
