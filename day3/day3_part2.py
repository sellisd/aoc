#!/usr/bin/env python3

def array_to_int(array):
    array=[str(i) for i in array]
    return(int("".join(array)))

def twelve(input):
    result = []
    numbers = [int(i) for i in input]
    current_index = 0
    for remaining in range(12,0,-1):
        head = numbers[current_index:len(numbers)-remaining+1]
        largest = max(head)
        head_index = head.index(largest)
        current_index = head_index + current_index
        result.append(numbers.pop(current_index))
    return array_to_int(result)


with open("../data/day3_input.txt", "r") as f:
    lines = f.readlines()
    joltage = 0
    for line in lines:
        joltage+=twelve(line.rstrip())
    print(joltage)

