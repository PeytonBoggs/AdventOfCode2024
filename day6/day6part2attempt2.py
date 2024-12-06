import copy

def trymap(map):
    guard_pos = [0, 0]

    i = 0
    while (i < len(map)):
        j = 0
        while (j < len(map[i])):
            if (map[i][j] == "^"):
                guard_pos = [i, j]
            j += 1
        i += 1

    map[guard_pos[0]][guard_pos[1]] = "X"
    guard_dir = "up"

    num_positions = 1
    in_bounds = True
    num_steps = 0

    while (in_bounds):
        if guard_dir == "up":
            if (guard_pos[0] - 1 < 0):
                in_bounds = False
            elif (map[guard_pos[0] - 1][guard_pos[1]] == "#"):
                guard_dir = "right"
            elif (map[guard_pos[0] - 1][guard_pos[1]] == "X"):
                guard_pos = [guard_pos[0] - 1, guard_pos[1]]
            elif (map[guard_pos[0] - 1][guard_pos[1]] == "."):
                guard_pos = [guard_pos[0] - 1, guard_pos[1]]
                map[guard_pos[0]][guard_pos[1]] = "X"
                num_positions += 1
        elif guard_dir == "right":
            if (guard_pos[1] + 1 >= len(map[0])):
                in_bounds = False
            elif (map[guard_pos[0]][guard_pos[1] + 1] == "#"):
                guard_dir = "down"
            elif (map[guard_pos[0]][guard_pos[1] + 1] == "X"):
                guard_pos = [guard_pos[0], guard_pos[1] + 1]
            elif (map[guard_pos[0]][guard_pos[1] + 1] == "."):
                guard_pos = [guard_pos[0], guard_pos[1] + 1]
                map[guard_pos[0]][guard_pos[1]] = "X"
                num_positions += 1
        elif guard_dir == "down":
            if (guard_pos[0] + 1 >= len(map)):
                in_bounds = False
            elif (map[guard_pos[0] + 1][guard_pos[1]] == "#"):
                guard_dir = "left"
            elif (map[guard_pos[0] + 1][guard_pos[1]] == "X"):
                guard_pos = [guard_pos[0] + 1, guard_pos[1]]
            elif (map[guard_pos[0] + 1][guard_pos[1]] == "."):
                guard_pos = [guard_pos[0] + 1, guard_pos[1]]
                map[guard_pos[0]][guard_pos[1]] = "X"
                num_positions += 1
        elif guard_dir == "left":
            if (guard_pos[1] - 1 < 0):
                in_bounds = False
            elif (map[guard_pos[0]][guard_pos[1] - 1] == "#"):
                guard_dir = "up"
            elif (map[guard_pos[0]][guard_pos[1] - 1] == "X"):
                guard_pos = [guard_pos[0], guard_pos[1] - 1]
            elif (map[guard_pos[0]][guard_pos[1] - 1] == "."):
                guard_pos = [guard_pos[0], guard_pos[1] - 1]
                map[guard_pos[0]][guard_pos[1]] = "X"
                num_positions += 1
        num_steps += 1
        if (num_steps > 25000):
            return True
        
    return False

f = open("day6/day6_input.txt", "r")

map = []

for line in f:
    line = list(line)
    line.pop()
    map.append(line)

num_obstacles = 0

i = 0
while (i < len(map)):
    j = 0
    while (j < len(map[i])):
        if (map[i][j] == "."):
            mapcopy = copy.deepcopy(map)
            mapcopy[i][j] = "#"
            if trymap(mapcopy):
                num_obstacles += 1
            mapcopy.clear()
        j += 1
    i += 1

print(num_obstacles)