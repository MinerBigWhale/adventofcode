import sys

#https://adventofcode.com/2021/day/2

with open("2021/Day 2.input", "r") as input:
    input = [x.split() for x in input]

# initiate start position and depth
hpos, aim, depth = 0

# for each line, split the text
for action, value in map(str.split, input): 
    
    #begin to count
    if action == "forward":
        hpos+= int(value)
        depth+= aim * int(value)
    if action == "up":
        aim-= int(value)
    if action == "down":
        aim+= int(value)

print("part 1: h= "+str(hpos)+" d= "+str(aim)+" r= "+str(hpos*aim))
print("part 2: h= "+str(hpos)+" d= "+str(depth)+" r= "+str(hpos*depth))
