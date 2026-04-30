total = 0
for num in range(3, 101):

    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        total += num

    #else:
        #print(f"{num} is not a prime number")
print(f"{total}")
