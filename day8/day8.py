def PartOneHelper(grid, i, j):
    if (i == 0 or i == len(grid)-1):
        return 1
    if (j == 0 or j == len(grid[0])-1):
        return 1

    height = grid[i][j]
    if (CheckColumn(grid, height, i, 0, j) 
        or CheckColumn(grid, height, i, j+1, len(grid[0]))
        or CheckRow(grid, height, j, 0, i) 
        or CheckRow(grid, height, j, i+1, len(grid))):
        return 1
    
    return 0

def CheckColumn(grid, height, row, start, end):
    for x in range(start, end):
        if grid[row][x] >= height:
            return False
    return True

def CheckRow(grid, height, j, start, end):
    for x in range(start, end):
        if grid[x][j] >= height:
            return False
    return True


def PartOne():
    file = open('input.txt', 'r')
    lines = file.readlines()
    grid = []
    value = 0

    for line in lines:
        grid.append([*line.strip()])
    
    for i in range(0, len(grid)):
        for j in range(0,len(grid[0])):
            value += PartOneHelper(grid, i, j)

    return value

def CheckColumnScore(grid, height, row, start, end, increment):
    count = 0
    for x in range(start, end, increment):
        count += 1
        if grid[row][x] >= height:
            return count
    return count

def CheckRowScore(grid, height, j, start, end, incremement):
    count = 0
    for x in range(start, end, incremement):
        count += 1
        if grid[x][j] >= height:
            return count
    return count

def PartTwoHelper(grid, i, j):
    if (i == 0 or i == len(grid)-1):
        return 0
    if (j == 0 or j == len(grid[0])-1):
        return 0
    height = grid[i][j]
    return CheckColumnScore(grid, height, i, j-1, -1, -1) \
        * CheckColumnScore(grid, height, i, j+1, len(grid[0]), 1) \
        * CheckRowScore(grid, height, j, i-1, -1, -1) \
        * CheckRowScore(grid, height, j, i+1, len(grid), 1)
    

def PartTwo():
    file = open('input.txt', 'r')
    lines = file.readlines()
    grid = []
    value = 0

    for line in lines:
        grid.append([*line.strip()])
    
    for i in range(0, len(grid)):
        for j in range(0,len(grid[0])):
            value = max(PartTwoHelper(grid, i, j), value)
    return value

#print(PartOne())
print(PartTwo())

