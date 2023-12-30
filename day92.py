from functools import reduce
import numpy as np

with open("C:/Users/Oliver/Documents/coding_advent2023/day9.txt", "r") as f:
    lines = f.read().split("\n")

for i, line in enumerate(lines):
    lines[i] = np.array(list(map(int, line.split())))

s = 0
for line in lines:
    new_line = line.copy()
    first_elements = []
    while np.sum(new_line != 0) != 0:
        first_elements.append(new_line[0])
        new_line = np.diff(new_line)
    first_elements = first_elements[::-1]
    s += reduce(lambda a, b: b - a, first_elements)

print(s)
