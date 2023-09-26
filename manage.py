# coding=utf-8

import hashlib
import random

from flask_script import Manager
from kingStagram import app, db
from kingStagram.models import User

# 将工程导进去
manager = Manager(app)


@manager.command
def init_database():
    # 删除所有表
    db.drop_all()
    # 创建所有表
    db.create_all()
    # 插入 用户 数据

    salt = '.'.join(random.sample('1234567890abcdefghijkABCDEFGHIJK', 10))
    m = hashlib.md5()
    m.update(("xiaoxiao" + salt).encode('utf-8'))
    user = User("123", m.hexdigest(), salt)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()