import numpy as np

with open("C:/Users/Oliver/Documents/coding_advent2023/day9.txt","r") as f:
    lines = f.read().split("\n")

for i, line in enumerate(lines):
    lines[i] = np.array(list(map(int, line.split())))

s = []
for line in lines:
    new_line = line.copy()
    last_elements = []
    while np.sum(new_line != 0) != 0:
        last_elements.append(new_line[-1])
        new_line = np.diff(new_line)
    s.append(sum(last_elements))
s = np.array(s, dtype=np.int64)
print(s.sum())
