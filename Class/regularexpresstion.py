import re

# words= "sun rises in east in"

# # k=re.match("sun",words)
# # k=re.search("in",words)
# # k=re.findall("s",words)
# k=re.finditer("s",words)
# # k=re.split(" ",words)
# print(k)


patten=r'\d{10}$'
number=input("Enter the Number")

if re.match(patten,number):
    print(f"'{number}' is vaild")

else:
    print(f"'{number}' is not vaild")
