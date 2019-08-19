from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
	return  ''' <form action="/signin" method="post">
				<p><input name="username"></p>
				<p><input name="passwold" type="passwold"></p>
				<p><button type="submit">Sign In</p>
				</form>'''

@app.route('/signin', methods=['post'])
def signin():  #需要从request对象读取表单内容
	username = request.form['username']
	passwold = request.form['passwold']
	if username == 'admin' and passwold == 'passwold':
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or passwold</h3>'

if __name__=='__main__':
	app.run()  #flask自带的server在5000端口监听












