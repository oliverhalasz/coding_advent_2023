from time import time
from regex import findall

start = time()
with open("C:/Users/Oliver/Documents/coding_advent2023/day8.txt", "r") as f:
    lines = f.read().split("\n")

directions = lines[0]
del lines[0:2]

coordinates = [findall("[A-Z1-9]+", element) for element in lines]
starting_positions = [coordinate[0] for coordinate in coordinates]

def is_final_loc(list_of_loc):
    for element in list_of_loc:
        if element[-1] != "Z":
            return False
    return True

i = 0
steps = 0
current_locs = [starting_pos for starting_pos in starting_positions if starting_pos[-1]=="A"]

n = len(directions)
while not is_final_loc(current_locs):
    for k, current_loc in enumerate(current_locs):
        j = starting_positions.index(current_loc)
        if directions[i] == "L":
            current_loc = coordinates[j][1]
        else:
            current_loc = coordinates[j][2]
        current_locs[k] = current_loc
    steps += 1
    i = (i + 1) % n

print(steps)
print(time() - start)
