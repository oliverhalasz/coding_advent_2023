import time

start = time.time()

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
    # Utsó szám
    while 1:
        try:
            int(line[j])
        except ValueError:
            j -= 1
            continue
        else:
            break
    # Utsó írt szám
    temp_s = line[j]
    for number, substring in enumerate(SUBSTINGS, 1):
        k = line.rfind(substring)
        if k != -1 and k > j:
            j = k
            temp_s = str(number)
    num += temp_s

    s += int(num)
print(s)
print(time.time() - start)



def recover_calibration_values(calibration_document):
    # Initialize the sum of calibration values
    total_sum = 0
    
    # Iterate through each line in the calibration document
    for line in calibration_document:
        # Extract the first and last digits
        first_digit = int(line[0])
        last_digit = int(line[-1])
        
        # Combine the digits to form a two-digit number
        calibration_value = int(str(first_digit) + str(last_digit))
        
        # Add the calibration value to the total sum
        total_sum += calibration_value
    
    return total_sum

# Example usage with the provided calibration document

result = recover_calibration_values(lines)

print("The sum of calibration values is:", result)
