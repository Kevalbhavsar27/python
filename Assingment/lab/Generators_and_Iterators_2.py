<<<<<<< HEAD
# Custom iterator to iterate over a list of integers

class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# List of integers
num_list = [10, 20, 30, 40, 50]

# Using the custom iterator
iterator = NumberIterator(num_list)

for num in iterator:
    print(num)
=======
# Custom iterator to iterate over a list of integers

class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# List of integers
num_list = [10, 20, 30, 40, 50]

# Using the custom iterator
iterator = NumberIterator(num_list)

for num in iterator:
    print(num)
>>>>>>> 7f273e04a8525ac20b4e2ba4e90098c9d7af5323
