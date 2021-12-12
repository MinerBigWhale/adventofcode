import sys

#https://adventofcode.com/2020/day/1

input = open("2020/Day 1.input", "r")
input = [x for x in input]

output2 = 0
output3 = 0
for line1 in input: 
    for line2 in input:
        for line3 in input:
            if int(line1) + int(line2) + int(line3) == 2020:
                output3 = int(line1) * int(line2) * int(line3)
        if int(line1) + int(line2) == 2020:
            output2 = int(line1) * int(line2)
print("part 1 : " + str(output2))
print("part 2 : " + str(output3))