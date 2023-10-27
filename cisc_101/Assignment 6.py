"""
Wordle esque game
Author:  Joseph Liao
Student Number: 20366481
Date:  10/31/2022
"""

import random

#chooses words
def chooseWord():


    validWords = ["could", "smile", "ultra", "extra", \
                  "beacon", "hearts", "cap", "wordle", \
                  "computing", "program", "python"]

    wordPosition = random.randint(0, 5)

    return validWords[wordPosition]

#checks the letters
def checkLetters(secretWord, userWord):
    final_results=[]



    for i in list(userWord):
        results = []
        if i in list(secretWord):

            results.append(i)
            results.append("is in the incorrect position")

            for l in list(secretWord):
                if i==l and list(userWord).index(i)==list(secretWord).index(l):
                    results[1]=("is in the right position")
        else:
            results.append(i+" is not in the secret word")

        final_results.append(" ".join(results))
    for r in final_results:
        print(r)


#checks for duplicates
def checkForDuplicates(userWord):
    check=[]
    for i in list(userWord):
        if (list(userWord)).count(i) != 1:
            check.append("t")
        else:
            check.append("f")
    if "t" in check:
        return True
    else:
        return False

#runs the game
def play(secretWord):

    print(secretWord)

    for i in range(6):
        while True:

            userword=input("Guess #"+str(i+1))
            if secretWord == userword:
                print(userword + " is right!!! You Won")
                return
            if checkForDuplicates(userword)==False:
                break

            print("Invalid input(contains duplicates) please try again")

        checkLetters(secretWord,userword)

#User interface
def main():

    print(" A word will be selected (by the program) from a random list of 5 lettered words.\n"
          "Guess words to to figure out the secret word! You have 6 guesses:\n"
          "when you are ready enter start.\n")
    begin=input("Enter start:")
    while True:
        if begin=="start":
            play(chooseWord())
            break
        else:
            print("invalid input")


main()