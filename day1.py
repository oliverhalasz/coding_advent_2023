SUBSTINGS = ["one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]

with open("C:/Users/Oliver/Documents/coding_advent2023/day1.txt", "r") as f:
    lines = f.read().split("\n")

s = 0
for line in lines:
    i, j = 0, len(line) - 1
    num = ""
    # Első szám
    while 1:
        try:
            int(line[i])
        except ValueError:
            i += 1
            continue
        else:
            break
    # Első írt szám
    temp_s = line[i]
    for number, substring in enumerate(SUBSTINGS, 1):
        k = line.find(substring)
        if k != -1 and k < i:
            i = k
            temp_s = str(number)
    num += temp_s

    while 1:
        try:
            int(line[j])
        except ValueError:
            j -= 1
            continue
        else:
            break
    # Első írt szám
    temp_s = line[j]
    for number, substring in enumerate(SUBSTINGS, 1):
        k = line.rfind(substring)
        if k != -1 and k > j:
            j = k
            temp_s = str(number)
    num += temp_s

    s += int(num)
print(s)
