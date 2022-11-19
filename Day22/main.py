from copy import deepcopy
import time

def deal_into_new_stack(s):
    return s[::-1]

def deal_into_new_stack2(s, pos):
    # input(5, 1)
    # 0 1 2 3 4
    #   ^
    # 5 - 1 - 1 = 3
    return s - pos - 1

def cut(s, n):
    new_stack = []

    first = s[n:]
    last = s[:n]

    for f in first:
        new_stack.append(f)
    for l in last:
        new_stack.append(l)

    return new_stack

def cut2(s, n, pos):
    # This needs testing
    # Also needs to consider which side of the cut the position is on
    # This needs to be redone so that it calculates the position before the cut, instead of after one
    if n > 0:
        # From top of deck
        if pos >= (s - n):
            # Pos in top
            # inputs (10, 3, 8)
            # 0 1 2 3 4 5 6   7 8 9
            # ---------------------
            # 3 4 5 6 7 8 9 | 0 1 2
            #                   ^
            # 0 1 2   3 4 5 6 7 8 9
            # ---------------------
            # 0 1 2 | 3 4 5 6 7 8 9
            #   ^
            # 
            assert cards > pos - (s - n) >= 0
            return pos - (s - n)
            # return s - (n - pos)
        else:
            # Pos in bottom
            # inputs (10, 3, 2)
            # 0 1 2 3 4 5 6   7 8 9
            # ---------------------
            # 3 4 5 6 7 8 9 | 0 1 2
            #     ^
            # 0 1 2   3 4 5 6 7 8 9
            # ---------------------
            # 0 1 2 | 3 4 5 6 7 8 9
            #             ^
            assert cards > pos + n >= 0
            return pos + n
            # return pos - n
    else:
        # From bottom of deck
        if pos >= -n:
            # Pos in bottom
            # inputs (10, -3, 8)
            # 0 1 2   3 4 5 6 7 8 9
            # ---------------------
            # 7 8 9 | 0 1 2 3 4 5 6
            #                   ^
            # 0 1 2 3 4 5 6   7 8 9
            # ---------------------
            # 0 1 2 3 4 5 6 | 7 8 9
            #           ^
            # 
            assert cards > pos + n >= 0
            return pos + n
            # return pos - (s + n)
            # return pos - (s + n)
        else:
            # Pos in top
            # input (10, -3, 2)
            # 0 1 2   3 4 5 6 7 8 9
            # ---------------------
            # 7 8 9 | 0 1 2 3 4 5 6
            #     ^
            # 0 1 2 3 4 5 6   7 8 9
            # ---------------------
            # 0 1 2 3 4 5 6 | 7 8 9
            #                     ^
            assert cards > pos + (s + n) >= 0
            return pos + (s + n)
            # return s - (s + n) + pos

def increment(s, n):
    new_stack = [None for _ in range(len(s))]
    index = 0

    for x in range(0, len(s) * n, n):
        new_stack[x % len(s)] = s[index]
        index += 1

    assert all([x is not None for x in new_stack])
    return new_stack

def increment2(s, n, pos):
    assert n != 0
    # This is done backwards to find the index of the number that got placed in pos
    # (pos * n) % s == forward
    # ((pos * n) + s) / n
    # input = (10, 7, 4)
    # 0 1 2 3 4 5 6 7 8 9 | 0 1 2 3 4 5 6 7 8 9
    #                               ^
    # 0 1 2 3 4 5 6 7 8 9 | 0 1 2 3 4 5 6 7 8 9
    #     ^  
    # 0 1 2 3 4 5 6 7 8 9
    # 0 3 6 9 2 5 8 1 4 7
    decks = 0
    while ((decks * s) + pos) % n != 0:
        decks += 1
    return ((decks * s) + pos) // n
    # return ((pos * n) + s) / n

def do_actions(deck, instructions):
    for action in instructions:
        if action == "deal into new stack":
            deck = deal_into_new_stack(deck)
        elif action.startswith("cut"):
            parts = action.split(" ")
            amount = int(parts[1])
            deck = cut(deck, amount)
        else:
            parts = action.split(" ")
            inc = int(parts[3])
            deck = increment(deck, inc)
    return deck

