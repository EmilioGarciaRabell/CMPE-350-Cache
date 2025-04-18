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
    return round(((hits / num_word_addr) * 100),2)

## calculates the miss rate based off misses and num_word_addr (total accesses)
## returns a float value (percentage)
def calculate_miss_rate (misses, num_word_addr):
    if num_word_addr == 0:
        return 0
    return round(((misses / num_word_addr) * 100), 2)

## calculates the hit and miss rate based off hits and misses
## prints the hit and miss rate
def calculate_hit_miss_rate(cache):
    total_accesses = cache.hits + cache.misses
    # calculate hit and miss rate
    hit_rate = calculate_hit_rate(cache.hits, total_accesses)
    miss_rate = calculate_miss_rate(cache.misses, total_accesses)
    # print hit and miss rate
    print(f"Final Hit Rate: {hit_rate}%")
    print(f"Final Miss Rate: {miss_rate}%")
