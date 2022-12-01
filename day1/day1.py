
def PartOne():
    file = open('input.txt', 'r')
    lines = file.readlines()

    maxValue = -1
    currentValue = 0
    for line in lines:
        line = line.strip()
        if (line == ""):
            maxValue = max(currentValue, maxValue)
            currentValue = 0
        else:
            currentValue += int(line)

    return maxValue

def PartTwo():
    file = open('input.txt', 'r')
    lines = file.readlines()

    calories = []

    currentValue = 0
    for line in lines:
        line = line.strip()
        if (line == ""):
            calories.append(currentValue)
            currentValue = 0
        else:
            currentValue += int(line)

    calories.sort(reverse=True)

    return calories[0] + calories[1] + calories[2]

print('Elf With Most Calories: ' + str(PartOne()))
print('Sum of Top 3 Elves With Most Calories: ' + str(PartTwo()))