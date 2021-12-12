import sys
from typing import Counter

#https://adventofcode.com/2020/day/2

input = open("2020/Day 2.input", "r")
input = [x for x in input]

validcounter1 = 0
validcounter2 = 0
for line in input: 
    policy = line.split(":")[0]
    minp = int(policy.split("-")[0])
    maxp = int(policy.split("-")[1].split(" ")[0])
    letter = policy.split(" ")[1]
    password = line.split(":")[1][1:-1]

    counter1 = 0
    counter2 = 0
    for i in range(len(password)):
        if password[i] == letter:
            counter1 += 1
        if i + 1 == minp or i + 1 == maxp and password[i] == letter:
            counter2 += 1
    if counter1 >= minp and counter1 <= maxp:
        validcounter1 += 1
    if counter2 == 1:
        validcounter2 += 1

print("part 1: " + str(validcounter1))
print("part 2: " + str(validcounter2))