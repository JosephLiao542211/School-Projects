import urllib.request
"""
This program will allow the user to play bingo, as called from different functions that take
the different cards as words from a txt file provided
Author: Tataru, Alex
Student Number: 20337641
Date:  Nov 2022
"""



def readtxt(url):
    """ Function takes the parameter of the url
    provided from the assignment and reads the
    lives that are in the .txt file and returns
    the new txt as a list """
    # Empty string placeholder for the list of lines
    orderlist = []

    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')

    # Adds line to list after each line '\n'
    orderlist += data.split('\n')
    # Removes final line which is empty
    orderlist.remove(orderlist[-1])
    return orderlist



def priceprint(orderlist):

    list = []
    orderdictionary = {}

    for i in range(len(orderlist)):
        x = orderlist[i].split()
        list.append(x)


    for i in range(len(list)):
        for word in range(len(list)):
            orderdictionary[list[i][0]] = float(list[i][-1])

    return orderdictionary



def foodprint(orderlist):

    list = []
    orderfood = {}

    for i in range(len(orderlist)):
        x = orderlist[i].split()
        list.append(x)


    for i in range(len(list)):
        for word in range(len(list)):
            orderfood[list[i][0]] = ' '.join(list[i][1:-1])

    return orderfood



def getorder(id, orderlist):

    id = str(id)

    f = foodprint(orderlist)
    p = priceprint(orderlist)

    food = f[id]
    price = p[id]

    order = str('Your order given id: ' + id + ' is a ' + food + ' which will cost $' + str(price))

    return order


def changefoodorder(id, newfood, foodprint):
    id = str(id)
    newfood = str(newfood)

    foodprint[id] = newfood

    return foodprint



def donutcheck(foodprint):

    idlist = []
    word = ['donut', 'Donut', 'DONUT']
    key = list(foodprint.keys())

    for i in range(len(foodprint)):
        words = foodprint[key[i]].split()
        for j in range(len(words)):
            if words[j] in word:
                idlist.append(key[i])

    return idlist


def orderidremoverfood(id, foodprint):
    id = str(id)

    del foodprint[id]


    return foodprint

def orderidremoverprice(id,priceprint):
    id = str(id)

    del priceprint[id]

    return priceprint


def totalprice(id,priceprint):

    for key in id:
        if key in priceprint:
            del priceprint[key]

    return "%.2f" % sum(priceprint.values())





def main():
    url = 'https://research.cs.queensu.ca/home/cords2/timHortons.txt'
    print(readtxt(url))
    print('This is the text file / website in which the data is taken from')
    print('')
    print('1) look up an order by the order id and print the food and the price.')
    print(getorder(101,readtxt(url)))
    print('')

    print('2) allow the user to change the food items for a particular order id.')

    print(changefoodorder(102, 'Soup', foodprint(readtxt(url))))
    print('')

    print('3) Find out which orders, if any, contain a donut.  Print the order ids of those that do')
    print(donutcheck(foodprint(readtxt(url))))
    print('')

    print('4) Remove an order from the order list given the order id.')
    id = input('Enter the order id wished to be removed')
    print(orderidremoverprice(id, priceprint(readtxt(url))) , orderidremoverfood(id, foodprint(readtxt(url))))
    print('')

    print('5) Calculate the total price of all orders that do not contain donuts in the order list.')
    print(totalprice(donutcheck(foodprint(readtxt(url))),priceprint(readtxt(url))))
main()