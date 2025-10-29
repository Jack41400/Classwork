import math

while True:
    checkNumber = (input("What number do you want to stop at? "))
    if checkNumber == "done":
        break
    
    inputNumber = float(checkNumber)
    stopNumber = (inputNumber + 1)/2
    roundNumber = math.ceil(stopNumber)
    counter = 0

    for evenNumbers in range(1, roundNumber):
        counter += 1
        print(evenNumbers*2)

    print("There are", counter, "even numbers")

