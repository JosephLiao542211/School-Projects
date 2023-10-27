"""

This program provides a framework to manage a rental syestem
Author:  Joseph Liao
Student Number: 20366481
Date:  11th NOV 2022

"""


def initializeBikeInfo():

    info={8010:{"Location":'York',"Total Capacity" :31,"Number of Bikes Available for rent currently":20,"Number of Docks Available (empty spaces)":11},
          8011:{"}Location":'Esplanade',"Total Capacity" :15,"Number of Bikes Available for rent currently":5,"Number of Docks Available (empty spaces)":10},
          8012:{"}Location":'George',"Total Capacity" :19,"Number of Bikes Available for rent currently":1,"Number of Docks Available (empty spaces)":18},
          8013:{"Location":'Madison',"Total Capacity" :15,"Number of Bikes Available for rent currently":2,"Number of Docks Available (empty spaces)":13},
          8014:{"Location":'Elm',"Total Capacity" :11,"Number of Bikes Available for rent currently":0,"Number of Docks Available (empty spaces)":11},
          8015:{"Location":'University',"Total Capacity" :19,"Number of Bikes Available for rent currently":1,"Number of Docks Available (empty spaces)":18},
          8016:{"Location":'Bay',"Total Capacity" :11,"Number of Bikes Available for rent currently":11,"Number of Docks Available (empty spaces)":0},
          8017:{"Location":'College',"Total Capacity" :11,"Number of Bikes Available for rent currently":1,"Number of Docks Available (empty spaces)":10}}

    return info

def changeInfo(bikeInfo, id, cap, numBikes, docks):
    #updates the bike info
    bikeInfo[id]["Totalcapacity"] = cap
    bikeInfo[id]["Number of Bikes Available for rent currently"] = numBikes
    bikeInfo[id]["Number of Docks Available (empty spaces)"] = docks

def bikeRental(bikeInfo, stationID):
    #tracks rentals and adjusts values
    if stationID not in bikeInfo:
        return False
    elif bikeInfo[stationID]["Number of Bikes Available for rent currently"]!=0:
        bikeInfo[stationID]["Number of Bikes Available for rent currently"]-=1
        bikeInfo[stationID]["Number of Docks Available (empty spaces)"]+=1
        return True
    else:
        return False

def returnBike(bikeInfo, stationID):
    #tracks returns and adjusts values
    if stationID not in bikeInfo:
        return False
    elif bikeInfo[stationID]["Number of Docks Available (empty spaces)"]!=0:
        bikeInfo[stationID]["Number of Bikes Available for rent currently"]+=1
        bikeInfo[stationID]["Number of Docks Available (empty spaces)"]-=1
        return True
    else:
        return False


def getInfo(bikeInfo,stationId):
    #allows user to find the stats of a specific station

    if stationId not in bikeInfo:
        return []
    else:
        return [bikeInfo[stationId]["Location"],bikeInfo[stationId]["Total Capacity"],bikeInfo[stationId]["Number of Bikes Available for rent currently"],bikeInfo[stationId]["Number of Docks Available (empty spaces)"]]
def docksAvailable(bikeInfo):
    #finds the total number of docks
    totallist=[]
    noid=bikeInfo.values()
    for i in noid:
        totallist.append(i["Number of Docks Available (empty spaces)"])
    return sum(totallist)


def testCode():
    # Test initialize function
    info = initializeBikeInfo()
    print(info)
    print()

    # Test change info
    changeInfo(info, 8012, 15, 7, 8)
    print("After changing information for 8012, new info is:")
    print(info)

    # Test bike rental when bikes not available
    print("Number of bikes at 8014 before renting is", info[8014]["Number of Bikes Available for rent currently"])
    bikeRental(info, 8014)
    print("Number of bikes at 8014 after renting is", info[8014]["Number of Bikes Available for rent currently"])

    # Test bike rental when bikes  available
    print("Number of bikes at 8011 before renting is", info[8011]["Number of Bikes Available for rent currently"])
    bikeRental(info, 8011)
    print("Number of bikes at 8011 after renting is", info[8011]["Number of Bikes Available for rent currently"])
    print("Number of docks at 8011 after renting is", info[8011]["Number of Docks Available (empty spaces)"])

    # Test information retrieval for a specific location that doesn't exist
    statInfo = getInfo(info,1010)
    if len(statInfo) == 0:
        print("Station does not exist")
    else:
        print("Info for station 1010 is ", statInfo)

    # Test information retrieval for a specific location that exists
    statInfo = getInfo(info, 8010)
    if len(statInfo) == 0:
        print("Station does not exist")
    else:
        print("Info for station 8010 is ", statInfo)

    # Test to find total number of docks available
    print("Total number of docks available: ", docksAvailable(info))

    # Test bike return - run through all cases
    for key in info:
        if returnBike(info, key):
            print("Returned bike successfully to ", key)
        else:
            print("Could not return bike to", key)

testCode()