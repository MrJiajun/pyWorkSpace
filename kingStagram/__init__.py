# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# [根据配置文件app.conf初始化数据库]
app = Flask(__name__)
app.config.from_pyfile('app.conf')
app.secret_key = 'kingdee'
db = SQLAlchemy(app)

login_Manager = LoginManager(app)
# 需要进行登录验证的，如果没有进行登录操作则会跳转到特定页面
login_Manager.login_view = '/regloginpage/'

from kingStagram import views, models
