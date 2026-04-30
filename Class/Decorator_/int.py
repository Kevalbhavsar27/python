def check_int(func):
    def wrapper(num):
        if num.isdigit():
            func(int(num))
        else:
            print("Enter only an integer")
    return wrapper


@check_int
def display(num):
    print("Integer is:", num)


n = input("Enter a number: ")
display(n)
