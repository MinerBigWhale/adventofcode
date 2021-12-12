from os import stat
import sys

#https://adventofcode.com/2021/day/3

with open("2021/Day 3.input", "r") as input:
    input = input.readlines()

# initiate start position and depth
states = [0 for x in range(len(input[0]) - 1)]

for line in input: 
    i = 0

    for char in line:
        if char == "1":
            states[i] += 1
        if char == "0":
            states[i] -= 1
        i += 1

ot = ""
of = ""
for state in states:
    if state > 0:
        ot += "1"
        of += "0"
    else:
        ot += "0"
        of += "1"
print("part 1: ot=("+ot + ") " + str(int(ot, 2)) + " of=("+of + ") " + str(int(of, 2)) + " r="+ str(int(ot, 2) * int(of, 2)))

def filter_up(codes, pos):
    if len(states) <= pos or len(codes) == 1:
        return codes

    ft = []
    ff = []
    for item in codes:
        if item[pos] == "1":
            ft.append(item)
        if item[pos] == "0":
            ff.append(item)

    if len(ft) >= len(ff):
        return filter_up(ft, pos + 1)
    else: 
        return filter_up(ff, pos + 1)
    
def filter_down(codes, pos):
    if len(states) <= pos or len(codes) == 1:
        return codes

    ft = []
    ff = []
    for item in codes:
        if item[pos] == "1":
            ft.append(item)
        if item[pos] == "0":
            ff.append(item)

    if len(ff) <= len(ft):
        return filter_down(ff, pos + 1)
    else: 
        return filter_down(ft, pos + 1)


up = filter_up(input, 0)[0][:-1]
down = filter_down(input, 0)[0][:-1]

print("part 2: up=("+up + ") " + str(int(up, 2)) + " down=("+down + ") " + str(int(down, 2)) + " r="+ str(int(up, 2) * int(down, 2)))