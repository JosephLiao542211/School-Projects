def longestPalindrome(s):
    stringlist=list(s)
    for i in range(len(stringlist)):
        stringlist.append("*")
    while True:
        count = 0
        for i in range(len(stringlist)):
            try:
                x = stringlist[i + 2]
            except IndexError:
                

            if stringlist[i] == stringlist[i + 1]:
                stringlist[i] = "".join(stringlist[i:i+1])
                count += 1
            if stringlist[i] == stringlist[i + 2]:
                stringlist[i] = "".join(stringlist[i:i+2])
                count += 1

        if count == 0:
            break
        sortedwords = sorted(stringlist, key=len)
        return sortedwords[-1]

longestPalindrome("aavsd")