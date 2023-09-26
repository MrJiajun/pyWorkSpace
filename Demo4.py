from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route('/index/')
def index():
    return "<p>Hello, kingdee!</p>"



@app.route('/getResource/<int:uuid>', methods = ['GET', 'POST'])
def getResource(uuid):
    return "getResource:" + str(uuid)


if __name__ == '__main__':
	app.run(debug=True)