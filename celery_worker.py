# coding=utf-8

from celery import Celery
import celeryconfig
import config

celery_app = Celery(
    __name__,
    broker=config.BROKER_URL,
    backend=config.RESULT_URL
)

celery_app.config_from_object(celeryconfig)
