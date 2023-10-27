from __future__ import print_function
"""
Final exam
Author:  Joseph Liao
Student Number: 20366481
Date:  11th NOV 2022
"""

'''I certify that this work has been done solely by myself and that 
I have not communicated with anyone during this examination using any means of 
communication.  I understand that a breach of academic 
integrity on this final exam will result in a failure in the course and 
possible additional consequences.'''

guestlist = {"Raisa": ["pizza", "cookies", 3], "Susan": ["salad", 2],
             "Jia": ["ice cream", 0], "Val": ["cake", 2],
             "Brian": ["pasta", "cheese", "crackers", 2],
             "Chandra": ["burgers", "buns", 3]}
powleyGuests = ["Isla", "Susan", "Ellen", "Jia", "Raisa", "Chandra", "Wendy"]

test=["pizza", "cookies", 3]

def name_print(guestlist):
    b=[]
    #loops through the guestlist and formats it
    for i in guestlist:
        b.append((i+" is bringing "+" and ".join(guestlist[i][:-1])+"."))
    return (b)

def totalguest(guestlist):
    total=[]
    #loops through the guestlists and finds the last value adding it to the total
    for i in guestlist:
        total.append(guestlist[i][-1]+1)
    #sums the total and returns it in the proper format
    return "There is",sum(total),"people attending"

'''returns a list of the names of people that are in powleyGuests 
but that are not in the guestlist. '''

def listings(guestlist,powleyGuests):
    guestlistnames = []
    guestsnotincluded=[]
    #creates a list with just the values of a dictionary
    for names in guestlist:
        guestlistnames.append(names)
    #loops through the powleyguest list and adds the values which are not in the guestlist into guestsnotincluded
    for i in powleyGuests:
        if i not in guestlistnames:
            guestsnotincluded.append(i)

    return guestsnotincluded


def listintersection(guestlist,powleyGuests):
    guestlistnames=[]
    for names in guestlist:
        guestlistnames.append(names)
    for i in powleyGuests:
        if i not in guestlistnames:
            guestlist[i]=["tbd",0]

# almost the same fucntion as listing but instead of adding the
# names to another list adds it to guest list with the appropriate values

    return guestlist



def food(foodlist):

    # breaks the word up
    t = []
    for i in foodlist[:-1]:
        t.append(list(i))
    for g in t:
        # checks for the conditions
        if (foodlist[-1]>0 and (len(list(foodlist[0]))>3 or list(foodlist[0])[0]=="p")) \
                or (foodlist[-1] == 0 and ("s" and "p" in g)):
            return ("True")
        else:
            return ("False")

def addguest(powleysguestlist):

    guest=[]
# friendly UI
    totalguests=int(input("please enter how many guests you want to add"))

# runs until there is no duplicates
    while len(guest)<totalguests:
        name=input("please input name of guest #"+str(len(guest)+1))
        if name in powleysguestlist:
            print("please try again")
        else:
            guest.append(name)
            powleysguestlist.append(name)

    return powleysguestlist

'''The main function'''

def main(g,p):
    # composites all the functions and formats them nicely
    print(*name_print(g),sep="\n")
    print("\n",*totalguest(g),"\n")
    print("The people not in the guest list but is on Powleys list are:",listings(g,p),"\n")
    g=listintersection(g,p)

    print("New list:")
    print(*name_print(g),sep="\n")
    print("\n")
    for i in g:
        print(food(g[i]))
    print("\n")

    print("The new powleys guest list is",addguest(p))

main(guestlist,powleyGuests)



