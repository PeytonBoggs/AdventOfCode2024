def trailDirection(i , j):
    dirs = []
    #Up
    if (i-1 >= 0 and map[i-1][j] == map[i][j] + 1):
        dirs.append([i-1, j])
    #Right
    if (j+1 < len(map[i]) and map[i][j+1] == map[i][j] + 1):
        dirs.append([i, j+1])
    #Down
    if (i+1 < len(map) and map[i+1][j] == map[i][j] + 1):
        dirs.append([i+1, j])
    #Left
    if (j-1 >= 0 and map[i][j-1] == map[i][j] + 1):
        dirs.append([i, j-1]) 
    return dirs


def getScore(i ,j, seen9s):
    if (map[i][j] == 9 and [i, j] not in seen9s):
        seen9s.append([i, j])
        return seen9s
    
    dirs = trailDirection(i, j)

    if dirs == []:
        return seen9s
    
    for dir in dirs:
        seen9s = getScore(dir[0], dir[1], seen9s)

    return seen9s

f = open("day10/day10_input.txt", "r")

map = []

for line in f:
    mapline = []
    for char in line:
        if char != '\n':
            mapline.append(int(char))
    map.append(mapline)

totalScore = 0

i = 0
while i < len(map):
    j = 0
    while j < len(map[i]):
        if map[i][j] == 0:
            totalScore += len(getScore(i, j, []))
        j += 1
    i += 1

print(totalScore)
