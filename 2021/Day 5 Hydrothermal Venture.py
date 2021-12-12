from os import stat, times
import numpy as np
from PIL import Image
import sys

#https://adventofcode.com/2021/day/5

with open("2021/Day 5.input", "r") as input:
    points = [[y.split(','),z.split(',')] for y,z in [x[:-1].split(' -> ') for x in input.readlines()]]
x=0
y=1
r=0
g=1
b=2
ra=250
ga=50
ba=100

max_x=0
max_y=0

for pa, pb in points:
    if int(pa[x]) > max_x:
        max_x = int(pa[x])
    if int(pb[x]) > max_x:
        max_x = int(pb[x])
    if int(pa[y]) > max_y:
        max_y = int(pa[y])
    if int(pb[y]) > max_y:
        max_y = int(pb[y])

pix = np.zeros([max_x+1, max_y+1, 3], dtype=np.uint8)
grid = np.zeros([max_x+1, max_y+1], dtype=int)

for pa, pb in points:
    # Horizontal
    if int(pa[x]) == int(pb[x]):
        sx = int(pa[x])
        if int(pa[y]) < int(pb[y]):
            for ny in range(int(pa[y]), int(pb[y])+1):
                pix[ny,sx][g] +=ga
                grid[ny,sx] +=1
        if int(pa[y]) > int(pb[y]):
            for ny in range(int(pa[y]), int(pb[y])-1, -1):
                pix[ny,sx][g] +=ga
                grid[ny,sx] +=1
    # Vertical
    if int(pa[y]) == int(pb[y]):
        sy = int(pa[y])
        if int(pa[x]) < int(pb[x]):
            for nx in range(int(pa[x]), int(pb[x])+1):
                pix[sy,nx][g] +=ga
                grid[sy,nx] +=1
        if int(pa[x]) > int(pb[x]):
            for nx in range(int(pa[x]), int(pb[x])-1, -1):
                pix[sy,nx][g] +=ga
                grid[sy,nx] +=1
    # Diagonal
    else:
        if int(pa[y]) < int(pb[y]):
            ry = range(int(pa[y]), int(pb[y])+1)
            if int(pa[x]) < int(pb[x]):
                rx = range(int(pa[x]), int(pb[x])+1)
                for nx, ny in zip(rx, ry):
                    pix[ny,nx][b] +=ba
                    grid[ny,nx] +=1
            if int(pa[x]) > int(pb[x]):
                rx = range(int(pa[x]), int(pb[x])-1, -1)
                for nx, ny in zip(rx, ry):
                    pix[ny,nx][b] +=ba
                    grid[ny,nx] +=1
        if int(pa[y]) > int(pb[y]):
            ry = range(int(pa[y]), int(pb[y])-1,-1)
            if int(pa[x]) < int(pb[x]):
                rx = range(int(pa[x]), int(pb[x])+1)
                for nx, ny in zip(rx, ry):
                    pix[ny,nx][b] +=ba
                    grid[ny,nx] +=1
            if int(pa[x]) > int(pb[x]):
                rx = range(int(pa[x]), int(pb[x])-1, -1)
                for nx, ny in zip(rx, ry):
                    pix[ny,nx][b] +=ba
                    grid[ny,nx] +=1

counter = 0
for i, gx in enumerate(grid):
    for j, gy in enumerate(gx):
        """ if i%2==0 and j%2==1:
            gy[b] += ba
        if i%2==1 and j%2==0:
            gy[b] += ba"""
        if gy >= 2:
            counter += 1
            pix[i,j][r] = ra

print(counter)
            
img = Image.fromarray(pix)
img.save('2021/Day 5 output.png')