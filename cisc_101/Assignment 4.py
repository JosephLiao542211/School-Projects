"""
This program does a variety of things
Author:  Joseph Liao
Student Number: 20366481
Date:  24th Sept 2022
"""
import math

#currency conversion
def currency(cad):
    return round((cad*(5.19)),2)
#number calculation
def numcalc(n,m):
    if 0<(m-n)<=3:
        return math.pow((math.prod(range(n,m+1))),2)
    else:
        return 0
#poem
def poem(name):
    print("Loops were crazy,\nWhat are functions about? \n"+name+",you can do this \nJust stick it out!")


#main function
menu=True
print("Welcome how can I help you today\n"
                            "For a custom poem please enter 1\n"
                            "For a numerical Calculation please enter 2\n"
                            "For converting from Canadian to Chinese Currency please eneter 3\n"
                            "To Exit enter 4\n")
while menu==True:
    while True:
        functionchoice = str(input("Make slection here"))
        if functionchoice in ("1", "2","3","4"):
            break
        print("invalid input.")

    if functionchoice=="1":
        name=str(input("please enter your name"))
        poem(name)
        menu=False
    if functionchoice=="2":
        n = int(input("please enter lower bound of calculation:"))
        m = int(input("please enter upper bound of calculation:"))
        print(numcalc(n,m))
        menu=False
    if functionchoice=="3":
        cad=float(input("please enter the amount fo Canadian currency you want to convert"))
        print(str(currency(cad))+"¥")
        menu=False
    if functionchoice=="4":
        menu=False




