"""
This application will work as a conversion calculator and complete the following.
1. Prompt the user to input amount of Canadian Dollars.
2. Translate the amount from Canadian Dollars to US Dollars using the conversion rate.
3. Print the ammount calculated rounded to the hundredths.
"""
conversionDirection = input("Please choose your input (CAN or USD)?: ")
capAnswer = capitalize(conversionDirection)
    # $1 CAN = $0.72 USD (10/15/2025)
CANtoUSD = 0.74 # Live rate is actually $0.72
USDtoCAN = 1.40 # Live rate is $1.40
if conversionDirection == "CAN":
        userBalance = float(input("Please enter the total you would like to transfer in Canadian Dollars: "))
        CANtoUSDConversion = userBalance * CANtoUSD
        roundedBalance = round(CANtoUSDConversion, 2)
        finalBalance = "$" + str(roundedBalance)

        print("Your balance in USD would be", finalBalance)

elif conversionDirection == "USD":
        userBalance = float(input("Please enter the total you would like to transfer in US Dollars: "))
        USDtoCANConversion = userBalance * USDtoCAN
        roundedBalance = round(USDtoCANConversion, 2)
        finalBalance = "$" + str(roundedBalance)

        print("Your balance in CAN would be", finalBalance)

else: print("This is not a valid input. Please try again")
