import re
import time

def addSecond(robots):
    for i in range(0, len(robots)):
        robots[i][0] = (robots[i][0] + robots[i][2]) % map_width
        robots[i][1] = (robots[i][1] + robots[i][3]) % map_height


def printmap(width, length, robots):
    map = []
    for i in range(0, length):
        map.append([])
        for j in range(0, width):
            map[i].append(" ")

    for robot in robots:
        map[robot[1]][robot[0]] = "█"
    
    for line in map:
        print(line)

f = open("day14_input.txt", "r")

robots = []

for line in f:
    pX, pY, vX, vY = re.findall("-?[0-9]+", line)
    robots.append([int(pX), int(pY), int(vX), int(vY)])

# Map data
map_width = 101
map_height = 103

second = 58
for _ in range (0, 58):
        addSecond(robots)
while (1):
    printmap(map_width, map_height, robots)
    print("Second", second)
    
    time.sleep(1)
    
    second += 103
    for _ in range (0, 103):
        addSecond(robots)
    print(chr(27) + "[2J")