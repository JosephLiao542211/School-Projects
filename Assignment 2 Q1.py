"""
This program calculates the price of the customers items as well as tax and tips
Author:  Joseph Liao
Student Number: 20366481
Date:  24th Sept 2022
"""
#menu
print("1 Chicken wings ($10.00)\n"
      "2 Chicken Tenders ($14.50)\n"
      "3 Chicken Burger ($7.00)\n"
      "4 Chicken Family Combo($28.75)\n"
      "5 Chicken Slurpee ($2.00)")

#tipping syestem
def tips2():
    while True:
        while True:
            typ = str(input("Would you like to % or set value? (precent/set)"))
            if typ in ("precent", "set"):
                break
            print("invalid input.")

        if typ == ("precent"):
            precent = float(input("how much would you like to tip %"))
            total = str(round(float(costaftertax * ((precent / 100) + 1)), 2))
            print("That will be " + total + " Thank you so much!")
            break
        else:
            set = float(input("how much would you like to tip $"))
            total = str(round(costaftertax + set, 2))
            print("That will be $" + total + " Thank you so much!")
            break


#Asks the customer if they want to tip
def tips():
    valid=False
    while True:
        # main program
        while True:
            tip= str(input("Would you like to tip? (y/n)"))
            if tip in ("y","n"):
                break
            print("invalid input.")
        if tip == 'y':
            tips2()
            break
        else:
            stringcost=str(costaftertax)
            print("That will be $ "+ stringcost +" Thank you so much!")
            break

while True:
    # main program
    while True:
        order = str(input("Enter the number corresponding to the item that you would like to purchase "))
        if order in ("1","2","3","4","5"):
            break
        print("invalid input.")

    if order == "1":
        cost=float(10.00)
        costaftertax=round(cost*1.05)
        print("that will be $10 ")
        print("Your cost after tax will be $" + str(costaftertax))
        tips()
        break

    elif order == "2":
        cost = float(14.50)
        costaftertax = round(cost * 1.05,2)
        print("that will be $14.50 ")
        print("Your cost after tax will be $" + str(costaftertax))
        tips()
        break

    elif order == "3":
        cost = float(7.00)
        costaftertax = round(cost * 1.05,2)
        print("that will be $7.00 ")
        print("Your cost after tax will be $" + str(costaftertax))
        tips()
        break

    elif order == "4":
        cost = float(28.75)
        costaftertax = round(cost * 1.05,2)
        print("that will be $28.75 ")
        print("Your cost after tax will be $"+str(costaftertax))
        tips()
        break

    elif order == "5":
        cost = float(3.00)
        costaftertax = round(cost * 1.05,2)
        print("that will be $3.00 ")
        print("Your cost after tax will be $" + str(costaftertax))
        tips()
        break

