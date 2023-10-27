"""
Word analyzer
Author:  Joseph Liao
Student Number: 20366481
Date:  24th Sept 2022
"""

import urllib.request
import webbrowser


def readWords(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    x = data.split()
    return x

def wordlettercount(word):
    letters=list(word)
    return (len(letters))

def wordCount(wordList):
    dictionary = {}
    for i in wordList:
        count = wordlettercount(i)
        if count in dictionary:
            dictionary[count] += 1
        else:
            dictionary.update({count: 1})

    return (dictionary)


def totalWords(dictionary,n,m):
    total = []
    if n > m:
        return 0
    else:
        for i in range(n, m+1):
            if i not in dictionary:
                total.append(0)
            else:
                num = dictionary[i]
                total.append(num)

    return (sum(total))


def maxWordLength(dictionary):
    return (max(dictionary))
def maxFrequency(dictionary):
    mostwords = max(dictionary, key=dictionary.get)
    return (mostwords)

def writeToFile(dictionary):
    file = open('words.txt', 'w')
    for i in dictionary:
        t=("There are " + str(dictionary[i]) + " words of length " + str(i)+"\n")
        file.write(t)

    file = open('words.txt', 'r')
    print(file.read())


def main():
    b = "https://research.cs.queensu.ca/home/cords2/words.txt"
    dictionary=wordCount(readWords(b))
    readWords(b)
    print("This is a dictionary of the frequency of words of a certain length")
    print(wordCount(readWords(b)))
    print("This tells you how many words are in the list with the length of the range of the given integers ")
    print(totalWords(dictionary,1,2))
    print("This tells you the length longest word in the list")
    print(maxWordLength(dictionary))
    print("This tells you the the length of word that is most frequent in the list")
    print(maxFrequency(dictionary))

    print("This writes the how many words there are of a given length and creates a new file")
    print(writeToFile(dictionary))

main()




