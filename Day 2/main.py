import math
import time
from IntcodeComputer import IntcodeComputer

input = open("input.txt").read()
instructions = input.split(",")

instructions[1] = 12
instructions[2] = 2

computer = IntcodeComputer(instructions)
computer.run()

print("Part 1:", computer.instructions[0])

desired_output = 19690720
found = False

for i in range(100):
    for j in range(100):
        instructions[1] = i
        instructions[2] = j

        computer = IntcodeComputer(instructions)
        computer.run()

        output = computer.instructions[0]
        calculation = 100 * i + j

        if output == desired_output:
            print("Part 2:", calculation)
            found = True
            break
    if found:
        break