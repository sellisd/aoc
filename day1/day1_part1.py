#!/usr/bin/env python3

dial = 50
password = 0

def decrement(dial, steps):
    if dial - steps < 0:
        dial = 100 + (dial - steps)
    else:
        dial -= steps
    return dial

def increment(dial, steps):
    if dial + steps > 99:
        dial = dial + steps - 100
    else:
        dial += steps
    return dial

with open("../data/day1_input.txt", 'r') as f:
    input = f.read().splitlines()
    for line in input:
        direction = line[0]
        steps = int(line[1:])
        if steps > 99:
            steps = steps % 100
        if direction == 'L':
            dial = decrement(dial, steps)
        elif direction == 'R':
            dial = increment(dial, steps)
        else:
            exit(1)
        if dial == 0:
            password += 1
print(password)


