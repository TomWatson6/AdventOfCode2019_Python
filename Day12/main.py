import re

def get_input(file_name):
    with open(file_name) as f:
        input = f.read().strip()

    values = [int(x) for x in list(re.findall("(?<=\=)-?\d+", input))]

    assert len(values) % 3 == 0

    positions = {}

    for x in range(0, len(values) - 2, 3):
        positions[(values[x], values[x+1], values[x+2])] = (0, 0, 0)

    return positions

def evolve(positions):
    for k, v in positions.items():
        x, y, z = 0, 0, 0

        for k1 in positions.keys():
            if k == k1:
                continue
            if k1[0] > k[0]:
                x += 1
            elif k1[0] < k[0]:
                x -= 1
            if k1[1] > k[1]:
                y += 1
            elif k1[1] < k[1]:
                y -= 1
            if k1[2] > k[2]:
                z += 1
            elif k1[2] < k[2]:
                z -= 1
            positions[k] = (v[0] + x, v[1] + y, v[2] + z)
        
    new_positions = {}

    for k, v in positions.items():
        k = (k[0] + v[0], k[1] + v[1], k[2] + v[2])
        new_positions[k] = v

    return new_positions

def energy(positions):
    energies = []

    for k, v in positions.items():
        energy = abs(k[0]) + abs(k[1]) + abs(k[2])
        energy *= abs(v[0]) + abs(v[1]) + abs(v[2])
        energies.append(energy)
    
    return sum(energies)

file_name = "input.txt"

positions = get_input(file_name)

for _ in range(1000):
    positions = evolve(positions)

print(f"Part 1: {energy(positions)}")

positions = get_input(file_name)
visited = {(tuple(positions.items())): True}
steps = 0

while True:
    positions = evolve(positions)
    steps += 1
    if steps % 100000 == 0:
        print(tuple(positions.items()))
    if tuple(positions.items()) in visited:
        break
    # visited[tuple(positions.items())] = True

print(f"Part 2: {steps}")








