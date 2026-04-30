def check_char(func):
    def wrapper(num):
        if num.isalpha():
            func(str(num))
        else:
            print("Enter only a character")
    return wrapper


@check_char
def display(num):
    print("Character is:", num)


n = input("Enter a character: ")
display(n)