def do_actions2(cards, instructions, pos, a, b):
    for action in list(reversed(instructions)): # run instructions backwards
        if action == "deal into new stack":
            # print(f"calling deal into stack 2 with cards: {cards}, pos: {pos}")
            pos = deal_into_new_stack2(cards, pos)
            # print(f"result of deal into new stack: {pos}")
            assert pos >= 0
        elif action.startswith("cut"):
            parts = action.split(" ")
            amount = int(parts[1])
            pos = cut2(cards, amount, pos)
            assert pos >= 0
        else:
            parts = action.split(" ")
            inc = int(parts[3])
            pos = increment2(cards, inc, pos)
            assert pos >= 0
    return a, b, pos

with open("input.txt") as f:
    instructions = [x.strip() for x in f.readlines() if x != ""]

deck = []

# for x in range(10):
for x in range(10007):
# for x in range(10):
    deck.append(x)

deck = do_actions(deck, instructions)

location = -1

for i, x in enumerate(deck):
    if x == 2019:
        location = i
        break

# print(deck)
print(f"Part 1: {location}")

iterations = 1
# iterations = 101741582076661
cards = 10007
# cards = 119315717514047
pos = 1867
# pos = 2020

# assert cut2(10, 3, 2) == 9
# assert cut2(10, 3, 5) == 2
# assert cut2(10, -3, 4) == 7
# assert cut2(10, -3, 8) == 1
print(f"cut2(10, 3, 2) -> {cut2(10, 3, 2)}")
print(f"cut2(10, 3, 8) -> {cut2(10, 3, 8)}")
print(f"cut2(10, -3, 2) -> {cut2(10, -3, 2)}")
print(f"cut2(10, -3, 8) -> {cut2(10, -3, 8)}")

# 0 1 2 3 4 5 6 7 8 9
# 0 3 6 9 2 5 8 1 4 7
assert increment2(10, 7, 0) == 0
assert increment2(10, 7, 1) == 3
assert increment2(10, 7, 2) == 6
assert increment2(10, 7, 3) == 9
assert increment2(10, 7, 4) == 2
assert increment2(10, 7, 5) == 5
assert increment2(10, 7, 6) == 8
assert increment2(10, 7, 7) == 1
assert increment2(10, 7, 8) == 4
assert increment2(10, 7, 9) == 7

count = 0
# DP = {pos: count}
inc = 0
start = time.time()
times = []

while count < iterations:
    a, b, pos = do_actions2(cards, instructions, pos, a, b)
    count += 1
    # if len(DP) % 10000 == 0:
    #     end = time.time()
    #     times.append(end - start)
    #     print(len(DP))
    #     start = time.time()
    # if pos in DP:
    #     print(DP[pos])
    #     break
    # DP[pos] = count
    # if len(visited) > 2:
    #     if visited[-1] - visited[-2] == visited[-2] - visited[-3]:
    #         # PATTERN FOUND
    #         inc = visited[-1] - visited[-2]
    #         break
    # if pos in DP:
    #     print("Repeat at count ==", count)
    # DP[pos] = count

print(f"increment2(10, 7, 4) -> {increment2(10, 7, 4)} -> expected: 2")
print(f"increment2(10, 7, 1) -> {increment2(10, 7, 1)} -> expected: 3")

# pos2 = deepcopy(pos)
# num = (cards - pos2) / inc
# pos2 += num * inc
# pos3 = do_actions2(cards, instructions, pos2)
# print("Pos2:", pos2, "Pos3:", pos3)

# pos += (iterations - count) * inc
# print("Pos before mod:", pos)
# pos %= cards


# average = sum(times) / len(times)

# mult = iterations / 10000

# print("Time to conquer:", str(mult * average))
# ~ 24.08 years to find answer... not willing to wait that long...

# print("DP:", DP)
print(f"Part 2: {pos}")



