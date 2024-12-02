def is_safe_report(levels):
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count

def is_safe_with_dampener(levels):
    if is_safe_report(levels):
        return True
    
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe_report(new_levels):
            return True
    return False

def count_safe_reports_with_dampener(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

inputFile = open("input.txt", "r")
lines = inputFile.readlines()

levels = []

for i in lines:
    seperated = i.split(" ")
    level = []
    for j in seperated:
        level.append(int(j))

    levels.append(level)

result = count_safe_reports(levels)
print("Number of safe reports:", result)
result = count_safe_reports_with_dampener(levels)
print("Number of safe reports with Problem Dampener:", result)
