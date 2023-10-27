""""
CISC-121 2023W

Name:   <Joseph Liao>

Student Number: <20366481>

Email:  <22jl41@queensu.ca>

Date: 2023-02-1

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity

"""
from functions import *

def main():
    print("You will insert numbers if they are all even or odd "
          "they will return True otherwise they will return False")
    numlist=[]
    numt=0
    start=(input("please enter yes to start the activity"))
    # start the activity if user inputs "YES"
    if start.upper()=="YES":
        while True:
            num=(input("please enter numbers"))
            try:
                numt==int(num)
            except:
                print("invalid input try again")
            if type(numt)==int:
                numlist.append(int(num))
                cont=input("enter yes to continue to input numbers "
                           "anything else to complete activity")
                if cont.upper()=="YES":
                    continue
                else:
                    break

        all_odd_or_even(numlist)
    else:
        return


main()


