#所谓的MVC	使用模板
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html') #Flask通过render_template()函数来实现模板的渲染

@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/signin', methods=['post'])
def signin():  #需要从request对象读取表单内容
	username = request.form['username']
	passwold = request.form['passwold']
	if username == 'admin' and passwold == 'passwold':
		return render_template('signin-ok.html', username=username)
	return render_template('form.html', message='Bad username or passwold', username=username)

if __name__=='__main__':
	app.run()  #flask自带的server在5000端口监听












