import re

f = open("day3/day3_input.txt", "r")

chars = f.read()
regex = "mul\([0-9]{1,3},[0-9]{1,3}\)"
matches = re.findall(regex, chars)

sum = 0

for match in matches:
    nums = re.findall("[0-9]{1,3}", match)
    sum += int(nums[0]) * int(nums[1])

print(sum)

f.close()