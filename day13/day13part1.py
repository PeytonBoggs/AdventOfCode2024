import re
import math
import numpy as np

f = open("day13/day13_input.txt", "r")

input = f.read()
input = input.split("\n\n")

tokens = 0

for machine in input:
    nums = re.findall("[0-9]+", machine)
    aX, aY, bX, bY, prizeX, prizeY = int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]), int(nums[4]), int(nums[5]), 

    a = np.array([[aX, bX], [aY, bY]])
    b = np.array([prizeX, prizeY])
    solution = np.linalg.solve(a, b)
    round_solution = [round(solution[0]), round(solution[1])]

    if math.isclose(solution[0], round_solution[0]) and math.isclose(solution[1], round_solution[1]):
        tokens += (3 * round_solution[0]) + round_solution[1]

print(tokens)