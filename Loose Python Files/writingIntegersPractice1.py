# Writing numbers to a file
# Creates 'integers' text file and overwrites with 500 random numbers
# Default location is shared folder with this .py file

import random
import math

f = open("integers.txt", "w")
for count in range(500):
    number = random.randint(1,500)
    f.write(str(number) + '\n')
f.close()
