# coding=utf-8

"""
    rewrite celery base methods.
    You can write your retry method or task other thing.
"""

from celery.task import BaseTask
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


class CrawlerTask(BaseTask):

    def run(self, *args, **kwargs):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        """
        :param retval: result for worker return
        :param task_id: Unique id of the executed task.
        :param args:
        :param kwargs:
        :return:
        """
        logger.info('Task {0!r} for POST {1} DONE! Result :{2}'.format(task_id, args, retval))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('Task {0!r} for POST {1} FAILED! args:{2}, kw: {3}, einfo: {4}'.format(
            task_id, args, args, kwargs, einfo)
        )

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        logger.info('Task {0!r} for POST {1} will be retry!')
        return super(CrawlerTask, self).on_retry(exc, task_id, args, kwargs, einfo)