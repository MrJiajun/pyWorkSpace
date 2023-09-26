# coding=utf-8

import hashlib
import random
import re

from flask import redirect, render_template, flash, request, jsonify, g
from flask_httpauth import HTTPBasicAuth
from flask_login import login_user, logout_user, login_required
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from kingStagram import app, db
from kingStagram.models import User

from CashFlowProdiction import var

auth = HTTPBasicAuth()
app.secret_key = 'kingdee'
app.jinja_env.line_statement_prefix = '#'


# 首页
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return 'Hello Kingdee!'


# 参数与模板
@app.route('/profile/<int:uid>', methods=['GET', 'POST'])
@login_required
def profile(uid):
    # return 'profile' + str(uid)
    colors = ('red', 'green', 'yellow', 'black')
    return render_template('profile.html', uid=uid, colors=colors)


# 参数与模板
@app.route('/profiles/<int:user_id>', methods=['GET', 'POST'])
@login_required
def profiles(user_id):
    user = User.query.get(user_id)
    return jsonify({'profiles Page userId': user.id}), 201


@app.route('/cashFlowPrediction', methods=['GET', 'POST'])
@login_required
def showCashFlowPrediction():
    var.demo_var()
    return 'showCashFlowPrediction seccused!'


@app.route('/regloginpage/')
def regloginpage():
    return 'needRegloginpage'


def redicrect_with_msg(target, msg, category):
    if msg is not None:
        flash(msg, category=category)
    return redirect(target)


# 重新注册
@app.route('/reg/', methods={'post', 'get'})
def reg():
    username = request.values.get('username')
    password = request.values.get('password')

    if username is None or password is None:
        return redicrect_with_msg('/regloginpage/', u'用户名或密码不能为空', category='reglogin')

    username = username.strip()
    password = password.strip()
    if username == '' or password == '':
        return redicrect_with_msg('/regloginpage/', u'用户名或密码不能为空', category='reglogin')

    user = User.query.filter_by(username=username).first()
    if user is not None:
        m = hashlib.md5()
        m.update((password + user.salt).encode('utf-8'))
        if user.password != m.hexdigest():
            return redicrect_with_msg('/regloginpage/', u'密码错误', category='reglogin')
        # 登录
        login_user(user)
        # return redicrect_with_msg('/regloginpage/', u'用户名已经存在', category='reglogin')
        return jsonify({'username': user.username, 'password': password, 'salt': user.salt}), 201
    else:
        # add salt
        salt = '.'.join(random.sample('1234567890abcdefghijkABCDEFGHIJK', 10))
        m = hashlib.md5()
        m.update((password + salt).encode('utf-8'))
        user = User(username, m.hexdigest(), salt)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return jsonify({'username': user.username, 'password': password, 'salt': user.salt}), 201


@app.route('/login', methods={'post'})
@auth.login_required
def login():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()

    if username == '' or password == '':
        return redicrect_with_msg('/regloginpage/', u'用户名或密码不能为空', category='reglogin')

    user = User.query.filter_by(username=username).first()
    if user is None:
        return redicrect_with_msg('/regloginpage/', u'用户名不存在', category='reglogin')

    m = hashlib.md5()
    m.update((password + user.salt).encode('utf-8'))
    if user.password != m.hexdigest():
        return redicrect_with_msg('/regloginpage/', u'密码错误', category='reglogin')

    login_user(user)

    return redirect('/')


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    # 设置token过期时间
    token = generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/logout', methods={'post', 'get'})
def logout():
    logout_user()
    flash('成功登出！')
    return 'logout success！'


# 验证token
@auth.verify_password
def verify_password(username, password):
    # 先验证token
    user_id = re.sub(r'^"|"$', '', username)
    user_id = verify_auth_token(user_id)
    if not user_id:
        user = User.query.filter_by(username=username).first()
        if not user_id:
            return False
    g.user_id = user_id.get('user_id')
    return True


# 生成token, 有效时间为600min
def generate_auth_token(user_id, expiration=36000):
    s = Serializer(app.secret_key, expires_in=expiration)
    return s.dumps({'user_id': user_id})


# 解析token
def verify_auth_token(token):
    s = Serializer(app.secret_key)
    # token正确
    try:
        data = s.loads(token)
        return data
    # token过期
    except SignatureExpired:
        return None
    # token错误
    except BadSignature:
        return None
