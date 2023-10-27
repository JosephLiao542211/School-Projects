# import csv library
import csv

# function to create a list of dictionaries from a CSV file
def dictionary_maker(filename):
    dictionary=[]
    with open(filename, 'r') as data:    # open the file in read mode
        for line in csv.DictReader(data):    # iterate through the lines and store each line as dictionary
            dictionary.append(line)
    return dictionary    # return the list of dictionaries

# function to display information for a specific electoral district
def displayInfo(maindict):
    while True:
        x=input("please input electoral district number for info: ")    # get user input
        for i in maindict:
            if i['Electoral District Number']==(x):    # check if the district number exists
                p=['Polling Stations','Valid Ballots','Total Ballots Cast','Percentage of Voter Turnout']
                for t in p:
                    print(t,':',i[t])    # print the information for the district
                return
        else:
            print("invalid input")    # print an error message if the input is invalid

# function to find the unique districts for a given province
def uniqueDistricts(maindict,province):
    plist=[]
    for i in maindict:
        if i['Province']==province and i['Electoral District Name'] not in plist:    # check if the district name is unique in the province
            plist.append(i['Electoral District Name'])
    if len(plist)==0:
        return 'province is misspelt or does not exist in the database'    # print an error message if the province is not found
    else:
        return plist    # return the list of unique districts

# function to find the maximum value for a given election stat
def findMax(LF,maindict):
    error = []
    for i in maindict:
        if LF in i:
            error.append('good')
    if len(error) == 0:
        print('ERROR INVALID STAT NAME CHECK SPELLING')
        return None    # print an error message if the stat is not found
    values=[]
    for i in maindict:
        values.append(i[LF])    # create a list of all values for the given stat
    largest = values[0]
    for item in values:
        if item > largest:
            largest = item    # find the largest value
    elecn = []
    for key in maindict:
        if key[LF] == largest:
            elecn.append(key['Electoral District Number'])    # store the district number(s) with the largest value
    return largest, 'district number:'+str(elecn )   # return the largest value and its district number(s)

# function to find the minimum value for a given election stat
def findMin(LF,maindict):
    error = []
    for i in maindict:
        if LF in i:
            error.append('good')
    if len(error) == 0:
        print('ERROR INVALID STAT NAME CHECK SPELLING')
        return None    # print an error message if the stat is not found
    values = []
    for i in maindict:
        values.append(i[LF])    # create a list of all values for the given stat
    smallest = values[0]
    for item in values:
        if item < smallest:
            smallest = item    # find the smallest value
    elecn = []
    for key in maindict:
        if key[LF]==smallest:
            elecn.append(key['Electoral District Number'])    # store the district number(s) with the smallest value
    return smallest, 'district number:'+ str(elecn)    # return the smallest value and its district number(s)

# function


def selection_sort(LF,maindict):
    error=[]
    for i in maindict:
        if LF in i:
            error.append('good')
    if len(error)==0:
        print('ERROR INVALID STAT NAME CHECK SPELLING')
        return None
    n = len(maindict)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        sm = i
        for j in range(i+1, n):
            if maindict[j][LF] < maindict[sm][LF]:
                sm = j
        # Swap the minimum element with the first element of the unsorted part
            maindict[i], maindict[sm] = maindict[sm], maindict[i]

    return maindict

    # Define a function for selection sorting a dictionary based on a specific key


def selection_sort(LF, maindict):
    error = []
    # Check if the key to sort by exists in the dictionary
    for i in maindict:
        if LF in i:
            error.append('good')
    # If the key doesn't exist, print an error message and return None
    if len(error) == 0:
        print('ERROR INVALID STAT NAME CHECK SPELLING')
        return None
    n = len(maindict)
    # Iterate through the dictionary to sort it
    for i in range(n):
        # Find the index of the minimum element in the unsorted part of the dictionary
        sm = i
        for j in range(i + 1, n):
            if maindict[j][LF] < maindict[sm][LF]:
                sm = j
        # Swap the minimum element with the first element of the unsorted part
        maindict[i], maindict[sm] = maindict[sm], maindict[i]

    return maindict

    # Define a function for binary searching a dictionary based on a specific key-value pair


