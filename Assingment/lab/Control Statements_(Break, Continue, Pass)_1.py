# Program to skip 'banana' in a list using the continue statement

List1 = ['apple', 'banana', 'mango']

print("Fruits in the list:")
for fruit in List1:
    if fruit == 'banana':
        continue  # Skip 'banana' and move to the next iteration
    print(fruit)
