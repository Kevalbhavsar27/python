# Program to manipulate and print strings using various string methods

str1 = "  Hello, World!  "
str2 = "python programming"
str3 = "apple,banana,mango"

print("Original Strings:")
print(f"str1 = '{str1}'")
print(f"str2 = '{str2}'")
print(f"str3 = '{str3}'")
print("\n" + "=" * 60 + "\n")

# 1. Case conversion methods
print("1. Case Conversion Methods:")
print("-" * 60)
print(f"str1.upper() = '{str1.upper()}'")
print(f"str2.lower() = '{str2.lower()}'")
print(f"str2.capitalize() = '{str2.capitalize()}'")
print(f"str2.title() = '{str2.title()}'")
print(f"str2.swapcase() = '{str2.swapcase()}'")
print()

# 2. Whitespace removal methods
print("2. Whitespace Removal Methods:")
print("-" * 60)
print(f"str1.strip() = '{str1.strip()}'")
print(f"str1.lstrip() = '{str1.lstrip()}'")
print(f"str1.rstrip() = '{str1.rstrip()}'")
print()

# 3. Search and replace methods
print("3. Search and Replace Methods:")
print("-" * 60)
print(f"str1.replace('World', 'Python') = '{str1.replace('World', 'Python')}'")
print(f"str3.replace(',', ' - ') = '{str3.replace(',', ' - ')}'")
print(f"str1.find('World') = {str1.find('World')}")
print(f"str1.count('l') = {str1.count('l')}")
print()

# 4. Split and join methods
print("4. Split and Join Methods:")
print("-" * 60)
words = str3.split(',')
print(f"str3.split(',') = {words}")
print(f"' | '.join(words) = '{' | '.join(words)}'")
print()

# 5. Checking methods
print("5. String Checking Methods:")
print("-" * 60)
print(f"'123'.isdigit() = {'123'.isdigit()}")
print(f"'abc'.isalpha() = {'abc'.isalpha()}")
print(f"'abc123'.isalnum() = {'abc123'.isalnum()}")
print(f"str1.startswith('  Hello') = {str1.startswith('  Hello')}")
print(f"str1.endswith('!')  = {str1.endswith('!')}")
print()

# 6. Formatting methods
print("6. Formatting Methods:")
print("-" * 60)
name = "Alice"
age = 25
print(f"Using f-string: Hello {name}, you are {age} years old")
print("Using format(): Hello {}, you are {} years old".format(name, age))
print(f"str2.center(30, '-') = '{str2.center(30, '-')}'")
print(f"str2.ljust(30, '.') = '{str2.ljust(30, '.')}'")
print(f"str2.rjust(30, '.') = '{str2.rjust(30, '.')}'")
print()

# 7. Index and position methods
print("7. Index and Position Methods:")
print("-" * 60)
print(f"str1.index('World') = {str1.index('World')}")
print(f"str1.rfind('l') = {str1.rfind('l')}")
print(f"len(str1) = {len(str1)}")
print()

# 8. Advanced string methods
print("8. Advanced String Methods:")
print("-" * 60)
test_str = "hello123world"
print(f"'{test_str}'.isalnum() = {test_str.isalnum()}")
print(f"'  '.isspace() = {'  '.isspace()}")
print(f"str2.partition(' ') = {str2.partition(' ')}")
print(f"str3.count(',') = {str3.count(',')}")
