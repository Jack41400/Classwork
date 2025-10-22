# While Loop testing the password


while True:
    password = input("Enter your password: ")
    if password == "secret123":
        print("PASSWORD ACCEPTED")
        break
    else:
        print("Incorrect Password: Please try again.")


######################################################


correctPassword = "your password"
attempts = 0
maxAttempts = 3

while attempts < maxAttempts:
    userInput = input("Please enter your password: ")

    if userInput == "correctPassword":
        print("PASSWORD ACCEPTED! ACCESS GRANTED:")
        break
    else:
        attempts += 1
        remainingAttempts = maxAttempts - attempts
        if remainingAttempts > 0:
            print("PASSWORD INCORRECT! Remaining Attempts: ", remainingAttempts)
        else:
            print("PASSWORD INCORRECT! You have been locked out of access.")
            break    
if attempts == maxAttempts and userInput != correctPassword:
    print("ACCESS DENIED! Maximum attempts reached.")

