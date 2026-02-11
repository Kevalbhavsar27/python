# Program to demonstrate string slicing

str1 = "Hello, World!"

print("Original String:", str1)
print("-" * 50)

# 1. Basic slicing - extract characters from index 0 to 4
print("1. str1[0:5]:", str1[0:5])  # Output: Hello

# 2. Slicing from the beginning
print("2. str1[:5]:", str1[:5])  # Output: Hello

# 3. Slicing to the end
print("3. str1[7:]:", str1[7:])  # Output: World!

# 4. Negative indexing - last character
print("4. str1[-1]:", str1[-1])  # Output: !

# 5. Negative slicing - last 6 characters
print("5. str1[-6:]:", str1[-6:])  # Output: World!

# 6. Slicing with step
print("6. str1[::2]:", str1[::2])  # Output: Hlo ol!

# 7. Slicing with negative step (reverse)
print("7. str1[::-1]:", str1[::-1])  # Output: !dlroW ,olleH

# 8. Slicing a range with step
print("8. str1[0:10:2]:", str1[0:10:2])  # Output: Hlo o

# 9. Extract middle part
print("9. str1[7:12]:", str1[7:12])  # Output: World

# 10. Every third character
print("10. str1[::3]:", str1[::3])  # Output: Hlwrd

