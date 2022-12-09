#!/usr/bin/env python

cargo = {
    1: ["N", "S", "D", "C", "V", "Q", "T"],
    2: ["M", "F", "V"],
    3: ["F", "Q", "W", "D", "P", "N", "H", "M"],
    4: ["D", "Q", "R", "T", "F"],
    5: ["R", "F", "M", "N", "Q", "H", "V", "B"],
    6: ["C", "F", "G", "N", "P", "W", "Q"],
    7: ["W", "F", "R", "L", "C", "T"],
    8: ["T", "W", "N", "S"],
    9: ["M", "S", "D", "J", "R", "Q", "H", "N"],
}

def move(m, f, t):
    for _ in range(m):
        v = cargo[f].pop()
        cargo[t].append(v)

def top():
    out = []
    for columns in cargo.values():
        out.append(columns[-1])
    print("".join(out))

with open("input") as f:
    for line in f:
        _, m, _, f, _, t = line.split()
        m, f, t = map(int, [m, f, t])
        move(m, f, t)

top()
