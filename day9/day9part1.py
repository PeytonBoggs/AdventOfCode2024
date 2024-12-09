f = open("day9/day9_input.txt", "r")

raw_disk = f.read()
disk_map = []

# Format disk map
i = 0
while (i < len(raw_disk) - 2):
    # File block
    file_block = [int(i/2)]*int(raw_disk[i])
    for file in file_block:
            disk_map.append(file)
    # Free block
    free_block = ["."]*int(raw_disk[i+1])
    for free in free_block:
            disk_map.append(free)
    i += 2
# Final file block
file_block = [int(i/2)]*int(raw_disk[i])
for file in file_block:
    disk_map.append(file)

# Compact disk map
compact = False

index_first_free = 0
index_last_file = len(disk_map) - 1

while not compact:
    # Get first "."
    while (index_first_free < len(disk_map)):
        if (disk_map[index_first_free] == "."):
             break
        index_first_free += 1

    # Get last file
    while (index_last_file > 0):
        if(disk_map[index_last_file] != "."):
            break
        index_last_file -= 1

    # Check if compact
    if (index_last_file < index_first_free):
        compact = True

    # Swap
    if not compact:
        disk_map[index_first_free], disk_map[index_last_file] = disk_map[index_last_file], disk_map[index_first_free]

checksum = 0

i = 0
while (disk_map[i] != "."):
    checksum += (i * disk_map[i])
    i += 1

print(checksum)