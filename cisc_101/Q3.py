"""
Author:  Joseph Liao
Student Number: 20366481
Date:  16th Sept 2022
"""

print("Enter 'your name' to start")
start_name=input()

#starts the program
if start_name!=(""):
    (function)=True
else:
    (function)=False

if function==True:

#finds the number of items that the customer requires and subsequentley prompts the correct amount of input options
    prices = []
    items = int(input("Please enter the number of items that you purchased: "))

    for i in range(items):
        itemnum=str(i+1)
        price = float(input("Enter the price of item "+itemnum+": "))
        prices.append(price)

#Calculates the total cost and prints the results to the customer

total_value=sum(prices)
stringTV=str(total_value)
print("The total value of your order= $"+stringTV)
after_tax=round(total_value*1.13,2)
stringAT=str(after_tax)
print("Your total after tax = $"+stringAT)
print("Have a great day!"+start_name)








