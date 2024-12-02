def total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return distance

inputFile = open("input.txt", "r")

lines = inputFile.readlines()

right_list = []
left_list = []

for i in lines:
    rightAndLeft = i.split("   ")

    left_list.append(int(rightAndLeft[0]))
    right_list.append(int(rightAndLeft[1]))

result = total_distance(left_list, right_list)
print(result)
