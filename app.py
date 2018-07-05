"""
================
App启动文件
================

该文件根据`Flask-Kickstart`方式生成

正确运行你需要当前项目能正确引用
`account`和`welcome` 组件


.. note::

    引用方式务必按照 from xxx.app import app as xxxx
    的格式，我们的db处理工具，需要依赖完全正确的格式匹配



"""
import os

from fantasy import create_app, create_celery
from flask_sqlalchemy import SQLAlchemy
from werkzeug.wsgi import DispatcherMiddleware


os.environ.setdefault('HIVE_APP', 'welcome')
os.environ.setdefault('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/1')
os.environ.setdefault('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/2')

db = SQLAlchemy()

os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')
celery = create_celery(os.environ.get('CELERY_APP_NAME', 'fantasy'))

app = DispatcherMiddleware(create_app('welcome', db=db), {
})

if __name__ == '__main__':
    import os
    from werkzeug.serving import run_simple

    bind_ip = os.environ.get('FLASK_SIMPLE_BIND', '127.0.0.1')

    run_simple(bind_ip, 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
