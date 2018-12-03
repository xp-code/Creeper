# coding=utf-8

import config

import time

# for init flower instance after celery worker.
time.sleep(5)

# This is the config for flower.

# RabbitMQ management
broker_api = config.BROKER_API

# view address
address = '0.0.0.0'
port = 10011

# basic_auth now not work. reason checking.
basic_auth = ["username:password"]

# 持久化
persistent = True
db = "var/flower_db"
