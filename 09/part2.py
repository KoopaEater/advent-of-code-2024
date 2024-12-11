inputFile = open("./09/sampleInput.txt", "r")
inputLines = list(map(lambda line: line.rstrip("\n"), inputFile.readlines()))
diskMap = inputLines[0]

def diskMapToDiskSpace(diskMap):
    diskSpace = []
    for i, sym in enumerate(diskMap):
        if i % 2 == 0:
            diskSpace.append({
                "type": "FILE",
                "id": int(i/2),
                "blocks": int(sym)
            })
        else:
            diskSpace.append({
                "type": "FREE",
                "blocks": int(sym)
            })
    return diskSpace

def diskSpaceToCompressed(diskSpace):
    pass

def calcChecksum(compressed):
    pass

diskSpace = diskMapToDiskSpace(diskMap)
print(diskSpace)
# compressed = diskSpaceToCompressed(diskSpace)
# print(compressed)
# checksum = calcChecksum(compressed)
# print(checksum)