def binarysearch(number, maindict):
    high = len(maindict) - 1
    low = 0
    # Keep searching until the low index is greater than the high index
    while low <= high:
        mid = (high + low) // 2
        # If the desired key-value pair is found, return the corresponding value
        if int(maindict[mid]['Electoral District Number']) == int(number):
            return maindict[mid]['Percentage of Voter Turnout']
        # If the key-value pair is in the lower half of the dictionary, search again with the lower half
        elif int(maindict[mid]['Electoral District Number']) > int(number):
            high = mid - 1
        # If the key-value pair is in the upper half of the dictionary, search again with the upper half
        else:
            low = mid + 1
    # If the key-value pair is not found, return None
    return (('NOT FOUND'))

    # Define a function for displaying a menu of options for interacting with a dictionary


def menu(filename):
    # Create a dictionary from a file
    dictionary = dictionary_maker(filename)

    while True:
        # Prompt the user to select a function to perform on the dictionary
        x = input('1. Display information for an electoral district \n'
                  '2. Show unique districts by the given province \n'
                  '3. Find Min/Max of a given election stat\n'
                  '4. Sort all data in increasing order by a given stat\n'
                  '5. Find Percentage of voter turnout by district number\n'
                  'Please enter the function you would like to access. To exit, enter q: ')
        # If the user selects option 1, display information for a specific electoral district
        if x == '1':
            displayInfo(dictionary)
        # If the user selects option 2, show a list of unique districts by the given province
        if x == '2':
            print('available provinces:\nNewfoundland and Labrador/Terre-Neuve-et-Labrador,\n'
                  'Prince Edward Island/ÃŽle-du-Prince-Ã‰douard\n'
                  'Nova Scotia/Nouvelle-Ã‰cosse\n'
                  'New Brunswick/Nouveau-Brunswick\n'
                  'Quebec/QuÃ©bec\n'
                  'Ontario\n'
                  'Manitoba \nSaskatchewan\n'
                  'Alberta\n'
                  'British Columbia/Colombie-Britannique\n'
                  'Yukon\n'
                  'Northwest Territories/Territoires du Nord-Ouest\n'
                  'Nunavut\n')
            while True:
                p=input('please input province name')
                if p in ['Newfoundland and Labrador/Terre-Neuve-et-Labrador', 'Prince Edward Island/ÃŽle-du-Prince-Ã‰douard',
                 'Nova Scotia/Nouvelle-Ã‰cosse', 'New Brunswick/Nouveau-Brunswick', 'Quebec/QuÃ©bec', 'Ontario',
                 'Manitoba', 'Saskatchewan', 'Alberta', 'British Columbia/Colombie-Britannique', 'Yukon',
                 'Northwest Territories/Territoires du Nord-Ouest', 'Nunavut']:
                    print(uniqueDistricts(dictionary,p))
                    break
                else:
                    print('invalid input')
        if x=='3':
            print('available stats: Electoral District Number\nPopulation\nElectors\nPolling Stations\nValid Ballots'
                 '\nPercentage of Valid Ballots\nRejected Ballots/\nPercentage of Rejected Ballots\nTotal Ballots Cast\n'
                 'Percentage of Voter Turnout')
            LF=input('enter the stat you want to search up')
            while True:
                m=input('Please enter min or max for which function you want').upper()
                if m=='MAX':
                    print(findMax(LF,dictionary))
                    break
                elif m=='MIN':
                    print(findMin(LF,dictionary))
                    break
                else:
                    print('invalid input')
        if x=='4':
            print('available stats: Electoral District Number\nPopulation\nElectors\nPolling Stations\nValid Ballots'
                  '\nPercentage of Valid Ballots\nRejected Ballots/\nPercentage of Rejected Ballots\nTotal Ballots Cast\n'
                  'Percentage of Voter Turnout')

            LF = input('enter the stat you want to sort by')
            print(selection_sort(LF,dictionary))
        if x=='5':
            e=input('enter district number')
            if binarysearch(e,dictionary)!='NOT FOUND':
                print('percentage of voter turnout:'+binarysearch(e,dictionary)+'%')
            else:
                print(binarysearch(e,dictionary))
        if x=='q':
            return

