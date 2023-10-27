
"""
This program calculates converts a numerical grade input into its respective alphabetical equivalent
Author:  Joseph Liao
Student Number: 20366481
Date:  24th Sept 2022
"""
#checks if input is valid
while True:
    Grade = float(input())
    if 0 <= Grade <= 100:
        break
    print("Invalid input try again")

def Grade_converter():
#function that finds the corresponding grade value
    if 67 <= Grade <= 69:
        print("C+")
    elif (Grade > 69):
        if (77 <= Grade <= 79):
            print("B+")
        elif (Grade > 79):
            if (85 <= Grade < 90):
                print("A")
            elif (Grade < 85):
                print("A-")
            else:
                print("A+")
        else:
            if (72 < Grade < 77):
                print("B")
            elif (Grade <= 72):
                print("B-")
    else:
        if (57 <= Grade <= 59):
            print("D+")
        elif (Grade > 59):
            if (60 <= Grade <= 62):
                print("C-")
            elif (Grade > 62):
                print("C")
        else:
            if (53 <= Grade <= 56):
                print("D")
            elif (50 <= Grade < 53):
                print("D-")
            else:
                print("F")
#runs the function
Grade_converter()



