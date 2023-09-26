from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:250017@172.17.240.1:3306/project'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

database = SQLAlchemy(app)

manager = Manager(app)


class KingdeeUser(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True)
    email = database.Column(database.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


@manager.command
def init_database():
    database.drop_all()
    database.create_all()
    for i in range(0, 6):
        database.session.add(KingdeeUser('xiaoxiao' + str(i), 'a' + str(i)))
    database.session.commit()

    print(1, KingdeeUser.query.all())
    print(2, KingdeeUser.query.get(3))
    print(3, KingdeeUser.query.filter_by(id=5).first())
    print(4, KingdeeUser.query.order_by(KingdeeUser.id.desc()).offset(1).limit(2).all())


if __name__ == '__main__':
    manager.run()
