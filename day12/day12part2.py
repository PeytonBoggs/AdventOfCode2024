def calculate_plot(i, j):
    plots_seen.append((i, j))

    measurements = [1, 0]

    perimeter_up = False
    perimeter_down = False
    perimeter_left = False
    perimeter_right = False

    #Look up
    if i-1 < 0 or farm[i-1][j] != farm[i][j]:
        perimeter_up = True
    elif ((i-1, j) not in plots_seen):
        temp_measurements = calculate_plot(i-1, j)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]

    #Look right
    if j+1 >= len(farm[i]) or farm[i][j+1] != farm[i][j]:
        perimeter_right = True
    elif ((i, j+1) not in plots_seen):
        temp_measurements = calculate_plot(i, j+1)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]

    #Look down
    if i+1 >= len(farm) or farm[i+1][j] != farm[i][j]:
        perimeter_down = True
    elif ((i+1, j) not in plots_seen):
        temp_measurements = calculate_plot(i+1, j)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]

    #Look left
    if j-1 < 0 or farm[i][j-1] != farm[i][j]:
        perimeter_left = True
    elif ((i, j-1) not in plots_seen):
        temp_measurements = calculate_plot(i, j-1)
        measurements[0] += temp_measurements[0]
        measurements[1] += temp_measurements[1]

    #Check for concave corners
    #Top-right
    if i-1 >= 0 and j+1 < len(farm[i]) and farm[i-1][j] == farm[i][j+1] == farm[i][j] != farm[i-1][j+1]:
        measurements[1] += 1
    #Bottom-right
    if i+1 < len(farm) and j+1 < len(farm[i]) and farm[i+1][j] == farm[i][j+1] == farm[i][j] != farm[i+1][j+1]:
        measurements[1] += 1
    #Top-left
    if i-1 >= 0 and j-1 >= 0 and farm[i-1][j] == farm[i][j-1] == farm[i][j] != farm[i-1][j-1]:
        measurements[1] += 1
    #Bottom-right
    if i+1 < len(farm) and j-1 >= 0 and farm[i+1][j] == farm[i][j-1] == farm[i][j] != farm[i+1][j-1]:
        measurements[1] += 1

    #Check for convex corners
    #Top-right
    if perimeter_up and perimeter_right: measurements[1] += 1
    #Bottom-right
    if perimeter_down and perimeter_right: measurements[1] += 1
    #Top-left
    if perimeter_up and perimeter_left: measurements[1] += 1
    #Bottom-left
    if perimeter_down and perimeter_left: measurements[1] += 1

        
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