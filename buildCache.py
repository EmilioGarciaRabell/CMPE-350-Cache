#--------------------------------------------------------------------
# buildCache.py
# Module creates a cache with mapping policy determined by user input
#--------------------------------------------------------------------


import calculateSize
import promptUser as prompt
import math


#-------------------------------------------------------------------
# Create cache
#-------------------------------------------------------------------

def start():
    # Prompt user for cache size and words per block
    nominal_size = prompt.get_nominal()
    words_per_block = prompt.get_words_per_block()

    # Determine mapping policy type
    typeC = prompt.get_mapping_policy()

    # Determine number of blocks or ways based on mapping policy
    num_blocks = calculateSize.numBlocks(nominal_size, words_per_block)
    if typeC == 0: # Direct Mapped
        
        num_ways = -1
        num_sets = -1
    else: # Set Associative
        num_ways = prompt.get_number_ways()
        num_blocks = math.floor(num_blocks / num_ways)
        num_sets = calculateSize.numSets(num_blocks, num_ways, typeC)

    # Create cache based on mapping policy
    return create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets)


def create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets):  
    cache = Cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets, None)
    cache.create_cache
    return cache


class Cache:
    def __init__(self, cache_type, size, words_per_block, num_blocks, num_ways, num_sets, cache,hits=0,misses=0):
        self.cache_type = cache_type
        self.size = size
        self.words_per_block = words_per_block
        self.num_blocks = num_blocks
        self.num_ways = num_ways
        self.num_sets = num_sets
        self.cache = cache
        self.hits = hits
        self.misses = misses

    def input_block_in_cache(self, block):
        # TODO - Implement logic for adding blocks to cache based on mapping policy
        if self.cache_type == 0:
            # check if the index is empty
            # check if the block is already in the cache - hit
            if self.cache[block] == -1:
                # if empty, add block to cache
                self.cache[block] = block
                print(f"Addded {block}", block)
                self.misses += 1
            else:
                # if not empty, check if the block is already in the cache - hit

                if self.cache[block] == block:
                    print(f"Hit {block}", block)
                    self.hits += 1
                else:
                    # if not, replace the block in the cache
                    self.cache[block] = block
                    print(f"Replaced {block}", block)
                    self.misses += 1
        else:
            print(f"Addded {block}", block)
    
    def create_cache(self):
        self.cache = []
        if (self.cache_type == 0): # Direct Mapped
            for i in range(self.num_blocks):
                self.cache.append(-1)
            self.num_ways = -1
            self.num_sets = -1
            
        else: # Set Associative
            for i in range(self.num_ways):
                self.cache.append([])
                for i in range(self.num_sets):
                    self.cache[i].append(-1)

    def clear_cache(self):
        self.create_cache()

    def __str__(self):
        return f"Cache Type: {self.cache_type}, Size: {self.size}, Words per Block: {self.words_per_block}, Number of Blocks: {self.num_blocks}, Number of Ways: {self.num_ways}, Number of Sets: {self.num_sets}"