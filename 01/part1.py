

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

l1.sort()
l2.sort()

sum = 0

for i in range(inputs):
    diff = abs(l1[i] - l2[i])
    sum += diff

print(sum)
