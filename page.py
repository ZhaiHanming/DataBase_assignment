from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)

# 全局变量user用于记录已经成功登陆的用户ID
# 全局变量iden用于记录已经成功登陆的用户身份 S学生 T教师

@app.route('/', methods=['GET', 'POST'])   
def home():
    return	''' <h1>Home</h1>
				<a href="http://127.0.0.1:5000/tsignin">
				<button>教师登录...</button>
				</a>
				<a href="http://127.0.0.1:5000/ssignin">
				<button>学生登录...</button>
				</a>
			'''

# student login page
@app.route('/ssignin', methods=['GET'])
def student_signin_form():
	return  '''<form action="/ssignin" method="post">
				<p><input name="ID"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''

@app.route('/ssignin', methods=['POST'])
def student_signin():
	UserID = request.form['ID']
	conn = sqlite3.connect('E:\DataBase_assignment\web_programming\SC.db')
	cursor = conn.cursor()
	selectSQL = 'select Spassword from User_Student where SID = \''
	selectSQL += UserID
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
		global user = UserID
		global iden = 'S'
		return   '''<h3>Hello, admin!</h3>
					<a href="http://127.0.0.1:5000/sinfo">
					<button>个人信息...</button>
					</a>
				'''
	return '<h3>Bad username or password.</h3>'



# teacher login page
@app.route('/tsignin', methods=['GET'])
def teacher_signin_form():
	return  '''<form action="/tsignin" method="post">
				<p><input name="ID"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''

@app.route('/tsignin', methods=['POST'])
def teacher_signin():
	UserID = request.form['ID']
	conn = sqlite3.connect('E:\DataBase_assignment\web_programming\SC.db')
	cursor = conn.cursor()
	selectSQL = 'select Tpassword from User_Teacher where TID = \''
	selectSQL += UserID
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
		global user = UserID
		global iden = 'T'
		return   '''<h3>Hello, admin!</h3>
					<a href="http://127.0.0.1:5000/tinfo">
					<button>个人信息...</button>
					</a>
				'''
	return '<h3>Bad username or password.</h3>'



# show student information
@app.route('/sinfo', methods=['POST'])
def student():
	conn = sqlite3.connect('E:\DataBase_assignment\web_programming\SC.db')
	cursor = conn.cursor()
	selectSQL = 'select * from Student where SID = \''
	selectSQL += user
	selectSQL += '\''
	cursor.execute(selectSQL)
	values = cursor.fetchall()
	conn.commit()
	conn.close()
	info = values.__str__()
	info = info[3:-4]
	table = '''<table border="1">
			<tr>
				<th>StudentName</th>
				<th>StudentID</th>
			</tr>
			<tr>'''
	table += '<td>%s</td>' % sname
	table += '<td>%s</td>' % info
	table += '''</tr>
			</table>'''
	return table
	
# show teacher information
@app.route('/tinfo', methods=['POST'])
def student():
	conn = sqlite3.connect('E:\DataBase_assignment\web_programming\SC.db')
	cursor = conn.cursor()
	selectSQL = 'select * from Student where SID = \''
	selectSQL += sname
	selectSQL += '\''
	cursor.execute(selectSQL)
	values = cursor.fetchall()
	conn.commit()
	conn.close()
	info = values.__str__()
	info = info[3:-4]
	table = '''<table border="1">
			<tr>
				<th>StudentName</th>
				<th>StudentID</th>
			</tr>
			<tr>'''
	table += '<td>%s</td>' % sname
	table += '<td>%s</td>' % info
	table += '''</tr>
			</table>'''
	return table


if __name__ == '__main__':
    app.run()
