"""
================
Database 操作
================
"""

import os
import re
import sys


def migrate(actions):
    """
    指定启动文件，并从启动文件中解析可能模块
    """

    if not actions:
        print("no action found... use {init,migrate,upgrade}")
        pass

    abs_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, abs_path)

    dir_name = os.path.basename(abs_path)

    bootstrap_file = os.path.join(abs_path, dir_name + '.py')

    with open(bootstrap_file, 'r') as fp:
        buffer = fp.read()
        pass

    regxp = r'from ([a-z]+)\.app import'
    modules = re.findall(regxp, buffer, re.MULTILINE | re.DOTALL)

    root = os.path.expanduser('~/Codes/1024/hive')

    for mod in modules:
        path = os.path.join(root, mod)
        os.chdir(path)

        os.environ['FLASK_APP'] = 'app.py'

        if 'init' in actions:
            if not os.path.exists('./migrations'):
                os.system('flask db init')
            else:
                print("Migrations目录已存在，跳过初始化环节：%s" % mod)
            pass

        if 'migrate' in actions:
            os.system('flask db migrate')
            pass


        if 'upgrade' in actions:
            os.system('flask db upgrade')
            pass
        pass

    pass


if __name__ == "__main__":
    actions = []

    if 'init' in sys.argv:
        actions.append('init')

    if 'migrate' in sys.argv:
        actions.append('migrate')

    if 'upgrade' in sys.argv:
        actions.append('upgrade')

    migrate(actions)
