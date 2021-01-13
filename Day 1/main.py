import math

def calculate(value):
    output = value // 3 - 2

    if output < 9:
        return output
    else:
        return output + calculate(output)

lines = open("input.txt").readlines()

numbers = [int(x) for x in lines]

total = 0

for x in numbers:
    total += x // 3 - 2

print("Part 1:", total)

total = 0

for x in numbers:
    total += calculate(x)

print("Part 2:", total)