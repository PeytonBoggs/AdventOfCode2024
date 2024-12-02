f = open("day 2/day2_input.txt", "r")

safeCount = 0

for line in f:
    report = line.split(" ")

    print(report)

    increasing = True
    decreasing = True
    smallChange = True

    for i in range (0, len(report) - 1):
        current = int(report[i])
        next = int(report[i+1])

        if current > next:
            increasing = False
        if current < next:
            decreasing = False
        if ((abs(current - next) > 3) or (current == next)):
            smallChange = False

    if (smallChange and (increasing or decreasing)):
        safeCount += 1
        print("safe")

print(safeCount)


