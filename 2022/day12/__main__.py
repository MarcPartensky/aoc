#!/usr/bin/env python

# parse input into grid of number
with open("input") as f:
    m = f.read()
alpha = "abcdefghijklmnopqrstuvwxyz"
grid = []
for y,l in enumerate(m.split()):
    line = []
    for x,letter in enumerate(l):
        if letter == "S":
            letter = "a"
            xp, yp = x, y
        elif letter == "E":
            letter = "z"
            xe, ye = x, y
        line.append(alpha.index(letter))
    grid.append(line)

# width and height
w = len(grid[0])
h = len(grid)


def bfs():
    visited = []
    for _ in range(h):
        visited.append([0]*w)

    visited[yp][xp] = 1
    neighbors = [(xp, yp)]
    steps = 0
    while True:
        steps += 1
        next_neighbors = []

        # use old neighbors
        for (x, y) in neighbors:
            height = grid[y][x]

            # to iterate over next potential neighbors
            for xi, yi in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    xt = x+xi
                    yt = y+yi

                    if 0<=xt<w and 0<=yt<h: # check if in grid
                        if visited[yt][xt]:
                            continue
                        if grid[yt][xt] <= height + 1: # check if too high
                            continue

                        if (xt, yt) == (xe, ye): # check if answer found
                            return steps
                        
                        # next neighbor found
                        visited[yt][xt] = 1
                        next_neighbors.append((xt, yt)) 

        neighbors = next_neighbors

print(bfs())
