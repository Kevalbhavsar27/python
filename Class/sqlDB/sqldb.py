import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="2424",
    
)

cursor = con.cursor()
cursor.execute("create database Keval_db")
con.commit()
# cursor.execute("create database 22dec_python")

