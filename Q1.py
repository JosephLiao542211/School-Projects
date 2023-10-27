"""
This program calculates the amount of cupcakes need for the user to bring to the party given the amount of guests and pets
Author:  Joseph Liao
Student Number: 20366481
Date:  16th Sept 2022
"""
print("Please enter the number of people who will attend (including you):")
people=int(input())
print("How many of these people have pets?:")
pets=int(input())
cupcakes=people*2+pets+4
cupcake=str(cupcakes)
print("You should bake "+cupcake+" cupcakes")
