reports = []

with open("input.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.split())))

numSafe = 0

for report in reports:
    increasing = report[1] > report[0]

    isSafe = True
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) > 3 or diff == 0:
            isSafe = False
            break

        if (increasing and diff < 0) or (not increasing and diff > 0):
            isSafe = False
    if isSafe:
        numSafe += 1


print(numSafe)
