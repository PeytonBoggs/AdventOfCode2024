import re

f = open("day14/day14_input.txt", "r")

robots = []

for line in f:
    pX, pY, vX, vY = re.findall("-?[0-9]+", line)
    robots.append([int(pX), int(pY), int(vX), int(vY)])

# Map data
seconds = 100
map_width = 101
map_height = 103

# Quadrant data
top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0

i = 0
while i < len(robots):
    # Move robots
    robots[i][0] = (robots[i][0] + (seconds * robots[i][2])) % map_width
    robots[i][1] = (robots[i][1] + (seconds * robots[i][3])) % map_height
    
    # Determine quadrant
    if robots[i][0] < map_width // 2 and robots[i][1] < map_height // 2:
        top_left += 1
    elif robots[i][0] > map_width // 2 and robots[i][1] < map_height // 2:
        top_right += 1
    elif robots[i][0] < map_width // 2 and robots[i][1] > map_height // 2:
        bottom_left += 1
    elif robots[i][0] > map_width // 2 and robots[i][1] > map_height // 2:
        bottom_right += 1

    i += 1

safetyfactor = top_left * top_right * bottom_left * bottom_right
print(safetyfactor)