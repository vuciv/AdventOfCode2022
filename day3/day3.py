def ConvertCharToPriorityValue(c):
    if (str.islower(c)):
        return ord(c) - 96
    else:
        return ord(c) - 38
    
def PartOneHelper(line):
    prioritySet = set()
    middleIndex = int(len(line)/2)
    
    # First Half, initialize
    for c in range(middleIndex):
        prioritySet.add(ConvertCharToPriorityValue(line[c]))

    # Second Half, check
    for c in range(middleIndex, len(line)):
        convertedChar = ConvertCharToPriorityValue(line[c])
        if convertedChar in prioritySet:
            return convertedChar

def PartOne():
    file = open('input.txt', 'r')
    lines = file.readlines()

    return sum([PartOneHelper(line.strip()) for line in lines])

def PartTwoHelper(line1, line2, line3):
    for c in line3:
        if c in line1 and c in line2:
            return ConvertCharToPriorityValue(c)

def PartTwo():
    file = open('input.txt', 'r')
    lines = file.readlines()
    value = 0

    for i in range(0, len(lines), 3):
        value += PartTwoHelper(
            lines[i].strip(), 
            lines[i+1].strip(), 
            lines[i+2].strip()
            )


    return value

print(PartOne())
print(PartTwo())

