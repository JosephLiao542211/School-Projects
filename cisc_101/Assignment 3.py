
"""
This program calculates plays a dice roll game
Author:  Joseph Liao
Student Number: 20366481
Date:  30th Sept 2022
"""
import random
rolls=[]
die2 = 0
die1 = 0
points=0
pointsearned=0

def even():
    for i in range(4):
        die2 = random.randint(1, 6)
        die1 = random.randint(1, 6)
        result = (die2, die1)
        print(result)
        total=die2+die1
        rolls.append(total)
        global pointsearned
    pointsearned=sum(rolls)
    print("you earned: "+str(pointsearned))

def double():
    count = 0
    twin=True
    while twin==True:
        count+=1
        die2 = random.randint(1, 6)
        result=(die2,die1)
        print(result)
        if die2!=die1:
            twin=False
    global pointsearned
    pointsearned=die1+die2+count
    print("you earned: " + str(pointsearned))


def seven():
    for i in range(10):
        die2 = random.randint(1, 6)
        die1 = random.randint(1, 6)
        result = (die2, die1)
        total = die2 + die1
        rolls.append(total)
        print(result)
    global pointsearned
    pointsearned = sum(rolls)+10
    print("you earned: " + str(pointsearned))

Go=False
play=input("To start enter y")
if play=="y":
    Go=True

#main program
while Go==True:

    die2 = random.randint(1, 6)
    die1 = random.randint(1, 6)

    print(die1,die2)

    if die2==die1:
        double()
        points+=pointsearned
        rolls=[]
    elif (die2+die1)%2==0:
        even()
        points += pointsearned
        rolls = []
    elif die2==3 or die1==3 and die2+die1!=7:
        points+=3
        rolls = []
        break
    elif die2+die1==7:
        seven()
        points += pointsearned+10
        rolls = []
    else:points+=die1+die2
    rolls = []

    print("total points:"+str(points))
    print("")
    playagain=input("eneter y to play again")
    if playagain!="y":
        print("your final point total is "+str(points)+" thanks for playing!")
        Go=False




