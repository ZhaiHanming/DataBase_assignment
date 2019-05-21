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
				<p><input name="username"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''

@app.route('/signin', methods=['POST'])
def signin():
	Username = request.form['username']
	conn = sqlite3.connect('E:\\DataBase_assignment\\web_programming\\userlist.db')
	cursor = conn.cursor()
	selectSQL = 'select Password from user where Username = \''
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

@app.route('/addstudent', methods=['GET'])
def add_form():
	return  '''<form action="/addstudent" method="post">
				<p><input name="studentname"></p>
				<p><input name="information" type="password"></p>
				<p><button type="submit">Hand up</button></p>
				</form>'''

@app.route('/addstudent', methods=['POST'])
def add():
	Studentname = request.form['studentname']
	StudentID = request.form['information']
	conn = sqlite3.connect('E:\\DataBase_assignment\\web_programming\\userlist.db')
	cursor = conn.cursor()
	insertSQL = 'insert into student(Studentname, StudentID) values (\''
	insertSQL += Studentname
	insertSQL += '\',\''
	insertSQL += StudentID
	insertSQL += '\')'
	cursor.execute(insertSQL)
	cursor.execute('select * from student')
	values = cursor.fetchall()
	st = values.__str__()
	conn.commit()
	conn.close()
	return '<h3>A New Studet Added : %s </h3>' % st
	

@app.route('/findstudent', methods=['GET'])
def find_student():
	return  '''<form action="/findstudent" method="post">
				<p><input name="studentname" type="password"></p>
				<p><button type="submit">Find...</button></p>
				</form>'''

@app.route('/findstudent', methods=['POST'])
def findstudent():
	sname = request.form['studentname']
	conn = sqlite3.connect('E:\DataBase_assignment\web_programming\SC.db')
	cursor = conn.cursor()
	selectSQL = 'select StudentID from Student where Studentname = \''
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
