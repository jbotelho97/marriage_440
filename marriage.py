# Authors: Jack Botelho, ...
# Programmed in PycharmCE on a Macbook with a 1.4GHz i5
# CSC 440 - Assignment 1

import sys


def main():
    try:
        people = open("ten.txt", "r")
    except:
        exit(1)
    num = int(people.readline())
    listNames = num + 1
    knights = [[0 for x in range(num)] for y in range(listNames)]
    ladies = [[0 for x in range(num)] for y in range(listNames)]
    pairs = []
    curLine = people.readline()
    kcounter = 1  # knight counter
    lcounter = 1  # lady coutner
    while curLine != "":
        curLine = curLine.strip()
        if kcounter <= num:
            knights[kcounter - 1] = curLine.split(" ")
            kcounter += 1
        else:
            ladies[lcounter - 1] = curLine.split(" ")
            lcounter += 1
        curLine = people.readline()
    pairCounter = 0

    # Main pairing loop, while there are less then n pairs the loopw will continue
    while pairCounter < num:
        for i in range(len(knights) - 1):  # loops through knights
            if free(pairs, knights[i][0], 0) < 0:
                lady = knights[i][1]
                for j in range(len(ladies) - 1):
                    if lady == ladies[j][0]:
                        ladyPair = free(pairs, lady, 1)
                        if ladyPair < 0:
                            pairs.append([knights[i][0], ladies[j][0]])
                            knights[i].pop(1)
                            pairCounter += 1
                        else:
                            knightPos = 0  # The position of the requestor in lady's list
                            for k in range(len(ladies[j])):
                                if knights[i][0] == ladies[j][k]:
                                    knightPos = k
                                    break
                            # if knightPos < pairs[ladyPair][0]:
                            comp = pairs[ladyPair][0]
                            for m in range(num + 1):
                                if comp == ladies[j][m]:
                                    if knightPos < m:
                                        pairs.pop(ladyPair);
                                        pairs.append([knights[i][0], ladies[j][0]])
                                        knights[i].pop(1)
                                        for i in range(len(knights)):
                                            if m == knights[i][0]:
                                                knights[i].pop(1)
                                                break
                                    else:
                                        knights[i].pop(1)
                                        break
    for i in range(len(pairs)):
        dude, lady = pairs[i][0], pairs[i][1]
        print(dude, " ", lady)
    people.close()


# num is 0 for knights, 1 for ladies
def free(pairs, name, num):
    if num < 0 or num > 1:
        return -1
    for i in range(len(pairs)):
        if name == pairs[i][num]:
            return i
    return -1

main()