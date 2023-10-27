"""
Plays zoom bingo
Author:  Joseph Liao
Student Number: 20366481
Date:  25th NOV 2022

"""

from __future__ import print_function
import random
import urllib.request

#READS DATA FROM URL
def readWords(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    x = data.split("\n")
    return (x)

b=readWords("https://research.cs.queensu.ca/home/cords2/zoombingo.txt")

# CHECKS FOR DUPLICATES
def dup_check(b):
    while True:
        check=[]
    #GENERATES BOARD FROM READ DATA
        bingo=[[b[random.randint(0,36)],b[random.randint(0,36)],b[random.randint(0,36)]],
           [b[random.randint(0,36)],b[random.randint(0,36)],b[random.randint(0,36)]],
           [b[random.randint(0,36)],b[random.randint(0,36)],b[random.randint(0,36)]]]
        for i in range(len(bingo)):
            for x in range(len(bingo[i])):
                check.append(bingo[i][x])
        for c in list(check):
            if list(check).count(c)!=1:
                check.append("ERROR")
        if "ERROR" not in check:
            return bingo
        else:
            continue



def main(bingo,b):
    print("THIS IS YOUR BOARD ENTER y TO START\n")
    print(*bingo, sep="\n")
    # TRACKS NUMBER OF GUESSES
    guesses=0

    while True:
        yes = input()
        # CHECKS FOR CORRECT INPUT
        if yes == "y":
            guesses+=1
            # GENERATES RANDOM CARD
            card = b[random.randint(0, 36)]
            print("YOUR CARD IS:",('"')+(card)+('"')+"\n")
            # CHECKS IF THE VALUES MATCH THE BOARD AND REPLACES THEM WITH SEEN IF THEY DO
            for t in range(len(bingo)):
                for i in range(len(bingo[t])):
                    if card == bingo[t][i]:
                        bingo[t][i] = "SEEN"
            print(*bingo, sep="\n")

            print("ENTER y TO CONTINUE, ANYTHING ELSE WILL END THE GAME")

        elif yes != "y":
            break
        # CHECKS IF YOUVE WON THE GAME
        if bingo[0][0] == "SEEN" and bingo[0][1] == "SEEN" and bingo[0][2] == "SEEN" or \
                bingo[1][0] == "SEEN" and bingo[1][1] == "SEEN" and bingo[1][2] == "SEEN" or \
                bingo[2][0] == "SEEN" and bingo[2][1] == "SEEN" and bingo[2][2] == "SEEN" or \
                bingo[0][0] == "SEEN" and bingo[0][2] == "SEEN" and bingo[2][2] == "SEEN" "SEEN" and bingo[2][0] == "SEEN":

            print("YOU WIN!!!! and it only took you",str(guesses),"tries")
            break

# RUNNING THE GAME

main(dup_check(b),b)


