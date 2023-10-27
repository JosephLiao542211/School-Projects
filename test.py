
def listintersection(guestlist,powleyGuests):
    guestlistnames=[]
    for names in guestlist:
        guestlistnames.append(names)
    for i in powleyGuests:
        if i not in guestlistnames:
            guestlist[i]=["tbd",0]

        return guestlist

def food(foodlist):
    t = []
    for i in foodlist[:-1]:
        t.append(list(i))
    for g in t:
        if (foodlist[-1]>0 and (len(list(foodlist[0]))>3 or list(foodlist[0])[0]=="p")) \
                or (foodlist[-1] == 0 and ("s" and "p" in g)):
            return ("True")
        else:
            return ("False")