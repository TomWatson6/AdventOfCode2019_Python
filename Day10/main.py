from collections import defaultdict as dd
from copy import deepcopy as dc
from fractions import Fraction

with open("input.txt") as f:
    input = [x.strip() for x in f.readlines() if x != ""]

asteroids = {}

for y, row in enumerate(input):
    for x, val in enumerate(row):
        asteroids[(x, y)] = val

def gcd(a,b): 
    return a if b == 0 else gcd(b,a%b) 

def simp(n, d):
    c = gcd(n,d)
    return (n//c,d//c)

def get_steps(c0, c1):
    dx = c1[0] - c0[0]
    dy = c1[1] - c0[1]

    sx = dx
    sy = dy

    if dx == 0:
        if dy > 0:
            sy = 1
        else:
            sy = -1
    if dy == 0:
        if dx > 0:
            sx = 1
        else:
            sx = -1

    if dx == 0 or dy == 0:
        return sx, sy

    x, y = simp(sx, sy)
    x, y = abs(x), abs(y)
    if sx < 0:
        x *= -1
    if sy < 0:
        y *= -1

    return x, y

def is_visible(asteroids, c0, c1):
    sx, sy = get_steps(c0, c1)
    checked = []

    x = c0[0] + sx
    y = c0[1] + sy

    while (x, y) in asteroids:
        checked.append((x, y))
        if asteroids[(x, y)] == "#" and (x, y) != c1:
            return False

        if (x, y) == c1:
            return True

        x += sx
        y += sy

    return False

def vaporise(asteroids, coord, index):
    """
    Organise into sections, where each can be ordered, D = Descending (y / x) and A = Ascending (y / x)
    Assuming a clockwise rotation - this should allow checks for visibility to be in order

        A A A   A   A A A
        A A A   A   A A A
        A A A   A   A A A

        A A A   X   D D D

        A A A   D   A A A
        A A A   D   A A A
        A A A   D   A A A

    """

    if index >= len([x for x in asteroids.values() if x == "#"]):
        return -1

    section = 0
    vap = 0

    while any([x == '.' for x in asteroids.values()]):
        if section % 8 == 0:
            adjusted = {(k[0] - coord[0], k[1] - coord[1]): v for k, v in asteroids.items()}
            sections = []

            sections.append(([k for k, v in adjusted.items() if k[0] == 0 and k[1] < 0 if v == '#'], False))    # Top
            sections.append(([k for k, v in adjusted.items() if k[0] > 0 and k[1] < 0 if v == '#'], False))     # Top Right
            sections.append(([k for k, v in adjusted.items() if k[0] > 0 and k[1] == 0 if v == '#'], True))     # Right
            sections.append(([k for k, v in adjusted.items() if k[0] > 0 and k[1] > 0 if v == '#'], False))     # Bottom Right
            sections.append(([k for k, v in adjusted.items() if k[0] == 0 and k[1] > 0 if v == '#'], True))     # Bottom
            sections.append(([k for k, v in adjusted.items() if k[0] < 0 and k[1] > 0 if v == '#'], False))     # Bottom Left
            sections.append(([k for k, v in adjusted.items() if k[0] < 0 and k[1] == 0 if v == '#'], False))    # Left
            sections.append(([k for k, v in adjusted.items() if k[0] < 0 and k[1] < 0 if v == '#'], False))     # Top Left

            for i in range(len(sections)):
                if len(sections[i][0]) == 0:
                    continue
                if i % 2 == 0:
                    if sections[i][0][0][0] == 0:
                        # sort with respect to y
                        sections[i] = sorted(sections[i][0], key=lambda x: x[1], reverse=sections[i][1])
                    else:
                        # sort with respect to x
                        sections[i] = sorted(sections[i][0], key=lambda x: x[0], reverse=sections[i][1])
                    continue
                sections[i] = sorted(sections[i][0], key=lambda x: (x[1] / x[0], x[0] + x[1]), reverse=sections[i][1])

            for i in range(len(sections)):
                sections[i] = [(k[0] + coord[0], k[1] + coord[1]) for k in sections[i]]

        last = (1, 1e9)

        for c in sections[section % 8]:
            if is_visible(asteroids, coord, c) and get_steps(coord, c) != get_steps(coord, last):
                last = c
                vap += 1
                if vap == index:
                    return c
                asteroids[c] = '.'

        section += 1


visible = dd(lambda: set())

for k, v in asteroids.items():
    if v == "#":
        for k1, v1 in asteroids.items():
            if k == k1:
                continue
            if v1 == "#" and is_visible(asteroids, k, k1):
                visible[k].add(k1)

highest = 0
highest_coord = (0, 0)

for k, v in visible.items():
    if len(v) > highest:
        highest_coord = k
        highest = len(v)

print(f"Part 1: {highest}")

c = vaporise(asteroids, highest_coord, 200)

print(f"Part 2: {c[0] * 100 + c[1]}")
