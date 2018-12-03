# coding=utf-8

"""
    示例任务。
"""

from tasks import logger


def get_divide(a, b):
    try:
        r = a / b
        return r
    except Exception as e:
        logger.error("calc error, {}".format(e))
        return None
