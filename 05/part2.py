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

badUpdates = []

for line in updateLines:
    update = line.split(",")
    bannedPageNums = []
    for pageNum in update:
        if pageNum in bannedPageNums:
            badUpdates.append(update)
            break
        if not pageNum in bannedPageNumsDict:
            continue
        bannedPageNums += bannedPageNumsDict[pageNum]

def swapPageNums(update, i, j):
    tmp = update[i]
    update[i] = update[j]
    update[j] = tmp

correctedUpdates = []

for update in badUpdates:
    correct = False
    while not correct:
        swapDict = {}
        for j, pageNum in enumerate(update):
            if pageNum in swapDict:
                swapPageNums(update, swapDict[pageNum], j)
                break
            if pageNum in bannedPageNumsDict:
                for banned in bannedPageNumsDict[pageNum]:
                    swapDict[banned] = j
        else:
            correct = True
    correctedUpdates.append(update)


sum = 0
for update in correctedUpdates:
    middleIndex = int((len(update) - 1) / 2)
    middle = update[middleIndex]
    sum += int(middle)

print(sum)