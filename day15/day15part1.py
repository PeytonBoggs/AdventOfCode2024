def attemptMove(map, move, robot):
    nextSpace = None

    # Move Up    
    if move == "^":
        i = robot[0]
        while i > 0:
            if map[i][robot[1]] == ".":
                nextSpace = (i, robot[1])
                break
            if map[i][robot[1]] == "#":
                break
            i -= 1
        if nextSpace != None:
            map[nextSpace[0]][nextSpace[1]] = "O"
            map[robot[0] - 1][robot[1]] = "@"
            map[robot[0]][robot[1]] = "."
            robot[0] -= 1
    # Move Right   
    elif move == ">":
        j = robot[1]
        while j < len(map[0]):
            if map[robot[0]][j] == ".":
                nextSpace = (robot[0], j)
                break
            if map[robot[0]][j] == "#":
                break
            j += 1
        if nextSpace != None:
            map[nextSpace[0]][nextSpace[1]] = "O"
            map[robot[0]][robot[1] + 1] = "@"
            map[robot[0]][robot[1]] = "."
            robot[1] += 1
    # Move Down 
    if move == "v":
        i = robot[0]
        while i < len(map):
            if map[i][robot[1]] == ".":
                nextSpace = (i, robot[1])
                break
            if map[i][robot[1]] == "#":
                break
            i += 1
        if nextSpace != None:
            map[nextSpace[0]][nextSpace[1]] = "O"
            map[robot[0] + 1][robot[1]] = "@"
            map[robot[0]][robot[1]] = "."
            robot[0] += 1
    # Move Left
    elif move == "<":
        j = robot[1]
        while j > 0:
            if map[robot[0]][j] == ".":
                nextSpace = (robot[0], j)
                break
            if map[robot[0]][j] == "#":
                break
            j -= 1
        if nextSpace != None:
            map[nextSpace[0]][nextSpace[1]] = "O"
            map[robot[0]][robot[1] - 1] = "@"
            map[robot[0]][robot[1]] = "."
            robot[1] -= 1

# Open File
f = open("day15/day15_input.txt", "r")

input = f.read()
input = input.split("\n\n")

str_map = input[0]

# Initialize Map
map = []
mapline = []
for char in str_map:
    if char == "\n":
        map.append(mapline)
        mapline = []
    else:
        mapline.append(char)

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
    attemptMove(map, move, robot)

# Get GPS Sum
gps_sum = 0

i = 0
while i < len(map):
    j = 0
    while j < len(map[i]):
        if map[i][j] == "O":
            gps_sum += 100 * i + j
        j += 1
    i += 1

print(gps_sum)