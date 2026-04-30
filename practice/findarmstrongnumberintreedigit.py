number =int(input("Enter the tree Number:"))
sum = 0
temp =number
while temp >0:
    digit = temp%10
    sum = sum + digit **3
    temp = temp //10
    if number == sum:
        print(f"{number}is Armstrong number")
    else:
        print(f"{number} is not armstrong number")