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

def fillDirs():
    return [[[] for _ in range(lines)] for _ in range(lineLength)]


def checkLoopWithExtraObstacle(startDir, startPos, extraObstacle):
    xDir, yDir = startDir
    x, y = startPos
    dirs = fillDirs()

    while inField(x, y):
        if (xDir, yDir) in dirs[y][x]:
            return 1
        dirs[y][x].append((xDir, yDir))
        xNext = x + xDir
        yNext = y + yDir
        if inField(xNext, yNext) and (inputLines[yNext][xNext] == "#" or (xNext, yNext) == extraObstacle):
            xDir, yDir = getTurnedDir(xDir, yDir)
        x += xDir
        y += yDir
    
    return 0

def countLoops(startDir, startPos):

    loops = 0

    for y in range(lines):
        for x in range(lineLength):
            if inputLines[y][x] == "#":
                continue
            if (x, y) == startPos:
                continue
            loops += checkLoopWithExtraObstacle(startDir, startPos, (x, y))
            
    return loops

print(countLoops((0,-1), searchStartPos()))


inputFile.close()