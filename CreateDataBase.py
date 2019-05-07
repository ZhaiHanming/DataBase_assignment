# database
import sqlite3
conn = sqlite3.connect('E:\DataBase_assignment\Assignmet\SC.db')
cursor = conn.cursor()

#用户登录表，用于存放学生和教师的登录信息
#登录账号（学号、教工号），登录密码
cursor.execute('create table User_Student ( SID char(6) primary key , Spassword varchar(16) )')
cursor.execute('create table User_Teacher ( TID char(6) primary key , Tpassword varchar(16) )')

#用户信息表，用于存放学生和教师的基本信息
#学生学号，学生姓名，学生院系，学生年级，已获得学分
cursor.execute('create table Student ( SID char(6) primary key , Sname varchar(20) , Sdepartment varchar(20) , Sage smallint , Scredit int )')
#教师教工号，教师姓名，教师院系，教师职称
cursor.execute('create table Teacher ( TID char(6) primary key , Tname varchar(20) , Tdepartment varchar(20) , Title varchar(10) )')

#课程信息表
#课程编号，课程名称，任课教师，课程最大人数，课程学分
cursor.execute('create table Course ( CID char(6) primary key , Cname varchar(20) , Cteacher char(6) , Cvolume int , Credit int )')

#学生选课表
#选课学生，课程号，课程成绩
cursor.execute('create table SC ( SID char(6) , CID char(6) , Grade int , primary key (SID,CID) , foreign key (SID) references Student (SID) , foreign key (CID) references Course (CID) )')

#填充数据
cursor.execute('insert into User_Student(SID, Spassword) values (\'201701\' , \'password\') ')
cursor.execute('insert into User_Student(SID, Spassword) values (\'201702\' , \'password\') ')

cursor.execute('insert into User_Teacher(TID, Tpassword) values (\'201001\' , \'password\') ')
cursor.execute('insert into User_Teacher(TID, Tpassword) values (\'201002\' , \'password\') ')

cursor.execute('insert into Student(SID, Sname, Sdepartment, Sage, Scredit) values (\'201701\' , \'Alice\' , \'INFO\' , 2 , 50) ')
cursor.execute('insert into Student(SID, Sname, Sdepartment, Sage, Scredit) values (\'201702\' , \'Bob\' , \'ART\' , 1 , 25) ')

cursor.execute('insert into Teacher(TID, Tname, Tdepartment, Title) values (\'201001\' , \'Mike\' , \'INFO\' , \'教授\') ')
cursor.execute('insert into Teacher(TID, Tname, Tdepartment, Title) values (\'201002\' , \'Tom\' , \'ART\' , \'讲师\') ')

cursor.execute('insert into Course(CID, Cname, Cteacher, Cvolume, Credit) values (\'100001\' , \'DataBase\' , \'201001\' , 30 , 2) ')
cursor.execute('insert into Course(CID, Cname, Cteacher, Cvolume, Credit) values (\'100002\' , \'Painting\' , \'201002\' , 20 , 2) ')

cursor.execute('insert into SC(SID, CID, Grade) values (\'100001\' , \'201701\' , 90) ')
cursor.execute('insert into SC(SID, CID, Grade) values (\'100002\' , \'201701\' , 80) ')
cursor.execute('insert into SC(SID, CID, Grade) values (\'100002\' , \'201702\' , 93) ')

conn.commit()
conn.close()
