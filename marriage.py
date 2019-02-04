#Authors: Jack Botelho, ...
#Programmed in PycharmCE on a Macbook with a 1.4GHz i5
#CSC 440 - Assignment 1

import sys

def main():
    people = open("ten.txt", "r")
    num = int(people.read())
    counter = 0
    knights = []
    ladies = []
    pairs = []
    curLine = people.read()
    counter += 1
    while curLine != "":
        curLine = curLine.strip()
        if counter <= num:
            knights[counter - 1] = curLine.split(" ")
        else:
            ladies[counter - 1] = curLine.split(" ")

        curLine = people.readline()
    currentPick = 1
    while pairs.__len__() < num:
        for i in knights:
            if free(pairs, knights[i][0], 0) <= 0:
                lady = knights[i][currentPick]
                for j in ladies:
                    if lady == ladies[j][0]:
                        ladyPair = free(pairs, lady, 1)
                        if ladyPair <= 0:
                            pairs.append([i, j])
                        else:
                            knightPos #The position of the requestor in lady's list
                            for k in ladies[j]:
                                if knights[i][0] == ladies[j][k]:
                                    knightPos = k
                                    break
                            if knightPos < pairs[ladyPair][0]:
                                pairs.remove(ladyPair);
                                pairs.append([i, j])
    for i in pairs:
        print(pairs[i][0], " ", pairs[i][1], "\n")






#num is 0 for knights, 1 for ladies
def free(pairs, name, num):
    if num < 0 or num > 1:
        return -1
    for i in pairs:
        if name == pairs[i][num]:
            return i
    return -1








