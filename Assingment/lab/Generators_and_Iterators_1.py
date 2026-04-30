# Generator function to generate first 10 even numbers

def even_numbers():
    for i in range(1, 11):
        yield i * 2

# Using the generator
for num in even_numbers():
    print(num)
