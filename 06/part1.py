inputFile = open("./06/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
lines = len(inputLines)
lineLength = len(inputLines[0])

def searchStartPos():
    for y, line in enumerate(inputLines):
        for x, symbol in enumerate(line):
            if inputLines[y][x] == "^":
                return (x, y)
    return (None, None)

def inField(x, y):
    if x < 0 or x >= lineLength:
        return False
    if y < 0 or y >= lines:
        return False
    return True

def getTurnedDir(xDir, yDir):
    return (-yDir, xDir)

xDir, yDir = (0, -1)
x, y = searchStartPos()
positions = set()

while inField(x, y):
    positions.add((x, y))
    xNext = x + xDir
    yNext = y + yDir
    if inputLines[yNext][xNext] == "#":
        xDir, yDir = getTurnedDir(xDir, yDir)
    x += xDir
    y += yDir

print(len(positions))


inputFile.close()