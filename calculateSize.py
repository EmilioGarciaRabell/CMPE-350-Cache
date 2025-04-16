import math

# Returns integer
def numBlocks(cacheSize, wordsPerBlock):
    return cacheSize / (wordsPerBlock * 4.0)

# typeC = 0 for Direct mapped and 1 for N-way
# Returns integer, -1 if Direct Mapped
def numSets(numBlocks, N, typeC):
    if typeC:
        return numBlocks / N
    return -1    

# typeC = 0 for Direct mapped and 1 for N-way
# Returns tuple [size(tag), size(index), size(offset)]
def addressType(wordsPerBlock, numBlocks, typeC):
    indexSize = math.log2(numBlocks)
    offsetSize = wordsPerBlock * 4
    tagSize = 32 - indexSize - offsetSize

    return [tagSize, indexSize, offsetSize]

# Returns double
def realSize(cacheSize, numBlocks, tagSize, statusSize):
    return cacheSize + numBlocks * (tagSize + statusSize) / 8