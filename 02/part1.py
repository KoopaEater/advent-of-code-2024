inputFile = open("./02/input.txt", "r")
inputLines = inputFile.readlines()
inputs = len(inputLines)


def checkCriteria(levels):

    if len(levels) <= 1:
        return True

    last = int(levels[0])
    lastDiff = 0

    for level in levels[1:]:
        level = int(level)

        diff = level - last

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if level < last and lastDiff > 0:
            return False
        
        if level > last and lastDiff < 0:
            return False
        
        lastDiff = diff
        last = level
    
    return True



safeCount = 0

for line in inputLines:
    levels = line.split()

    if not checkCriteria(levels):
        continue

    safeCount += 1


print(safeCount)
