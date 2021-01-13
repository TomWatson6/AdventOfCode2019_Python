import math

lines = open("input.txt").readlines()

wires = [x.split(",") for x in lines]

wire_paths = []

for wire in wires:
    position = [0, 0]
    visited = []
    mags = [int(x[1:]) for x in wire]
    print("Sum:", sum(mags))

    for instruction in wire:
        instruction = instruction.strip("\n")
        magnitude = int(instruction[1:])
        increment = []
        if instruction[0] == 'R':
            increment = [1, 0]
        if instruction[0] == 'L':
            increment = [-1, 0]
        if instruction[0] == 'U':
            increment = [0, 1]
        if instruction[0] == 'D':
            increment = [0, -1]

        for x in range(magnitude):
            x, y = position
            x += increment[0]
            y += increment[1]
            position = [x, y]
            visited.append(position)

        #print("Instruction", instruction, "Complete!")

    wire_paths.append(visited)

#print(len([(x[0] + x[1]) for x in wire_paths[0] if x in wire_paths[1]]))

# intersections = len([(x[0] + x[1]) for x in wire_paths[0] if x in wire_paths[1]])
# print(intersections)
# print("Part 1:", min(intersections))