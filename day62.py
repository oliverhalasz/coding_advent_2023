from regex import findall
from time import time

start = time()

with open("C:/Users/Oliver/Documents/coding_advent2023/day6.txt", "r") as f:
    lines = f.read().split("\n")

T = int("".join(findall("\d+", lines[0])))
record = int("".join(findall("\d+", lines[1])))

product = 1

t1 = (T + (T**2-4*record)**0.5) / 2
t0 = (T - (T**2-4*record)**0.5) / 2
if t1 == t1.real:
    product *= int(t1) - (int(t0)+1) + 1

print(product)
print(time()-start)
