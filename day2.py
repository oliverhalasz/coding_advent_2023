import regex as re
import time

start = time.time()
with open("C:/Users/Oliver/Documents/coding_advent2023/day2.txt", "r") as f:
    lines = f.read().split("\n")

REDS, GREENS, BLUES = 12, 13, 14

sum_of_ids = 0
for line in lines:
    max_reds = 0
    max_greens = 0
    max_blues = 0

    # Hányadik játék
    game_id = int(re.search("\d+", line).group())

    pulls = line.split(";")

    for pull in pulls:
        # Pirosak
        num_reds = re.findall("\d+ red", pull)
        if len(num_reds) > 0:
            max_reds = max(max_reds, int(re.findall("\d+", num_reds[0])[0]))

        # Zöldek
        num_greens = re.findall("\d+ green", pull)
        if len(num_greens) > 0:
            max_greens = max(max_greens, int(
                re.findall("\d+", num_greens[0])[0]))

        # Kékek
        num_blues = re.findall("\d+ blue", pull)
        if len(num_blues) > 0:
            max_blues = max(max_blues, int(re.findall("\d+", num_blues[0])[0]))

    # Lehetséges a játék?
    if max_reds <= REDS and max_greens <= GREENS and max_blues <= BLUES:
        sum_of_ids += game_id

print(sum_of_ids)
print(time.time() - start)