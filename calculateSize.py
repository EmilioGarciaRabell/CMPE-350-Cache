import math

# Returns integer
def numBlocks(cacheSize, wordsPerBlock):
    return math.floor(cacheSize / (wordsPerBlock * 4.0))

# typeC = 0 for Direct mapped and 1 for N-way
# Returns integer, -1 if Direct Mapped
def numSets(numBlocks, N, typeC):
    if typeC:
        return math.floor(numBlocks / N)
    return -1    

# numBlocks has to be numSets for the Set associative case
# typeC = 0 for Direct mapped and 1 for N-way
# Returns tuple [size(tag), size(index), size(offset)]
def addressType(wordsPerBlock, numBlocks):
    indexSize = math.log2(numBlocks)
    offsetSize = wordsPerBlock * 4
    tagSize = 32 - indexSize - offsetSize

    return [tagSize, indexSize, offsetSize]

# Returns double
def realSize(cacheSize, numBlocks, tagSize, statusSize):
    return math.floor(cacheSize + numBlocks * (tagSize + statusSize) / 8)


## calculates the hit rate based off hits and num_word_addr (total accesses)
## returns a float value (percentage)
def calculate_hit_rate (hits, num_word_addr):
    if num_word_addr == 0:
        return 0
    return (hits / num_word_addr) * 100

## calculates the miss rate based off misses and num_word_addr (total accesses)
## returns a float value (percentage)
def calculate_miss_rate (misses, num_word_addr):
    if num_word_addr == 0:
        return 0
    return (misses / num_word_addr) * 100