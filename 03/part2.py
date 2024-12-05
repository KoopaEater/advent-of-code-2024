inputFile = open("./03/input.txt", "r")
inputLines = inputFile.readlines()
inputStr = "".join(inputLines)

def getResultFromIndex(i):
    if inputStr[i:i+4] != "mul(":
        return 0
    
    nextBracket = findNextBracket(i+5)
    if nextBracket == None:
        return 0
    
    calcList = inputStr[i+4:nextBracket]

    if len(calcList) < 3:
        return 0
    
    nums = calcList.split(",")

    if len(nums) != 2:
        return 0
    
    for num in nums:
        if len(num) > 3 or len(num) < 1:
            return 0

        if not set(num).issubset(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            return 0
    
    return int(nums[0]) * int(nums[1])
    

def findNextBracket(i):
    ii = i
    while (inputStr[ii] != ")"):
        ii += 1
        if ii - i > 7:
            return None
    return ii

def checkDo(i):
    if inputStr[i:i+4] == "do()":
        return True
    elif inputStr[i:i+7] == "don't()":
        return False
    else:
        return None
    
sum = 0
do = True
for i, sym in enumerate(inputStr):

    tempDo = checkDo(i)
    if tempDo != None:
        do = tempDo

    if do:
        sum += getResultFromIndex(i)

print(sum)