import re

f = open("day3/day3_input.txt", "r")

chars = f.read()

sum = 0
enabled = True

i = 0
while (i < len(chars) - 10):
    if ((chars[i] + chars[i + 1] + chars[i + 2] + chars[i + 3]) == "do()"):
        enabled = True
    if ((chars[i] + chars[i + 1] + chars[i + 2] + chars[i + 3] + chars[i + 4] + chars[i + 5] + chars[i + 6]) == "don't()"):
        enabled = False

    if (((chars[i] + chars[i + 1] + chars[i + 2] + chars[i + 3]) == "mul(") & enabled):
        next12 = chars[i:i+12]
        if (re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", next12) != []):
            nums = re.findall("[0-9]{1,3}", next12)
            sum += int(nums[0]) * int(nums[1])

    i += 1

print(sum)