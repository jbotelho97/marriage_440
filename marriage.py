#Authors: Jack Botelho, ...
#Programmed in PycharmCE on a Macbook with a 1.4GHz i5
#CSC 440 - Assignment 1

import sys

def main(argv):
    # people = open(argv, "r")
    try:
        people = open(argv, "r")
        num = int(people.readline())
    except:
        exit(1)
    # num = int(people.readline())
    listNames = num + 1
    knights = [[0 for x in range(num)] for y in range(listNames)]
    ladies = [[0 for x in range(num)] for y in range(listNames)]
    #pairs = [[0 for x in range(num)] for y in range(num)]
    pairs = []
    curLine = people.readline()
    kcounter = 1  #knight counter
    lcounter = 1  #lady coutner
    while curLine != "":
        curLine = curLine.strip()
        if kcounter <= num:
            knights[kcounter - 1] = curLine.split(" ")
            kcounter += 1
        else:
            ladies[lcounter - 1] = curLine.split(" ")
            lcounter += 1

        curLine = people.readline()
    currentPick = 1
    pairCounter = 0
    while pairCounter < num:
        print('I made it!')
        for i in range(len(knights)):
            if free(pairs, knights[i][0], 0) <= 0:
                lady = knights[i][currentPick]
                for j in range(len(ladies)):
                    if lady == ladies[j][0]:
                        ladyPair = free(pairs, lady, 1)
                        if ladyPair <= 0:
                            pairs.append([i, j])
                            pairCounter += 1
                        else:
                            knightPos #The position of the requestor in lady's list
                            for k in range(len(ladies[j])):
                                if knights[i][0] == ladies[j][k]:
                                    knightPos = k
                                    break
                            if knightPos < pairs[ladyPair][0]:
                                pairs.remove(ladyPair);
                                pairs.append([i, j])
                                pairCounter += 1
    for i in range(len(pairs)):
        dude, lady = pairs[i][0], pairs[i][1]
        print(dude, " ", lady)



#num is 0 for knights, 1 for ladies
def free(pairs, name, num):
    if num < 0 or num > 1:
        return -1
    for i in range(len(pairs)):
        if name == pairs[i][num]:
            return i
    return -1







