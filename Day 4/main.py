

f = open("input.txt")
numbers = [int(x) for x in f.read().split("-")]
f.close()

matches = 0

for x in range(numbers[0], numbers[1] + 1, 1):
    match = False
    has_double = False
    prev = 0
    for digit in str(x):
        if int(digit) < prev:
            match = False
            break
        if int(digit) == prev:
            match = True
        prev = int(digit)
    if match:
        matches += 1

print("Part 1:", matches)

matches = 0

for x in range(numbers[0], numbers[1] + 1, 1):
    number = str(x)
    ascending = True
    split_numbers = []
    
    for y in range(len(number)):
        if y != len(number) - 1:
            if int(number[y]) > int(number[y + 1]):
                ascending = False
                break

        if len(split_numbers) != 0:
            if split_numbers[-1][0] == number[y]:
                split_numbers[-1] = split_numbers[-1] + number[y]
            else:
                split_numbers.append(number[y])
        else:
            split_numbers.append(number[y])

    if ascending and len([x for x in split_numbers if len(x) == 2]) > 0:
        matches += 1

print("Part 2:", matches)