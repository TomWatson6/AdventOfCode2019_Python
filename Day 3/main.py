import math

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

wires = [x.split(",") for x in lines]

directions = {
    'L': [-1, 0],
    'R': [1, 0],
    'U': [0, 1],
    'D': [0, -1]
}

visited = dict()

def append(visited, pos, value, steps):
    if visited.get(tuple(pos)) == None:
        visited[tuple(pos)] = [(value, steps)]
    else:
        if value in [x[0] for x in visited[tuple(pos)]]:
            return
        visited[tuple(pos)].append((value, steps))

for x in range(len(wires)):
    position = [0, 0]
    steps = 0
    append(visited, position, x, steps)
    for instruction in wires[x]:
        direction = directions[instruction[0]]
        magnitude = int(instruction[1:])
        for y in range(magnitude):
            position = [position[0] + direction[0], position[1] + direction[1]]
            steps += 1
            append(visited, position, x, steps)

intersections = [abs(x[0]) + abs(x[1]) for x in visited if len(visited[x]) > 1 and x != (0, 0)]

print("Part 1:", min(intersections))

distances = [visited[x][0][1] + visited[x][1][1] for x in visited if len(visited[x]) > 1 and x != (0, 0)]
min_distance = min(distances)

print("Part 2:", min_distance)