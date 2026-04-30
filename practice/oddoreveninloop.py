l=[1,2,3,4,5,6,7,8,9,10,12,55,78,93]

def oe():
    for i in l:
        if l %2==0:
            print("number is even")
        else:
            print("Number is odd")
oe = lambda l: list(filter(lambda x: x % 2 != 0,l))
print(oe(l))