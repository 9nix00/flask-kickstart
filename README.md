Flask Kickstart
=================

我们的标准工具链
----

- pycharm
- macOS


使用约束
----

- 项目名称必须是一个合法的python包名称且不能叫hive
- 仅支持Github
- Github 团队（个人）目录下必须有一个命名为___REPO___-config的配置项目
- 本地部署目录必须有真实可用的hello-deploy

- 服务器端用户名始终为：

    - web用户为：web-项目名称
    - conf用户为：conf-项目名称


你需要做什么？
---

执行

```
cliez create wangwenpei/flask-kickstart <本地路径>
```

打开该文档并编辑下面参数为自己满意的参数后，然后再执行

```
cliez init -s \
author:wangwenpei \
email:wangwenpei@nextoa.com \
\
RAVEN-USER:f6401e6e5bf24551bed99879d996f843 \
RAVEN-SECRET:b94239fcc9eb4a609607abeb3fac60cd \
RAVEN-HOST:sentry.io \
RAVEN-ID:239195 \
\
\
LB-ID:lb-lfe5lvp7  CLOUD-ZONE:sha1a \
HTTP-LISTENER:lbl-bqonntxu  LB-BACKEND-ID:izpc327t \
MACHINE-IP:192.168.190.3 \
ROUTER-IP:139.198.190.190 \
\
\
REPO:wangwenpei/___pkg___ \
GFW:direct \
PYTHON-VERSION:pypy3.5-5.10.0 \
DATABASE:___pkg___ \
DOMAIN:___pkg___.com \
WSGI-PORT:<端口号7010-7999> \
pkg:<必须是英文> \
--skip-builtin --yes

# 建议修改执行上条语句后执行
mysql -uroot -e 'CREATE DATABASE `___DATABASE___` DEFAULT CHARACTER SET utf8mb4'
```
