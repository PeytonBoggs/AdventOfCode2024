f = open("day 2/day2_input.txt", "r")

safeCount = 0

for line in f:
    report = line.split(" ")

    print(report)

    dampenedReportSafe = False

    for i in range (0, len(report)):
        reportWithoutLevel = report.copy()
        del reportWithoutLevel[i]

        print(reportWithoutLevel)

        increasing = True
        decreasing = True
        smallChange = True

        for j in range (0, len(reportWithoutLevel) - 1):

            current = int(reportWithoutLevel[j])
            next = int(reportWithoutLevel[j+1])

            if current > next:
                increasing = False
            if current < next:
                decreasing = False
            if ((abs(current - next) > 3) or (current == next)):
                smallChange = False

        if (smallChange and (increasing or decreasing)):
            dampenedReportSafe = True
            print("Dampened report safe")

    if (dampenedReportSafe):
        safeCount += 1

print(safeCount)


