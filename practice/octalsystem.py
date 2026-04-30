num=int(input("Enter the decimal Number"))
octal=""

while num>0:
    rum = num%8
    octal =str(num)+octal
    num = num//8
print(f"The octal number is {octal}")
