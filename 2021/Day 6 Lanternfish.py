from os import stat, times

#https://adventofcode.com/2021/day/6

days = 256
with open("2021/Day 6.input", "r") as input:
    fish = [int(x) for x in input.readline().split(',')]

counters = [0,0,0,0,0,0,0,0,0]
for k, f in enumerate(fish):
    counters[f] += 1
print(counters)
for d in range(days+1):
    zero = counters[0]
    counters.pop(0)
    counters[6] += zero
    counters.append(zero)
    if d == 80:
        print("part 1 : " + str(counters[0]+counters[1]+counters[2]+counters[3]+counters[4]+counters[5]+counters[6]+counters[7]))
    if d == 256: 
        print("part 2 : " + str(counters[0]+counters[1]+counters[2]+counters[3]+counters[4]+counters[5]+counters[6]+counters[7]))
