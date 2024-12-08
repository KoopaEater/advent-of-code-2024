inputFile = open("./08/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
lines = len(inputLines)
lineLength = len(inputLines[0])

locMap = {}

for y, line in enumerate(inputLines):
    for x, symbol in enumerate(line):
        if symbol == ".":
            continue
        if not symbol in locMap:
            locMap[symbol] = [(x, y)]
        else:
            locMap[symbol].append((x,y))     
            
antinodes = set()

def checkInBounds(x, y):
    if x < 0 or x >= lineLength:
        return False
    if y < 0 or y >= lines:
        return False
    return True  
            
def addAntisFromPair(aLoc, bLoc):
    ax, ay = aLoc
    bx, by = bLoc
    xDist = bx - ax
    yDist = by - ay
    
    while checkInBounds(ax, ay):
        antinodes.add((ax,ay))
        ax, ay = (ax - xDist, ay - yDist)
        
    while checkInBounds(bx, by):
        antinodes.add((bx, by))
        bx, by = (bx + xDist, by + yDist)   

for freq, locs in locMap.items():
    for i in range(len(locs)):
        iLoc = locs[i]
        for j in range(i+1, len(locs)):
            jLoc = locs[j]
            addAntisFromPair(iLoc, jLoc)
            
print(len(antinodes))