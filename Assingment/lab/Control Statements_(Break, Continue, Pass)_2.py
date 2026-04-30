# Program to stop the loop once 'banana' is found using the break statement

List1 = ['apple', 'banana', 'mango']

print("Fruits in the list:")
for fruit in List1:
    if fruit == 'banana':
        break  # Stop the loop once 'banana' is found
    print(fruit)

print("Loop stopped at 'banana'")
