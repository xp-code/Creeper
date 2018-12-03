# coding=utf-8

"""
    default project config.
"""
import os

# celery relatives
BROKER_URL = 'pyamqp://username:password@{}/taskData'.format(os.getenv('RABBITMQ_SERVER_PORT_5671_TCP_ADDR'))
RESULT_URL = 'redis://{}:6379/0'.format(os.getenv('REDIS_SERVER_PORT_6379_TCP_ADDR'))

# flower relatives
BROKER_API = 'http://username:password@{}:15672/api/'.format(os.getenv('RABBITMQ_SERVER_PORT_15672_TCP_ADDR'))

try:
    from local_settings import *  # nopa
except ImportError:
    pass
