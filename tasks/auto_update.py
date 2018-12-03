# coding=utf-8
"""
    auto tasks.
"""
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger

from celery_worker import celery_app
from tasks.crawler import get_divide
from utils.base_task import CrawlerTask

logger = get_task_logger(__name__)


@celery_app.task(base=CrawlerTask, queue='task_queue')
def auto_run(a, b):
    try:
        result = get_divide(a, b)
        return result
    except SoftTimeLimitExceeded as e:
        logger.error("Task for get a:{0} b:{1} divide has time limit. errors: {2}".format(
            a, b, e
        ))
        return False
