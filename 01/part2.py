

inputFile = open("./01/input.txt", "r")
inputLines = inputFile.readlines()
inputs = len(inputLines)

l1 = []
l2 = []

for line in inputLines:
    numLeft = int(line[0:5])
    numRight = int(line[8:13])

    l1.append(numLeft)
    l2.append(numRight)

l2Counts = {}

for num in l2:
    if l2Counts.get(num) == None:
        l2Counts[num] = 1
    else:
        l2Counts[num] += 1

simScore = 0

for num in l1:
    count = l2Counts.get(num, 0)
    simScore += num * count

print(simScore)
