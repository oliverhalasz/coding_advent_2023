from regex import findall
from time import time

start = time()

with open("C:/Users/Oliver/Documents/coding_advent2023/day6.txt", "r") as f:
    lines = f.read().split("\n")

TIMES = [*map(int, findall("\d+", lines[0]))]
RECORDS = [*map(int, findall("\d+", lines[1]))]

product = 1
for t, record in zip(TIMES, RECORDS):
    t1 = (t + (t**2 - 4*record) ** 0.5) / 2
    t0 = (t - (t**2 - 4*record) ** 0.5) / 2
    if t1 != t1.real:
        continue
    else:
        product *= int(t1) - (int(t0)+1) + 1
print(product)
print(time()-start)
