def canMoveUp(position):
    next = [position[0] - 1, position[1]]
    if map[next[0]][next[1]] == ".":
        return True
    elif map[next[0]][next[1]] == "#":
        return False
    elif map[next[0]][next[1]] == "[":
        return canMoveUp(next) and canMoveUp([next[0], next[1] + 1])
    elif map[next[0]][next[1]] == "]":
        return canMoveUp(next) and canMoveUp([next[0], next[1] - 1])
    
def moveUp(position):
    next = [position[0] - 1, position[1]]
    if map[next[0]][next[1]] == ".":
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
    elif map[next[0]][next[1]] == "[":
        moveUp(next)
        moveUp([next[0], next[1] + 1])
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
    elif map[next[0]][next[1]] == "]":
        moveUp(next)
        moveUp([next[0], next[1] - 1])
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
        
def canMoveRight(position):
    next = [position[0], position[1] + 1]
    if map[next[0]][next[1]] == ".":
        return True
    elif map[next[0]][next[1]] == "#":
        return False
    else:
        return canMoveRight(next)
    
def moveRight(position):
    next = [position[0], position[1] + 1]
    if map[next[0]][next[1]] == ".":
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
    else:
        moveRight(next)
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."

def canMoveDown(position):
    next = [position[0] + 1, position[1]]
    if map[next[0]][next[1]] == ".":
        return True
    elif map[next[0]][next[1]] == "#":
        return False
    elif map[next[0]][next[1]] == "[":
        return canMoveDown(next) and canMoveDown([next[0], next[1] + 1])
    elif map[next[0]][next[1]] == "]":
        return canMoveDown(next) and canMoveDown([next[0], next[1] - 1])
    
def moveDown(position):
    next = [position[0] + 1, position[1]]
    if map[next[0]][next[1]] == ".":
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
    elif map[next[0]][next[1]] == "[":
        moveDown(next)
        moveDown([next[0], next[1] + 1])
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
    elif map[next[0]][next[1]] == "]":
        moveDown(next)
        moveDown([next[0], next[1] - 1])
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."

def canMoveLeft(position):
    next = [position[0], position[1] - 1]
    if map[next[0]][next[1]] == ".":
        return True
    elif map[next[0]][next[1]] == "#":
        return False
    else:
        return canMoveLeft(next)
    
def moveLeft(position):
    next = [position[0], position[1] - 1]
    if map[next[0]][next[1]] == ".":
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
    else:
        moveLeft(next)
        map[next[0]][next[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."

def attemptMove(move, robot):
    # Move Up
    if move == "^" and canMoveUp(robot):
        moveUp(robot)
        robot[0] -= 1

    # Move Right
    if move == ">" and canMoveRight(robot):
        moveRight(robot)
        robot[1] += 1
    
    # Move Down
    if move == "v" and canMoveDown(robot):
        moveDown(robot)
        robot[0] += 1

    # Move Left
    if move == "<" and canMoveLeft(robot):
        moveLeft(robot)
        robot[1] -= 1

# Open File
f = open("day15/day15_input.txt", "r")

input = f.read()
input = input.split("\n\n")

str_map = input[0]

# Initialize Scaled Map
map = []
mapline = []
for char in str_map:
    if char == "\n":
        map.append(mapline)
        mapline = []
    else:
        if char == "#":
            mapline.append("#")
            mapline.append("#")
        elif char == ".":
            mapline.append(".")
            mapline.append(".")
        elif char == "O":
            mapline.append("[")
            mapline.append("]")
        elif char == "@":
            mapline.append("@")
            mapline.append(".")
map.append(mapline)

robot = [0, 0]

# Find Robot
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == "@":
            robot = [i , j]

# Move Robot
moves = input[1]
moves = moves.replace("\n", "")

for move in moves:
    attemptMove(move, robot)

# Get GPS Sum
gps_sum = 0

i = 0
while i < len(map):
    j = 0
    while j < len(map[i]):
        if map[i][j] == "[":
            gps_sum += 100 * i + j
        j += 1
    i += 1

print(gps_sum)