a={"apple", "banana", "cherry", False, 0}
b=set([1,2,3,4,5])
print(b)
print(a)
print(len(a))



c={"apple", "banana", "cherry",}
if 10 in c:
    print(c)
else:
    print("no, 10 is not present")


d={"apple", "banana", "cherry"}
dd={"google", "microsoft", "apple"}
d.remove("apple")
#d.update(dd)
print(d)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


set111 = {"apple", "banana", "cherry"}
set22 = {"google", "microsoft", "apple"}

set11 = set111.difference(set22)

print(set11)



a1= {"apple", "banana", "cherry"}
b1 = {"google", "microsoft", "apple"}

c1 = a1.symmetric_difference(b1)

print(c1)

