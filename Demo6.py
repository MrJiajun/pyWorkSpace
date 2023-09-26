from flask import Flask
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)

@manager.option('-n', '--name',dest='name', default='kingdee')
def	hello(name):
	'say hello world'
	print('hello %s' % name)

@manager.command
def init_database():
	print('init_database')

if __name__ == '__main__':
	manager.run()

