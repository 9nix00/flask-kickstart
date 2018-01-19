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
    指定启动文件，并从启动文件中解析可能模块。

    附加操作，因为此处我们会解析出模块，所以我们顺便
    把requirements文件也一并解析
    同样，我们强依赖顺序，对于顺序不一致出现的多个重复的问题，我们不关心
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

    regxp = r'^from ([a-z]+)\.app import'
    modules = re.findall(regxp, buffer, re.MULTILINE | re.DOTALL)

    root = os.path.expanduser('~/Codes/1024/hive')

    project_requirements_file = os.path.join(abs_path, 'requirements.txt')
    depends_packages = []

    if 'requirements' in actions:
        hive_requirements_file = os.path.join(root, 'requirements.txt')
        if os.path.exists(hive_requirements_file):
            with open(hive_requirements_file, 'r') as fp:
                depends_packages += fp.readlines()
                pass
            pass

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

        if 'requirements' in actions:
            requirements_file = os.path.join(path, 'requirements.txt')

            if os.path.exists(requirements_file):
                with open(requirements_file, 'r') as fp:
                    depends_packages += fp.readlines()
                    pass
                pass
            pass

        if 'upgrade' in actions:
            os.system('flask db upgrade')
            pass

        pass

    with open(project_requirements_file, 'w') as fp:
        fp.write(''.join(set(depends_packages)))
        os.chdir(abs_path)
        pass
    os.system("git commit requirements.txt -m "
              "'sync requirements from hive.'")
    os.system("git push")
    pass


if __name__ == "__main__":
    actions = []

    if 'init' in sys.argv:
        actions.append('init')

    if 'migrate' in sys.argv:
        actions.append('migrate')

    if 'requirements' in sys.argv:
        actions.append('requirements')

    if 'upgrade' in sys.argv:
        actions.append('upgrade')

    migrate(actions)
