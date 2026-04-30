# Check blood donation eligibility using nested if

age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood (minimum 50 kg required).")
else:
    print("You are not eligible to donate blood (must be at least 18 years old).")
