num=int(input("Enter the binary Number: "))
decimal=0
power=0
while num>0:
    rem=num%10
    decimal=decimal+rem*(2**power)
    power=power+1
    num=num//10
print(f"The decimal number is {decimal}")