
"""

This program provides a framework to ORDERING SYESTEM
Author:  Joseph Liao
Student Number: 20366481
Date:  02 DEC 2022

"""

from __future__ import print_function
import math
import urllib.request

def readWords(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    x = data.split("\n")
    return (x)

def order_lookup(data):
    orderid=input("Please input id of order you want to look up ")
    for i in range(len(data)):
        if data[i][0]==orderid:
            for x in range(1,len(data[i])):
                if data[i][x]==(data[i][-1]):
                    print("price=",data[i][x],"$")
                elif x<(len(data[i])):
                    print("item",x,data[i][x])



def change_order(data):
    new=[]
    orderid = input("Please input id of order you want to change ")
    for i in range(len(data)):
        if data[i][0] == orderid:
            while True:
                neworder=input("Please input new orders pressing enter after each item, enter DONE once you are done inputing your order")
                if neworder=="DONE":
                    break
                else:
                    new.append(neworder)
            new.insert(0,data[i][0])
            new.append(data[i][-1])
            print("Your new order is:",new)
            data[i]=new
    return data

def donutdetection(data):
    for i in range(len(data)):
        for x in data[i]:
            if x=="Donut":
                print(data[i][0])

def orderremoval(data):

    order = input("Please input id of order you want remove")
    for i in data:
        if i[0] == order:
            data.remove(i)

    return data

def cost(data):
    nonuts=[]
    for i in range(len(data)):
            if "Donut" in data[i]:
                continue
            else:
                nonuts.append(float(data[i][-1]))

    print(math.fsum(nonuts))

def main(smalldata):
    print("To Find the cost and items of an Order enter 1\n"
          "To remove an order enter 2\n"
          "To find orders that contain a Donut enter 3\n"
          "To find the total cost of orders that do NOT contain Donuts enter 4\n"
          "To change an order enter 5\n")
    while True:
        b=input()
        if b == "1":
            order_lookup(smalldata)
        elif b=="2":
            smalldata=orderremoval(smalldata)
            print("Your new order is",*smalldata,sep="\n")
        elif b=="3":
            donutdetection(smalldata)
        elif b=="4":
            cost(smalldata)
        elif b=="5":
            smalldata=change_order(smalldata)
            print("Your new order is", *smalldata, sep="\n")

bigdata=readWords("https://research.cs.queensu.ca/home/cords2/timHortons.txt")
bigdata.pop()
smalldata=[]
for i in bigdata:
    x=list(i)
    if x[-1]==" ":
        x.pop()
        smalldata.append(("".join(x)).split(" "))
    else:
        smalldata.append(i.split(" "))

print("Your current orders are:")
print(*smalldata,sep="\n")

main(smalldata)





