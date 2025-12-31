marks = int(input("Enter your marks: "))

if marks >= 81 and marks <= 100:
    print("Grade: A+")
elif marks >= 71 and marks <= 80:
    print("Grade: A")
elif marks >= 51 and marks <= 70:
    print("Grade: B")
elif marks >= 35 and marks <= 50:
    print("Grade: C")
elif marks >= 0 and marks <= 34:
    print("Fail")
else:
    print("Invalid marks")
