inputFile = open("./04/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
lines = len(inputLines)
lineLength = len(inputLines[0])

dirs = [
    (-1,-1),
    (-1,1),
    (1,-1),
    (1,1)
]


def checkAll(x, y):

    if inputLines[y][x] != "A":
        return 0

    if x < 1 or x > lineLength - 2:
        return 0
    if y < 1 or y > lines - 2:
        return 0
    
    masCount = 0
    for xDir, yDir in dirs:

        if inputLines[y + yDir][x + xDir] != "M":
            continue
        if inputLines[y - yDir][x - xDir] != "S":
            continue

        masCount += 1

    if masCount != 2:
        return 0

    return 1

sum = 0
for y in range(lines):
    for x in range(lineLength):
        sum += checkAll(x, y)

print(sum)
