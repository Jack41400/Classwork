# Grades exercise on pg 67

grade = int(input("Enter your numeric grade: "))

if grade >= 0 and grade <= 100:
    if grade > 89:
        letter = "A"
    elif grade > 79:
        letter = "B"
    elif grade > 69:
        letter = "C"
    else:
        letter = "F"

    print("Your letter grade is", letter)

else:
    print("ERROR: GRADE MUST BE BETWEEN 0 AND 100")
