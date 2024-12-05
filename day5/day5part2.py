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

def orderPages(pages, rules, correctly_ordered):
    i=0
    while (i < len(pages)):
        for rule in rules:
            if (pages[i] == rule[1]):
                j = i + 1
                while (j < len(pages)):
                    if (pages[j] == rule[0]):
                        correctly_ordered = False
                        temp = pages[j]
                        pages[j] = pages[i]
                        pages[i] = temp
                        return orderPages(pages, rules, correctly_ordered)
                    j += 1
        i += 1
    
    return pages, rules, correctly_ordered

sum_middle_pages = 0

for update in updates:
    correctly_ordered = True
    pages = re.findall("[1-9][0-9]", update)
    
    pages, rules, correctly_ordered = orderPages(pages, rules, correctly_ordered)
    
    if not correctly_ordered:
        sum_middle_pages += int(pages[math.floor(len(pages)/2)])

print(sum_middle_pages)