def is_safe(report):
    increasing = report[1] > report[0]
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) > 3 or diff == 0 or (increasing and diff < 0) or (not increasing and diff > 0):
            return False
    return True


def can_be_safe(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False


# Read input reports
reports = []
with open("input.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.split())))

num_safe = 0

# Check each report
for report in reports:
    if is_safe(report) or can_be_safe(report):
        num_safe += 1

print(num_safe)
