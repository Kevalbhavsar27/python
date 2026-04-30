num=int(input("Enter the decimal number: "))
res=''

while num>0:
    res=str(num & 1)+res
    num=num>>1   
print(f"The binary number is {res}")