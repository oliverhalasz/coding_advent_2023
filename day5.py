from regex import findall
from time import time

start = time()
with open("C:/Users/Oliver/Documents/coding_advent2023/day5.txt", "r") as f:
    text = f.read().split("\n\n")

lines = [category.split("\n") for category in text]

seeds = list(map(int, findall("\d+", lines[0][0])))
del lines[0]


conversions = []
for conversion in lines:
    n = len(conversion)
    category = []
    for i in range(1, n):
        category.append(list(map(int, conversion[i].split(" "))))
    conversions.append(category)



def seed_iteration(seed, i=0):
    try:
        conversions[i]
    except IndexError:
        return seed

    for line in conversions[i]:
        dest_start = line[0]
        source_start = line[1]
        range_len = line[2]

        mapped = False

        if seed in range(source_start, source_start+range_len):
            step = seed - source_start
            seed = dest_start + step
            mapped = True
            break

        if mapped:
            break
    return seed_iteration(seed, i+1)


lowest_location = min([seed_iteration(seed) for seed in seeds])
print(lowest_location)
print(time()-start)
