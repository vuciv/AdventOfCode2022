def SplitPairIntoInts(pair):
    pairSplit = pair.split('-')
    return [int(pairSplit[0]), int(pairSplit[1])]

def OverlapsFully(pairs):
    pair1 = SplitPairIntoInts(pairs[0])
    pair2 = SplitPairIntoInts(pairs[1])
    if (pair2[0] >= pair1[0] and pair2[1] <= pair1[1]):
        return True
    elif (pair1[0] >= pair2[0] and pair1[1] <= pair2[1]):
        return True
    else:
        return False

def PartOne():
    file = open('input.txt', 'r')
    lines = file.readlines()

    return sum([1 for line in lines if OverlapsFully(line.strip().split(','))])

def OverlapsPartially(pairs):
    pair1 = SplitPairIntoInts(pairs[0])
    pair2 = SplitPairIntoInts(pairs[1])

    if (pair1[0] <= pair2[0] <= pair1[1]
    or pair1[0] <= pair2[1] <= pair1[1]):
        return True
    elif (pair2[0] <= pair1[0] <= pair2[1]
    or pair2[0] <= pair1[1] <= pair2[1]):
        return True
    else:
        return False

def PartTwo():
    file = open('input.txt', 'r')
    lines = file.readlines()

    return sum([1 for line in lines if OverlapsPartially(line.strip().split(',')) ])

print(PartOne())
print(PartTwo())