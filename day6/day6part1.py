f = open("day6/day6_input.txt", "r")

map = []

for line in f:
    line = list(line)
    line.pop()
    map.append(line)

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
num_positions = 1

guard_dir = "up"
in_bounds = True

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

print(num_positions)
    
