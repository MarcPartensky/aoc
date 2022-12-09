#!/usr/bin/env python

import sys

element = dict(X=1, Y=2, Z=3)
win = dict(A="Y", B="Z", C="X")
draw = dict(A="X", B="Y", C="Z")

# xyz = "XYZ"
# abc = "ABC"
end = dict(X="loose", Y="draw", Z="win")
# end = ["loose", "draw", "win"]

score = 0
for line in sys.stdin:
    a, b = line.split()
    score += element[b]
    if end[b] == "win":
        score += 6
    elif end[b] == "draw":
        score += 3 

print(score)
