inputFile = open("./07/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))

def getValWithout(val, without):
    assert str(val).endswith(str(without))
    valStr = str(val)
    withoutStr = str(without)
    valWithoutStr = valStr[:-len(withoutStr)]
    if len(valWithoutStr) == 0:
        return 0
    valWithout = int(valWithoutStr)
    return valWithout


def tryEq(testVal, nums):
    if len(nums) == 1:
        return testVal == nums[0]
    if tryEq(testVal - nums[-1], nums[:-1]):
        return True
    if (testVal % nums[-1] == 0) and tryEq(int(testVal / nums[-1]), nums[:-1]):
        return True
    if str(testVal).endswith(str(nums[-1])) and tryEq(getValWithout(testVal, nums[-1]), nums[:-1]):
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
    