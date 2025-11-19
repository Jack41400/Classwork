# Lets Go Gambling
'''
Creates a text file and uses for loop to generate 500 random numbers
while loop starts to allow replay
Prompts user for total tries
prompts user for a 5 digit number
starts count
grabs a random slice of 5 digits
checks if numbers match user digits
if numbers match, prints fanfare and congrats. Asks to play again or end the while loop
if numbers do not match ask to go again
once count reaches user tries, prompt user tries are out and asks to go again
overwrites a new set of 500 to text file and restarts loop
'''

import random
import sys

def generate_random_numbers(filename):
    with open(filename, 'w') as f:
        for _ in range(500):
            random_number = random.randint(10000, 99999)
            f.write(f"{random_number}\n")

def get_valid_number(prompt):
    while True:
        user_input = input(prompt).strip()
        if len(user_input) == 5 and user_input.isdigit():
            return user_input
        print("Please enter a valid 5-digit number.")

def main():
    filename = "random_numbers.txt"
    generate_random_numbers(filename)

    while True:
        tries - int(input("Enter total tries: ").strip())
        user_number = get_valid_number("Enter a 5-digit number: ").strip()

        count = 0
        found = False
        with open(filename, 'r') as f:
            for line in f:
                if count >= tries:
                    break
                count += 1
                selected_number = line.strip()
                print(f"Try {count}: The selected number is {selected_number}")

                if user_number == selected_number:
                    found = True
                    print("*** CONGRATULATIONS!!!! *** You guessed correctly")
                    break
                else:
                    print(f"Tries are out! The correct number was {Sselected_number}")
                    replay = input("Do you want to play again? (yes/no): ").strip().lower()
                    if replay != 'yes':
                        print("Thanks for playing! Goodbye!")
                        sys.exit()

                generate_random_numbers(filename)

if __name__ == "__main__":
    main()
