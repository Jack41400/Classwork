""" This application will work as a conversion calculator and complete the following.

1. Prompt the user to input amount of Canadian Dollars.
2. Translate the amount from Canadian Dollars to US Dollars using the conversion rate.
3. Print the ammount calculated rounded to the hundredths.

"""
conversionDirection = input("Please choose your input (CAN or USD)?: ") 
userBalance = float(input("Please enter the total you would like to transfer in Canadian Dollars: "))

# $1 CAN = $0.72 USD
CANtoUSD = 0.74 # Live rate is actually $0.72
USDtoCAN = 1.40 # Live rate is $1.40
CANtoUSDConversion = userBalance * CANtoUSD
finalBalance = "$" + str(CANtoUSDConversion)

print("Your balance in USD would be", finalBalance)
