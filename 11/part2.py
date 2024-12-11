import math

inputFile = open("./11/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
stones = list(map(int, inputLines[0].split(" ")))

stoneMap = {}

def transformStone(stone, iteration):

    if iteration == 75:
        return 1

    if (stone, iteration) in stoneMap:
        return stoneMap[(stone, iteration)]

    if stone == 0:
        stones = transformStone(1, iteration + 1)
        stoneMap[(stone, iteration)] = stones
        return stones

    digits = len(str(stone))
    if digits % 2 == 0:
        left = math.floor(stone / (10 ** (digits/2)))
        right = math.floor(stone - (left * (10 ** (digits/2))))
        stones = transformStone(left, iteration + 1) + transformStone(right, iteration + 1)
        stoneMap[(stone, iteration)] = stones
        return stones

    stones = transformStone(stone * 2024, iteration + 1)
    stoneMap[(stone, iteration)] = stones
    return stones

sum = 0
for stone in stones:
    sum += transformStone(stone, 0)
    
print(sum)



        
