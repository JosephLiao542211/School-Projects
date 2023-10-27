"""
CISC-121 2023W

Name:   <Joseph Liao>

Student Number: <20366481>

Email:  <22jl41@queensu.ca>

Date: 2023-03-1

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity

"""

from functions import *
def main():
    print(friendship_to_dictionary())
    print("\n")
    name=input("Insert name of friend you want to look up")
    print(allmyfriends(name))
    print("\n")
    (friendship_degree(friendship_to_dictionary()))



main()
