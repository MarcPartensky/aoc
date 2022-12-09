#!/usr/bin/env python

import sys

element = dict(X=1, Y=2, Z=3)
win = dict(A="Y", B="Z", C="X")
draw = dict(A="X", B="Y", C="Z")

score = 0
for line in sys.stdin:
    a,b = line.split()
    score += element[b]
    if win[a] == b:
        score += 6
    elif draw[a] == b:
        score += 3 

print(score)
