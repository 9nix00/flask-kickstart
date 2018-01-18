"""
=============
开发机配置
=============
"""

from ..core import *
from online.web import *
_ = active_extra

DEBUG = True
DATABASE_URI = 'mysql+pymysql://root@localhost/___DATABASE___?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = DEBUG
