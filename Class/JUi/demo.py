from tkinter import *
import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="2424",
    database="keval"
)

cursor = con.cursor()

root=Tk()
root.geometry("400x400")
root.title("My app")



# b1=Button(root, text="Right").pack(side=RIGHT)
# b2=Button(root, text="TOP").pack(side=TOP)
# b3=Button(root, text="LEFT").pack(side=LEFT)
# b4=Button(root, text="BOTTOM").pack(side=BOTTOM)

# l1=Label(root, text="username").grid(row=0, column=0)
# l2=Label(root, text="Password").grid(row=1, column=0)
# l3=Label(root, text="email").grid(row=2, column=0)

# t1= Entry(root).grid(row=0, column=1)
# t2= Entry(root).grid(row=1, column=1)
# t3= Entry(root).grid(row=2, column=1)

# B1= Button(root,text="Submit",width=15).place(x=3, y=0)

def add():
    uname=t1.get()
    password=t2.get()
    phone=t3.get()
    cursor.execute(f"insert into emp(username, password, phone) values ('{uname}', '{password}', '{phone}')")
    con.commit()
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)

    
l1=Label(root, text="username").place(x=100, y=100)
l2=Label(root, text="Password").place(x=100, y=150)
l3=Label(root, text="phone").place(x=100, y=200)

t1= Entry(root)
t1.place(x=200, y=100)
t2= Entry(root)
t2.place(x=200, y=150)
t3= Entry(root)
t3.place(x=200, y=200)
B1= Button(root,text="Submit",width=15,command=add).place(x=200, y=250)


root.mainloop()