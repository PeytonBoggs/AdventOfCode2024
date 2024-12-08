def findmatch(map, loc_a, found_matches):
    i = 0
    while (i < len(map)):
        j = 0
        while (j < len(map[i])):
            if ((map[i][j] == map[loc_a[0]][loc_a[1]]) and not ([i, j] in found_matches) and (loc_a[0] < i or (loc_a[0] == i and loc_a[1] < j))):
                return [i, j]
            j += 1
        i += 1
    return None

f = open("day8/day8_input.txt", "r")

map = []

for line in f:
    line = line.strip()
    map.append(line)

antinode_map = []
found_matches = []

i = 0
while (i < len(map)):
    j = 0
    while (j < len(map[i])):
        if (map[i][j] != "."):
            loc_a = [i, j]
            found_matches.append(loc_a)
            loc_b = findmatch(map, loc_a, found_matches)
            found_matches.append(loc_b)
            all_matches_found = False

            while (not all_matches_found):
                if ((loc_b != None)):
                    if (loc_a[1] <= loc_b[1]):
                        antinode_one = [loc_a[0] - abs(loc_a[0] - loc_b[0]), loc_a[1] - abs(loc_a[1] - loc_b[1])]
                        antinode_two = [loc_b[0] + abs(loc_a[0] - loc_b[0]), loc_b[1] + abs(loc_a[1] - loc_b[1])]
                    else:
                        antinode_one = [loc_a[0] - abs(loc_a[0] - loc_b[0]), loc_a[1] + abs(loc_a[1] - loc_b[1])]
                        antinode_two = [loc_b[0] + abs(loc_a[0] - loc_b[0]), loc_b[1] - abs(loc_a[1] - loc_b[1])]

                    if (antinode_one[0] >= 0 and antinode_one[1] >= 0 and antinode_one[1] < len(map[0]) and not (antinode_one in antinode_map)):
                        antinode_map.append(antinode_one)
                    if (antinode_two[0] < len(map) and antinode_two[1] >= 0 and antinode_two[1] < len(map[0]) and not antinode_two in antinode_map):
                        antinode_map.append(antinode_two)
                    loc_b = findmatch(map, loc_b, found_matches)
                    found_matches.append(loc_b)
                if (loc_b == None):
                    all_matches_found = True
        found_matches = []
        j += 1
    i += 1

num_antinodes = 0

for antinode in antinode_map:
    num_antinodes += 1

print(num_antinodes)