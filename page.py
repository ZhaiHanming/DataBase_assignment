from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])   
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
	return  '''<form action="/signin" method="post">
				<p><input name="ID"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''

@app.route('/signin', methods=['POST'])
def signin():
	Username = request.form['ID']
	conn = sqlite3.connect('E:\DataBase_assignment\Assignmet\SC.db')
	cursor = conn.cursor()
	selectSQL = 'select Spassword from User_Student where SID = \''
	selectSQL += Username
	selectSQL += '\''
	cursor.execute(selectSQL)
	values = cursor.fetchall()
	conn.commit()
	conn.close()
	# 需要从request对象读取表单内容：
	Password = request.form['password']
	#Password = Password[2:-3]
	PW = values.__str__()
	PW = PW[3:-4]
	#print (PW)
	if  PW == Password:
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
