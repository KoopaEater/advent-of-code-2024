import math

inputFile = open("./11/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
stones = list(map(int, inputLines[0].split(" ")))

def transformStones(listOfStones):
    newStones = []
    for stone in listOfStones:

        if stone == 0:
            newStones.append(1)
            continue

        digits = len(str(stone))
        if digits % 2 == 0:
            left = math.floor(stone / (10 ** (digits/2)))
            right = math.floor(stone - (left * (10 ** (digits/2))))
            newStones.append(left)
            newStones.append(right)
            continue

        newStones.append(stone * 2024)

    return newStones

for i in range(25):
    stones = transformStones(stones)

print(len(stones))

        
