##  Creeper

通用的用于定时执行一些任务项目结构。
主要是用于定时执行一些脚本任务，或者是一些定时的爬虫任务。

## requirements

- celery   
[celery](http://celeryproject.org) Python异步任务调度工具。
- flower   
[flower](https://flower.readthedocs.io/en/latest/) Celery的监控工具。 

## How to modify.

你可以在`tasks`中添加相关任务。然后再 `celeryconfig.py` 中写定时执行，或者依据 `flower` 提供的接口直接调用。

## How to run.

使用[supervisor](http://supervisord.org/)进行项目部署.

执行前，需要修改对应的 `config.py`. 你可以在本地使用 `local_settings.py` (类似Django的配置)

单独执行 supervisor.
```bash
supervisord -c supervisor.ini
```
或者将 supervisor.ini 加入到 supervisor 的配置目录，配置到总的管理中。

