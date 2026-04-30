class Student:
    id=101
    name="Keval Bhavsar"
    email="keval111@gmail.com"
 cv

    def to_write(self):
        print(self.id,self.name,self.email)

s1=Student()
s1.to_write()
s1.email="kevalbhavsar@gmail.com"
s1.id="102"
s1.name="xyz"
s1.to_write()