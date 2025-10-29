# Rectangular and Triangle Patterns

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

"""
for r in range(rows):
    for c in range(columns):
        print("*",end = " ")

    print()

"""

##################################################

base_size = 8
doubleBase = base_size + 4

print("Its Nepal!!")

for r in range(base_size):
    for c in range(r+1):
        print("*", end = " ")

    print()

for r in range(doubleBase):
    for c in range(r+1):
        print("*", end = " ")

    print()
