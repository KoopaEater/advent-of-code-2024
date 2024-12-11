inputFile = open("./10/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
lines = len(inputLines)
lineLength = len(inputLines[0])

topoMap = list(map(lambda line: list(map(int,line)), inputLines))

dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def isOnMap(x, y):
    if x < 0 or x >= lineLength:
        return False
    if y < 0 or y >= lines:
        return False
    return True

def findTrails(x, y, searchHeight, listOfEnds):
    if topoMap[y][x] != searchHeight:
        return
    if searchHeight == 9:
        listOfEnds.append((x, y))
        return
    for xDir, yDir in dirs:
        xNew = x + xDir
        yNew = y + yDir
        if isOnMap(xNew, yNew):
            findTrails(xNew, yNew, searchHeight + 1, listOfEnds)

sum = 0
for y, line in enumerate(topoMap):
    for x, height in enumerate(line):
        endList = []
        findTrails(x, y, 0, endList)
        sum += len(endList)

print(sum)