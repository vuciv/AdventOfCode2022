def PartOne():
    dictionary = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    file = open('input.txt', 'r')
    lines = file.readlines()

    value = 0
    for line in lines:
        line = line.strip()
        value += dictionary[line]

    return value

def PartTwo():
    dictionary = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    file = open('input.txt', 'r')
    lines = file.readlines()

    value = 0
    for line in lines:
        line = line.strip()
        value += dictionary[line]

    return value

print(PartOne())
print(PartTwo())