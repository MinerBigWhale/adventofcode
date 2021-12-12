from os import stat, times
import sys

#https://adventofcode.com/2021/day/4

with open("2021/Day 4.input", "r") as input:
    tirage = [int(x) for x in input.readline().split(",")]
    input = input.readlines()

grids = []


def printcard(card, carry):
    counter = 0
    for r in card:
        for c in r:
            if c != 'X':
                counter += c

    print(carry * counter)

for c, r1, r2, r3, r4 ,r5 in zip(input[::6], input[1::6], input[2::6], input[3::6], input[4::6], input[5::6]):
    grids.append(
        [
            [int(x) for x in r1[:-1].split(" ")],
            [int(x) for x in r2[:-1].split(" ")],
            [int(x) for x in r3[:-1].split(" ")],
            [int(x) for x in r4[:-1].split(" ")],
            [int(x) for x in r5[:-1].split(" ")]
        ]
    )
first = False
winner = False
card = []
carry = 0
for n in tirage:
    gs = 0 
    while gs < len(grids) :
        g= grids[gs]
        row = [0 for x in range(len(grids[0]))]
        col = [0 for x in range(len(grids[0][0]))]
        for r in range(len(grids[0])):
            for c in range(len(grids[0][0])):
                if g[r][c] == n:
                    g[r][c] = 'X'
        
        for r in range(len(grids[0])):
            for c in range(len(grids[0][0])):
                if g[r][c] == 'X': 
                    col[c] += 1
                    row[r] += 1

        for r in row:
            if r == 5:
                winner = True
                if first == False:
                    printcard(g, n)
                    first = True
        for c in col:
            if c == 5:
                winner = True
                if first == False:
                    printcard(g, n)
                    first = True
                  
        if winner != False:
            winner = False
            if len(grids) == 1:
                printcard(grids[0], n)
            grids.pop(gs)
            gs-=1
          
        gs+=1
        