import re
import math

f = open("day5/day5_input.txt", "r")
input = f.read()

input_rules = re.findall("[1-9][0-9]\|[1-9][0-9]", input)
rules = []

for rule in input_rules:
    nums = re.findall("[1-9][0-9]", rule)
    rules.append(nums)

updates = re.findall("(?:(?:[1-9][0-9],)+[1-9][0-9])", input)

sum_middle_pages = 0

for update in updates:
    correctly_ordered = True
    pages = re.findall("[1-9][0-9]", update)
    
    i=0
    while (i < len(pages)):
        for rule in rules:
            if (pages[i] == rule[1]):
                j = i + 1
                while (j < len(pages)):
                    if (pages[j] == rule[0]):
                        correctly_ordered = False
                    j += 1
        i += 1
    
    if (correctly_ordered):
        sum_middle_pages += int(pages[math.floor(len(pages)/2)])

print(sum_middle_pages)
