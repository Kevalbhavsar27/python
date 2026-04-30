def Gen() :
    yield "Keval"
    yield "Uday"
    yield "Raj"
    yield "Dev"
    yield "Bhanu"
k=Gen() 
print(next(k))
print(next(k))
print(next(k))