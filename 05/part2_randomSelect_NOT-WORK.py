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

shouldComeBefore = {}
for line in ruleLines:
    rule = line.split("|")
    if not rule[0] in shouldComeBefore:
        shouldComeBefore[rule[0]] = [rule[1]]
    else:
        shouldComeBefore[rule[0]].append(rule[1])

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


def swapPageNum(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if x in shouldComeBefore.get(A[j], []):
            i += 1
            swapPageNum(A, i, j)
    swapPageNum(A, i+1, r)
    return i + 1

import random
def randomizedPartition(A, p, r):
    i = random.randint(p, r)
    swapPageNum(A, r, i)
    return partition(A, p, r)

def randomizedSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = randomizedPartition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomizedSelect(A, p, q-1, i)
    else:
        return randomizedSelect(A, q + 1, r, i-k)

sum = 0
for update in badUpdates:
    middleIndex = int((len(update) - 1) / 2)
    middle = randomizedSelect(update, 0, len(update)-1, middleIndex)
    sum += int(middle)

print(sum)