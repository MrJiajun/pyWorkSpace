# coding=utf-8

from kingStagram import db, login_Manager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    salt = db.Column(db.String(32))

    def __init__(self, username, password, salt=''):
        self.username = username
        self.password = password
        self.salt = salt

    def __repr__(self):
        return '<User %d %s %s>' % (self.id, self.username, self.salt)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


@login_Manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
