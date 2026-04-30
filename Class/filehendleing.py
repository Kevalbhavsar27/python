# f= open("test.txt",'w')
# f.write("Writeing something in file......")
# # f.writelines(["Hello Python\n","Hello tops"])
# f.close()

# f= open("test.txt",'r')
# while True:
#     a = f.readline()
#     if not a:
#         break
#     if "Hello" in a:
#         print(a)
# f.close()

# f= open("test.txt",'r')
# while True:
#     a = f.readline()
#     if not a:
#         break
#     print(len(a))
# f.close()


# while True:
#     f=open("test.txt","r")
#     d=f.readline()
#     print(d)
#     if not d:
#         break

# with open("test.txt","r") as f:
#     print(f.tell())
#     f.seek(20)
#     a=f.read()
#     print(a)
#     print(f.tell())

# mode :r,w,a,r+,w+,a+,rb,wb

# with open("home.txt","r+")as f:
#     f.write("write someing")
#     f.seek(2)
#     d=f.read()
#     print(d)

# with open("image.jpeg","rb") as f:
#     v=f.read()
#     print(v)

import json
d={"Name":"Keval","email":"Keval@gmail.com"}
with open("data.json",'w')as f:
    json.dump(d,f)