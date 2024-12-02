f = open("day 1/day1_input.txt", "r")

left_list = []
right_list = []

for line in f:
    split_line = line.split(" ")
    left_list.append(int(split_line[0]))
    right_list.append(int(split_line[3]))

similarity_score = 0

for i in range(len(left_list)):
    for j in range(len(right_list)):
        if left_list[i] == right_list[j]:
            similarity_score += left_list[i]

print(similarity_score)

f.close()