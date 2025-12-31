Firstnumber = int(input("Enter your Number: "))
Secondnumber = int(input("Enter your Number: "))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")

match choice:
    case '1':
        print(Firstnumber, "+", Secondnumber, "=", Firstnumber + Secondnumber)
    case '2':
        print(Firstnumber,"-",Secondnumber,"=",Firstnumber-Secondnumber)
    case '3':
        print(Firstnumber,"*",Secondnumber,"=",Firstnumber*Secondnumber)
    case '4':
        print(Firstnumber,"/",Secondnumber,"=",Firstnumber/Secondnumber)
    case _:
        print("invalid input")