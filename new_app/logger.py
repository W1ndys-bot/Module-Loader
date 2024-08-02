# logger.py

import logging
import colorlog


def setup_logger():
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s %(levelname)s:%(name)s:%(message)s",  # 添加日期
            datefmt="%Y-%m-%d %H:%M:%S",  # 日期格式
            log_colors={
                "DEBUG": "cyan",
                "INFO": "light_green",  # 使用更亮的绿色
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
        )
    )
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])