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
        # num_blocks = math.floor(num_blocks / num_ways)
        num_sets = calculateSize.numSets(num_blocks, num_ways, typeC)

    # Create cache based on mapping policy
    return create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets)


def create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets):  
    cache = Cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets, None)
    cache.create_cache()
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

        index = math.floor(block / self.words_per_block)
                
        if self.cache_type == 0:
            # check if the index is empty
            # check if the block is already in the cache - hit
            if self.cache[index % self.num_blocks] == -1:
                # if empty, add block to cache
                self.cache[index % self.num_blocks] = index
                print(f"Added {index}")
                self.misses += 1
            else:
                # if not empty, check if the block is already in the cache - hit
                if self.cache[index % self.num_blocks] == index:
                    print(f"Hit {index}")
                    self.hits += 1
                else:
                    # if not, replace the block in the cache
                    self.cache[index % self.num_blocks] = index
                    print(f"Replaced {index}")
                    self.misses += 1
        else:

            # Set associative case

            # Loop through each way in the set
            for i in range(self.num_ways):

                # Check if there are any hits first, if not check for empty spaces
                if self.cache[index % self.num_sets][i] == index:
                    # Print if hit
                    print(f"Hit {index}, Position: {i}")
                    self.hits += 1
                    return 1
                elif self.cache[index % self.num_sets][i] == -1:
                    # if empty, add block to cache
                    self.cache[index % self.num_sets][i] = index
                    print(f"Added {index}, Position: {i}")
                    self.misses += 1
                    return 1
            
            # After checking for hits or empty spaces, replace the first position in the set
            # TODO: Change replacement policy
            self.cache[index % self.num_sets][0] = index
            print(f"Replaced {index}, Position: 0")
            self.misses += 1
        return 1
    
    def create_cache(self):
        self.hits = 0
        self.misses = 0
        self.cache = []
        if (self.cache_type == 0): # Direct Mapped
            for i in range(self.num_blocks):
                self.cache.append(-1)
            self.num_ways = -1
            self.num_sets = -1
            
        else: # Set Associative
            for i in range(self.num_sets ):
                self.cache.append([])
                for j in range(self.num_ways):
                    self.cache[i].append(-1)
        print(self)

    def clear_cache(self):
        self.create_cache()

    def get_word_in_block(self, block):

        # If the block is empty, don't return anything
        if block == -1:
            return ""

        wordOffset = block * self.words_per_block
        string = "b" + str(block) + "("
        
        for i in range(self.words_per_block):
            string += "w" + str(wordOffset + i) + ", "

        string = string[:-2] + ")"
        return string

    def __str__(self):
        return f"Cache Type: {self.cache_type}, Size: {self.size}, Words per Block: {self.words_per_block}, Number of Blocks: {self.num_blocks}, Number of Ways: {self.num_ways}, Number of Sets: {self.num_sets}"
    
    def print_cache(self):
        print("Cache:")
        string = ""
        if self.cache_type == 0: # Direct Mapped
            for i in range(self.num_blocks):
                string = self.get_word_in_block(self.cache[i])
                print(f"Block {i}: {string}")
        else: # Set associative
            for i in range(self.num_sets):
                string = ""
                for j in range(self.num_ways):
                    string += (self.get_word_in_block(self.cache[i][j]) + "\t")
                print(f"Block {i}: {string}")
