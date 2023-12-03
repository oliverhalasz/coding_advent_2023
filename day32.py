import regex as re
import numpy as np
import time

start = time.time()


with open("C:/Users/Oliver/Documents/coding_advent2023/day3.txt", "r") as f:
    lines = f.read().split("\n")

NON_SYMBOLS = [*map(str, range(10))]
NON_SYMBOLS.append(".")

numbers_with_coords = []
symbols_coords = []
astrix_coords = []
req_numbers = []
astrix_neighbors = {}

for i, line in enumerate(lines):
    matches = re.finditer("\d+", line)
    for match in matches:
        l = [i, match.start(), match.end(), int(match.group())]
        numbers_with_coords.append(l)
    for j, char in enumerate(line):
        if char not in NON_SYMBOLS:
            symbols_coords.append((i, j))
        if char == "*":
            astrix_coords.append((i, j))

astrix_neighbors = {coor: [] for coor in astrix_coords}

for number_coor in numbers_with_coords:
    x = number_coor[0]
    y = np.arange(number_coor[1], number_coor[2])
    number = number_coor[3]

    for coor in astrix_coords:
        top_to_bottom = list(range(coor[0]-1, coor[0] + 2))
        left_to_right = list(range(coor[1]-1, coor[1] + 2))

        egyik = x in top_to_bottom
        masik = np.array([i in left_to_right for i in y]).any()
        if egyik and masik:
            astrix_neighbors[coor].append(number)
        elif top_to_bottom[0] > x and left_to_right[0] > y[-1]:
            break


s = 0
for key, value in astrix_neighbors.items():
    if len(value) == 2:
        # print(f"Koordináta: {key}, számok: {value}")
        s += value[0]*value[1]
print(s)
print(time.time() - start)
