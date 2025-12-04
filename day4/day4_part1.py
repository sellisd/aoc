#!/usr/bin/env python3

with open("../data/day4_input.txt") as f:
    lines = f.readlines()

def add_roll(char):
    if char == '@':
        return 1
    return 0

accessible = 0
for line_no, line in enumerate(lines):
    for char_no, char in enumerate(line.rstrip()):
        if char != "@":
            print('.', end='')
            continue
        rolls = 0
        top = line_no - 1
        bottom = line_no + 1
        left = char_no - 1
        right = char_no + 1
        #top line
        #lines[top][left:char_no+2]
        if top >= 0:
            if left >= 0:
                rolls+=add_roll(lines[top][left])
            rolls+=add_roll(lines[top][char_no])
            if right < len(lines):
                rolls+=add_roll(lines[top][right])
        #around
        if left >= 0:
            rolls+=add_roll(lines[line_no][left])
        if right < len(lines):
            rolls+=add_roll(lines[line_no][right])
        #bottom
        #lines[bottom][left:char_no+2]
        if bottom < len(lines):
            if left >= 0:
                rolls+=add_roll(lines[bottom][left])
            rolls+=add_roll(lines[bottom][char_no])
            if right < len(lines):
                rolls+=add_roll(lines[bottom][right])
        if rolls < 4:
            accessible+=1
            print('x', end='')
        else:
            print('@', end='')
    print("\n", end='')
print("Accessible positions:", accessible)