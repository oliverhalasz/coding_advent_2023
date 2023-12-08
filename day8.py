from time import time
from regex import findall

start = time()
with open("C:/Users/Oliver/Documents/coding_advent2023/day8.txt", "r") as f:
    lines = f.read().split("\n")

directions = lines[0]
del lines[0:2]

coordinates = [findall("[A-Z]+", element) for element in lines]
starting_positions = [coordinate[0] for coordinate in coordinates]

i = 0
steps = 0
current_loc = "AAA"
n = len(directions)
while current_loc != "ZZZ":
    j = starting_positions.index(current_loc)
    if directions[i] == "L":
        current_loc = coordinates[j][1]
    else:
        current_loc = coordinates[j][2]
    steps += 1
    i = (i + 1) % n

print(steps)
print(time() - start)
