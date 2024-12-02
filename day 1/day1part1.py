f = open("day1_input.txt", "r")

left_list = []
right_list = []

for line in f:
    split_line = line.split(" ")
    left_list.append(int(split_line[0]))
    right_list.append(int(split_line[3]))

total_distance = 0

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(total_distance)

f.close()