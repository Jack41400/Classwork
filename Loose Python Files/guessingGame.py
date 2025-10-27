# Guessing game OCT 27th

import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

myNumber = random.randint(smaller, larger)
count = 0

while True:
    count += 1
    userNumber = int(input("Enter your number: "))
    if userNumber < myNumber:
        print("Too small, Try again!")
    elif userNumber > myNumber:
        print("Too large, Try again!")
    else:
        print("You guessed it in", count, "tries, Congrats!")
        break
