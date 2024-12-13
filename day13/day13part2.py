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

    prizeX += 10000000000000
    prizeY += 10000000000000

    a = np.array([[aX, bX], [aY, bY]])
    b = np.array([prizeX, prizeY])
    solution = np.linalg.solve(a, b)
    round_solution = [round(solution[0]), round(solution[1])]

    difference = solution - round_solution
      
    if np.allclose(difference, [0,0], 1e-02, 1e-02):
        tokens += (3 * round_solution[0]) + round_solution[1]

print(tokens)