"""
CISC-121 2023W

Name:   <Joseph Liao>

Student Number: <20366481>

Email:  <22jl41@queensu.ca>

Date: 2023-03-16

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity

"""
from functions4 import *
while True:

    inp1=input('Please enter 1st string ').upper()
    inp2=input('Please enter 2nd string ').upper()

    if (inp1 and inp2).isalpha():
        print(is_anagram(inp1,inp2))
        break
    else:
        print('PLEASE ONLY ENTER ALPHABETS TRY AGAIN')
