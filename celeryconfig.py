# coding=utf-8


from celery.schedules import crontab

# the timezone for celery use
enable_utc = True
timezone = 'Asia/Shanghai'

# celery worker relative
worker_concurrency = 2  # 并发的 worker
worker_prefetch_multiplier = 1

# task time limit
task_soft_time_limit = 100

# per worker handler task. close and restart a new
worker_max_tasks_per_child = 10

# code serializer type.
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['pickle', 'json']

# ignore the task result
task_ignore_result = True

# celery routes
task_routes = {
    'tasks.auto_update.*': {
        'queue': 'task_queue',
        'routing_key': 'my-task'
    }
}

# celery include tasks.
imports = (
    'tasks.auto_update',
)

beat_schedule = {
    # auto run crontab task.
    'run_task_on_everyday': {
        'task': 'tasks.auto_update.auto_run',
        'schedule': crontab(
            hour=22,
            minute=45,
        ),
        'args': (10, 2)
    }
}
