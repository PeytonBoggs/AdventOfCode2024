def calculate_plot(i, j):
    plots_seen.append((i, j))

    measurements = [1, 0]

    #Look up
    if i-1 < 0 or farm[i-1][j] != farm[i][j]:
        measurements[1] += 1
    elif ((i-1, j) not in plots_seen):
        temp_measurements = calculate_plot(i-1, j)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]

    #Look right
    if j+1 >= len(farm[i]) or farm[i][j+1] != farm[i][j]:
        measurements[1] += 1
    elif ((i, j+1) not in plots_seen):
        temp_measurements = calculate_plot(i, j+1)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]

    #Look down
    if i+1 >= len(farm) or farm[i+1][j] != farm[i][j]:
        measurements[1] += 1
    elif ((i+1, j) not in plots_seen):
        temp_measurements = calculate_plot(i+1, j)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]

    #Look left
    if j-1 < 0 or farm[i][j-1] != farm[i][j]:
        measurements[1] += 1
    elif ((i, j-1) not in plots_seen):
        temp_measurements = calculate_plot(i, j-1)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]
        
    return measurements
        
f = open("day12/day12_input.txt", "r")

farm = []

for line in f:
    line = line.strip()
    farm.append(line)

plots_seen = []
totalPrice = 0

i = 0
while i < len(farm):
    j = 0
    while j < len(farm[i]):
        if (i, j) not in plots_seen:
            measurements = calculate_plot(i, j)
            totalPrice += measurements[0] * measurements[1]
        j += 1
    i += 1

print(totalPrice)
