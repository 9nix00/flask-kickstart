"""
================
启动文件
================

该文件根据`Flask-Kickstart`方式生成

正确运行你需要当前项目能正确引用
`account`和`welcome` 组件


.. note::

    引用方式务必按照 from xxx.app import app as xxxx
    的格式，我们的db处理工具，需要依赖完全正确的格式匹配



"""

from werkzeug.wsgi import DispatcherMiddleware

from account.app import app as account_app
from welcome.app import app as welcome_app

application = DispatcherMiddleware(welcome_app, {
    '/account': account_app,
})


if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 5000, application,
               use_reloader=True, use_debugger=True, use_evalex=True)
