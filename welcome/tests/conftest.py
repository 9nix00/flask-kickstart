"""
=============

=============
"""

pytest_plugins = "fantasy.fixtures.pytest_hive",


def pytest_namespace():
    return {
        'entry_app': 'welcome'
    }
