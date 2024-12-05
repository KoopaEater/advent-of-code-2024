inputFile = open("./04/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
lines = len(inputLines)
lineLength = len(inputLines[0])

dirs = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

symbols = [
    'X', 'M', 'A', 'S'
]

symbolCount = len(symbols)


def checkAll(x, y):
    count = 0

    for xDir, yDir in dirs:
        outerX = x + (xDir*(symbolCount-1))
        outerY = y + (yDir*(symbolCount-1))
        if outerX < 0 or outerX >= lineLength:
            continue
        if outerY < 0 or outerY >= lines:
            continue
        
        for i, symbol in enumerate(symbols):
            checkX = x + (xDir * i)
            checkY = y + (yDir * i)

            if inputLines[checkX][checkY] != symbol:
                break
        else:
            count += 1

    return count

sum = 0
for y in range(lines):
    for x in range(lineLength):
        sum += checkAll(x, y)

print(sum)
