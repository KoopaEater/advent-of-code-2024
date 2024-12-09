inputFile = open("./09/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
diskMap = inputLines[0]

def diskMapToDiskSpace(diskMap):
    state = "FILE"
    id = 0
    diskSpace = ""
    for symbol in diskMap:
        symToWrite = "#" + str(id) if state == "FILE" else "."
        for _ in range(int(symbol)):
            diskSpace += symToWrite
        if state == "FREE":
            id += 1
            state = "FILE"
        else:
            state = "FREE"
    return diskSpace
    
def findPrevNum(someList, j):
    num = []
    while j >= 0 and someList[j] != "#":
        if someList[j] != ".":
            num.insert(0, someList[j])
        j -= 1
    return j-1, ["#"] + num

def findNextNum(someList, i):
    num = []
    while i < len(someList) and someList[i] != "#":
        if someList[i] != ".":
            num.append(someList[i])
        i += 1
    return i+1, int("".join(num))

def diskSpaceToCompressed(diskSpace: str):
    compressed = []
    i = 0
    j = len(diskSpace) - 1
    diskSpaceAsList = list(diskSpace)
    while i <= j:
        sym = diskSpaceAsList[i]
        i += 1
        if sym != ".":
            compressed.append(sym)
        else:
            j, numToBeMoved = findPrevNum(diskSpaceAsList, j)
            compressed += numToBeMoved
    return "".join(compressed)

def calcChecksum(compressed: str):
    checksum = 0
    i = 1
    index = 0
    compressedAsList = list(compressed)
    while i < len(compressedAsList):
        i, num = findNextNum(compressedAsList, i)
        checksum += index * num
        # print(index, "*", num, "=", index*num, "total=", checksum)
        index += 1
    return checksum
        

diskSpace = diskMapToDiskSpace(diskMap)
print(diskSpace)
compressed = diskSpaceToCompressed(diskSpace)
print(compressed)
checksum = calcChecksum(compressed)
print(checksum)