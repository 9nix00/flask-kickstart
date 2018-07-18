"""
========================
整合队列方式启动
========================

该文件根据`Flask-Kickstart`方式生成

运行该app，默认需要启用redis在 127.0.0.1:6379 并允许多数据库，允许数量>2

请求完成后，执行：
.. code-block::

    curl http://127.0.0.1:5000/hello-celery.api


"""
import os

import sys  # 此行仅为了演示方便

sys.path.insert(0, __file__.rsplit('/', 2)[0])  # 此行仅为了演示方便

from fantasy import create_app, create_celery
from werkzeug.wsgi import DispatcherMiddleware

os.environ.setdefault('HIVE_APP', 'welcome')  # 此行仅为了演示方便
os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')  # 此行仅为了演示方便
os.environ.setdefault('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/1')
os.environ.setdefault('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/2')

celery = create_celery(os.environ.get('CELERY_APP_NAME', 'fantasy'))

app = DispatcherMiddleware(create_app('welcome', celery=celery))

if __name__ == '__main__':
    import os
    from werkzeug.serving import run_simple

    bind_ip = os.environ.get('FLASK_SIMPLE_BIND', '127.0.0.1')

    run_simple(bind_ip, 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
