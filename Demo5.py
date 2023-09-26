from flask import Flask, render_template

app = Flask(__name__)

app.jinja_env.line_statement_prefix = '#'

@app.route("/")
@app.route('/index/')
def index():
    return "<p>Hello, kingdee!</p>"


@app.route('/getResource/<int:uid>', methods = ['GET', 'POST'])
def getResource(uid):
	colors = ('red','yellow','green')
	paymentinfo = {'be': '银企', 'cas': '出纳', 'fs':'结算', 'cbs':'跨境支付'}
	return render_template("profile.html", uid = uid, colors=colors, paymentinfo=paymentinfo)


if __name__ == '__main__':
	app.run(debug=True)