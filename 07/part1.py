inputFile = open("./07/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))


def tryEq(testVal, nums):
    if len(nums) == 1:
        return testVal == nums[0]
    if tryEq(testVal - nums[-1], nums[:-1]):
        return True
    if (testVal % nums[-1] == 0) and tryEq(testVal / nums[-1], nums[:-1]):
        return True
    return False


sum = 0
for line in inputLines:
    split = line.split(": ")
    testValue = int(split[0])
    nums = list(map(int, split[1].split(" ")))
    
    if tryEq(testValue, nums):
        sum += testValue
    
print(sum)
    