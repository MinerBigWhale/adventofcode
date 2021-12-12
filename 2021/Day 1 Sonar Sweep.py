import sys

#https://adventofcode.com/2021/day/1

with open("2021/Day 1.input", "r") as input:
    input = [int(x) for x in input]

# initiate previous over any possible value so it does not go up at first compare
counter = 0

# compare each item to the previous
for previous, value in zip(input, input[1:]):

    # if current bigger than previous, condition is True
    # True = 1 so counter increased, False = 0 so counter do not change
     counter += value > previous

print("part 1: " + str(counter))

# initiate previous over any possible value so it does not go up at first compare
counter = 0

# 1 A
# 2 AB
# 3 ABC
# 4  BCD
# 5   CDE
# 6    DEF
# 7     EF
# 8      F
# to compare sum of As to sum of Bs
# 1 + 2 + 3 == 2 + 3 + 4
# 2+3 is on both side, so we can just compare 1 to 4
# compare each item to the thrid follower 
for previous, value in zip(input, input[3:]):

    # if current bigger than previous, condition is True
    # True = 1 so counter increased, False = 0 so counter do not change
     counter += value > previous

print("part 2: " + str(counter))