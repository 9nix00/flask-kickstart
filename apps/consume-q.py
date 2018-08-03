"""
========================
消费队列
========================

该文件根据`Flask-Kickstart`方式生成

该app用于消费通过`with-q.py`产生的消息

"""
import os

import sys  # 此行仅为了演示方便

sys.path.insert(0, __file__.rsplit('/', 2)[0])  # 此行仅为了演示方便

from fantasy import create_app, create_celery, load_tasks   # noqa: E402

os.environ.setdefault('HIVE_APP', 'welcome')  # 此行仅为了演示方便
os.environ.setdefault('FANTASY_SETTINGS_MODULE', 'web.conf')  # 此行仅为了演示方便
os.environ.setdefault('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/1')
os.environ.setdefault('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/2')

celery = create_celery(os.environ.get('CELERY_APP_NAME', 'fantasy'))
app = create_app('welcome', celery=celery)

if __name__ == '__main__':
    load_tasks(app, __file__)
