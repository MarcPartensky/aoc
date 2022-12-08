#!/usr/bin/env python

import sys
print(max([sum([int(i) for i in s.split()]) for s in sys.stdin.read().split("\n\n")]))
