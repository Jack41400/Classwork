# Data Encryption Practice
import math
import random

plainText = input("Enter a one word, lower case password: ") #Takes user input. Only works with lowercase words no spaces.
distance = int(input("Enter the distance value: ")) #lets user choose the distance for the cipher

code = "" #Starts with empty string. This will be the final result.

# for each character in the input text.
for ch in plainText:
    # find the value of the character with ord() function.
    ordvalue = ord(ch)
    # adds distance choosen by the user
    cipherValue = ordvalue + distance
    # if the calculated value is larger than lowercase z (Largest ord() value in cipher)
    if cipherValue > ord('z'):
        # starts back at ord value of a, then adds the input distance with some extrta math to get desired results
        cipherValue = ord('a') + distance - (ord('z') - ordvalue + 1)
    #adds each character after loop finishes to output string
    code += chr(cipherValue)
# prints result
print(code)
                                
#########################################
# Data Decryption Practice

decipher = input("enter your encrypted characters: ")
distance = int(input("Enter the distance value: "))
code = ""

for ch in decipher:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - distance - (ord('a') - ordvalue - 1)
    code += chr(cipherValue)

print(code)
