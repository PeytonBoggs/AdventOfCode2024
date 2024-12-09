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

seen = []

while not compact:
    # Get last file
    while (index_last_file > 0):
        if(disk_map[index_last_file] != "." and disk_map[index_last_file] not in seen):
            seen.append(disk_map[index_last_file])
            break
        index_last_file -= 1

    # Get length of last file
    length_last_file = 1
    while (length_last_file < 10):
        if (disk_map[index_last_file - length_last_file] != disk_map[index_last_file]):
            break
        length_last_file += 1

    # Get first free with proper length
    index_first_free = 0
    while (index_first_free < len(disk_map)):
        if (disk_map[index_first_free : index_first_free + length_last_file] == ["."]*length_last_file):
             break
        index_first_free += 1

    # Swap
    if (index_last_file > index_first_free):
        disk_map[index_first_free : index_first_free + length_last_file], disk_map[index_last_file - length_last_file + 1: index_last_file + 1] = disk_map[index_last_file - length_last_file + 1: index_last_file + 1], disk_map[index_first_free : index_first_free + length_last_file]

    index_last_file -= length_last_file

    if (index_last_file <= 0):
        compact = True
        break

checksum = 0

i = 0
while (i < len(disk_map)):
    if disk_map[i] != ".":
        checksum += (i * disk_map[i])
    i += 1

print(checksum)