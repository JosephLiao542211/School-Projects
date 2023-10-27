"""
CISC-121 2023W

Name:   <Joseph Liao>

Student Number: <20366481>

Email:  <22jl41@queensu.ca>

Date: 2023-02-1

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity

"""
def all_odd_or_even(arg):
    # check if length of arg is greater than or equal to 1,
    # all elements are integers, and all elements are either even or odd
    if len(arg)>=1 and ([True for i in arg if (type(i)==int)]) \
            and (all(i%2==0 for i in arg) or all(i%2==1 for i in arg)):
        print("True")
    else:
        print("False")

def friendship_to_dictionary():
    #creates dictionary from friendship txt
    d={}
    allname=[]
    f=open("friendship.txt")
    for row in f:
        row = row.strip().split()
        allname.append(row)

    for set in allname:
        if set[0] not in d:
            d[set[0]]=set[1]
        else:
            d[set[0]]=[d[set[0]],set[1]]

    return (d)

def allmyfriends(friend):
    #finds all the friends of a given friend
    dictionary=friendship_to_dictionary()
    friend_count=[]
    if type(dictionary[friend])==str:
        friend_count.append((dictionary[friend]))
    else:
        for x in range(len(dictionary[friend])):

         friend_count.append((dictionary[friend][x]))

    for i in dictionary:
        if friend in dictionary[i]:
            friend_count.append(i)

    return friend_count



def friendship_degree(dictionary):
    #prints the number of friends and who they are of everyone in friendship txt
    for i in dictionary:
         print(i,"has",len(allmyfriends(i)),"friends","("+", ".join(allmyfriends(i))+")")