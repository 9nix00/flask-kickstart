"""
=============
开发机配置
=============
"""

from ..core import *
_ = active_core

DEBUG = True
JSON_AS_ASCII = False

DATABASE_URI = 'mysql+pymysql://root@localhost/___DATABASE___?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = DEBUG
