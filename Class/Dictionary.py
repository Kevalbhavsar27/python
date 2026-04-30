a = {
  "Name": "Keval",
  "Email": "keval123@gmail.com",
  "Place": "Surat",
  "name": "Uday",
  "languages": ["Python", "Java", "C++"],
  "hobbies": ("Reading", "Traveling", "Coding")

}
print(a["name"])
#--------------------------------------------------------------------------------
#if dont get value so output will be show none
print(a.get("Name"))

#Dictionary items are ordered, changeable, and do not allow duplicates.



#only gett keys
print(a.keys())

#only getting values
print(a.values())



#for loop

for i in a:
    print(i)

for i in a.values():
    print(i)

for i,j in a.items():
    print(i,j)



#change value


b={
    "Name": "Keval",
    "Email": "kkkkk@gmail.com"
}
b["Name"]= "Uday"
b.update(b)
print(b)
#add item
b["Email"]= "Surat"
print(b)

#remove item



