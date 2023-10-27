""""
CISC-121 2023W

Name:   <Joseph Liao>

Student Number: <20366481>

Email:  <22jl41@queensu.ca>

Date: 2023-01-16

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity

"""

import random
import math

a=random.randint(0,100) #generates random integer between 0 and 100 and assigns it to a
b=random.randint(0,100) #generates random integer between 0 and 100 and assigns it to b
largest_value=max(a,b) #assigns the largest value among a and b to largest_value
smallest_value=min(a,b) #assigns the smallest value among a and b to smallest_value

def validcheck(l,s): #defining a function validcheck which takes l and s as argument
    if 10<=l-s<=50: #checks if difference of l and s is between 10 and 50
        print("valid pair")
        return "valid"
    else:
        print("invalid pair")
        return

def adjustments(largest_value,smallest_value): #defining a function adjustments which takes largest_value and smallest_value as argument
    list=[]
    while True:
        if validcheck(largest_value,smallest_value)!="valid":
            if largest_value-smallest_value>50:
                largest_value=max(math.ceil(largest_value/3),smallest_value) #adjusting the value of largest_value
                smallest_value=min(math.ceil(largest_value/3),smallest_value) #adjusting the value of smallest_value
            if largest_value-smallest_value<10:
                largest_value=largest_value*2 #adjusting the value of largest_value
        else:
            break
    list.append(int(smallest_value))
    list.append(int(largest_value))
    return list

x=(adjustments(largest_value,smallest_value))
rangelist=[*(range(x[0],x[1]))] #generating a list of range between x[0] and x[1]
print("\n")
for i in rangelist: #iterating through the range list
    what_to_print=[]
    if i%5==0:
        what_to_print.append("apple ") #adding apple to what_to_print list if i is divisible by 5
    if i%7==0:
        what_to_print.append("pen ") #adding pen to what_to_print list if i is divisible by 7
    if "3" in list(str(i)):
        what_to_print.append("pineapple") #adding pineapple to what_to_print list if 3 is present in i
    if what_to_print==[]:
        what_to_print.append(i) #if nothing is added to what_to_print list, add i to it
    print(*what_to_print) #printing the list
