import sqlite3

conn= sqlite3.connect("data.db")
# qry="create table Student(id primary key,name varchar(20),email varchar(20))"
#qry="insert into Student values(1,'Keval','keval11@gmail.com')"
# qry= "update Student set name='King' where id=1"
# qry="delete from Student where id=1"
# conn.execute(qry)
conn.commit()
# data=conn.execute("select * from student")
# for i in data.fetchall():
#     print(i)
