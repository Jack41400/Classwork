# Age eligibility to vote

# import math
age = float(input("Enter your age: "))
# roundedDown = math.floor(age)
if age >= 18:
    print("You are an adult! You are eligible to vote")
elif age <=0:
    print("ERROR: That is impossible. Please enter a number greater than 0.")
else:
    print("You are not eligible to vote, you must be 18 years old!")

"""
age = float(input("Enter your age: "))

if age < 18:
    print( "You are not eligible to vote. You must be 18 years old!")

else:
    print("You are an adult! You are eligible to vote.")
"""
