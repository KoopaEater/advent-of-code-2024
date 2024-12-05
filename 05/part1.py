inputFile = open("./05/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))

ruleLines = inputLines[:1176]
updateLines = inputLines[1177:]

bannedPageNumsDict = {}

for line in ruleLines:
    rule = line.split("|")
    if not rule[1] in bannedPageNumsDict:
        bannedPageNumsDict[rule[1]] = [rule[0]]
    else:
        bannedPageNumsDict[rule[1]].append(rule[0])

goodUpdates = []

for line in updateLines:
    update = line.split(",")
    bannedPageNums = []
    for pageNum in update:
        if pageNum in bannedPageNums:
            break
        if not pageNum in bannedPageNumsDict:
            continue
        bannedPageNums += bannedPageNumsDict[pageNum]
    else:
        goodUpdates.append(update)

sum = 0
for update in goodUpdates:
    middleIndex = int((len(update) - 1) / 2)
    middle = update[middleIndex]
    sum += int(middle)

print(sum)