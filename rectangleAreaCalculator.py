# This a rectangle area calculator

print("RECTANGLE AREA CALCULATOR")
length = float(input("Please enter the length of the rectangle: "))
width = float(input("Please enter the width of the rectangle: "))
area = length * width

if length == width: print("This is a Square! The area is", area, "units/sq"),
elif area == 0: print("This is not a rectangle!", area, "units/sq"),
elif area < 0: print("You can't have a negative measurement, run the program again!"),
else: print("The area of the rectangle is", area, "units/sq")


