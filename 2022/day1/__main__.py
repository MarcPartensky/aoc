#!/usr/bin/python

import sys

elf = 0
elf_i = 0
max_elf = 0
max_elf_i = 0

for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        if elf > max_elf:
            max_elf = elf
            max_elf_i = elf_i
        elf = 0
        elf_i += 1
    else:
        elf += int(line)

print(max_elf_i)
