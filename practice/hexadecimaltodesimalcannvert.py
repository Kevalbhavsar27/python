number = int(input("Enter the Hex-style number: "))
sum_decimal = 0
temp = number
power = 0  

while temp > 0:
    digit = temp % 10 
    sum_decimal = sum_decimal + (digit) * (16 ** power)
    temp = temp // 10
    power += 1
print(f"The Decimal value of your input is: {sum_decimal}")