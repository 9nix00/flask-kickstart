"""
====================
测试用例集配置文件
====================
"""

pytest_plugins = "app_fixtures.myapp",  # 固定声明，引入扩展


def pytest_namespace():
    return {
        'entry_app': 'welcome'  # 指定入口，通常是包名
    }
