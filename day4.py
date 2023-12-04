from regex import findall
from time import time

start = time()
with open("C:/Users/Oliver/Documents/coding_advent2023/day4.txt", "r") as f:
    lines = f.read().split("\n")

card_counts = {i: 1 for i in range(1, len(lines)+1)}


for i, line in enumerate(lines, start=1):
    all_numbers = findall("\d+", line)
    del all_numbers[0]
    n = len(all_numbers)
    k = len(set(all_numbers))
    pairs = n-k
    if pairs > 0:
        for j in range(i + 1, i + pairs + 1):
            card_counts[j] += 1 * card_counts[i]

print(sum(card_counts.values()))
print(time() - start)
