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


def getTrails(i ,j, trails):
    if (map[i][j] == 9):
        return map[i][j]
    
    dirs = trailDirection(i, j)

    if dirs == []:
        return map[i][j]
    
    for dir in dirs:
        trails.append(map[i][j])
        trails.append(getTrails(dir[0], dir[1], trails))
    
    return trails

f = open("day10/day10_input.txt", "r")

map = []

for line in f:
    mapline = []
    for char in line:
        if char != '\n':
            mapline.append(int(char))
    map.append(mapline)

totalRating = 0

i = 0
while i < len(map):
    j = 0
    while j < len(map[i]):
        if map[i][j] == 0:
            rating = 0
            trails = getTrails(i, j, [])
            for endpoint in trails:
                if endpoint == 9:
                    rating += 1
            totalRating += rating

        j += 1
    i += 1

print(totalRating)