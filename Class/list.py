a= [10,20,30,40,50] #list
b= (10,20,30,40,50) #tuple
c= {10,20,30,40,50} #set

#print(a)
print(b)
print(c)
# append the list
# print(len(a))
a.append(80)
print(a)

print(type(a))

# remove item using pop for using valuse of list
a.remove(80)
print(a)

# remove item using pop for using 1234 index
a.pop(1)
print(a)