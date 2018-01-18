# -*- coding: utf-8 -*-
from cabric.api import *
from fabric.api import *


@task
def sync_db():
    with cd("/home/web-___pkg___/___REPO___"):
        run("python db.py upgrade", user="web-__pkg__")
        pass
    pass
