inputFile = open("./09/input.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
diskMap = inputLines[0]

def diskMapToDiskSpace(diskMap):
    state = "FILE"
    id = 0
    diskSpace = []
    for symbol in diskMap:
        symToWrite = id if state == "FILE" else None
        for _ in range(int(symbol)):
            diskSpace.append(symToWrite)
        if state == "FREE":
            id += 1
            state = "FILE"
        else:
            state = "FREE"
    return diskSpace

def diskSpaceToCompressed(diskSpace):
    compressed = []
    i = 0
    j = len(diskSpace) - 1
    while i < j:
        id = diskSpace[i]
        i += 1
        if id != None:
            compressed.append(id)
        else:
            while diskSpace[j] == None:
                j -= 1
            compressed.append(diskSpace[j])
            j -= 1
    if i == j and diskSpace[i] != None:
        compressed.append(diskSpace[i])
        
    return compressed

def calcChecksum(compressed):
    checksum = 0
    for i, id in enumerate(compressed):
        checksum += i * id
    return checksum

def convertStrToDiskSpace(someStr):
    diskSpace = []
    for sym in someStr:
        if sym == ".":
            diskSpace.append(None)
        else:
            diskSpace.append(int(sym))
    return diskSpace

diskSpace = diskMapToDiskSpace(diskMap)
# diskSpace = convertStrToDiskSpace("0..111....22222")
# print(diskSpace)
compressed = diskSpaceToCompressed(diskSpace)
# print(compressed)
checksum = calcChecksum(compressed)
print(checksum)