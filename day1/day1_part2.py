#!/usr/bin/env python3

dial = 50
password = 0

def decrement(dial, steps):
    zero = False
    if dial - steps < 0:
        if dial != 0:
            zero = True
        dial = 100 + (dial - steps)
    else:
        dial -= steps
    return (dial, zero)

def increment(dial, steps):
    zero = False
    if dial + steps > 99:
        zero = True
        dial = dial + steps - 100
    else:
        dial += steps
    return (dial, zero)

with open("../data/day1_input.txt", 'r') as f:
    input = f.read().splitlines()
    for line in input:
        direction = line[0]
        steps = int(line[1:])
        if steps > 99:
            password += steps // 100
            steps = steps % 100
        if direction == 'L':
            dial, zero = decrement(dial, steps)
        elif direction == 'R':
            dial, zero = increment(dial, steps)
        else:
            exit(1)
        if zero or dial == 0:
            password += 1
print(password)


