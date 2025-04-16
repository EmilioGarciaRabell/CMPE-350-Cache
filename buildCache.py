import calculateSize
import math

# Creates a cache with mapping policy determined by user input

#-------------------------------------------------------------------
# Prompt the user for cache size and words per block
#-------------------------------------------------------------------

# Prompt user to provide cache size in Bytes
def prompt_nominal():
    # prompt user to provide nominal size in Bytes
    nominal_size = int(input("Enter nominal size in Bytes: "))
    return nominal_size

def prompt_words_per_block():
    # prompt user to provide words per block
    words_per_block = int(input("Enter number of words per block: "))
    return words_per_block 

# Determine the type of mapping policy 0 for for Direct Mapped, 1 for Set Associative
def determine_mapping_policy():
    # prompt user to enter mapping policy
    mapping_policy = input("Enter mapping policy (DM or SA): ").strip().lower()

    if mapping_policy == "dm":
        return 0
    elif mapping_policy == "sa":
        return 1 
    else:
        print("Invalid mapping policy. Please enter 'DM' or 'FA'.")
        return None

def promt_number_ways():
    # prompt user to provide number of ways
    num_ways = int(input("Enter number of ways: "))
    return num_ways



#-------------------------------------------------------------------
# Create cache
#-------------------------------------------------------------------
def create_direct_mapped_cache(nominal_size, words_per_block, num_blocks):
    dm_cache = []
    for i in range(num_blocks):
        dm_cache.append(-1)

    return Cache(0, nominal_size, words_per_block, num_blocks, -1, -1, dm_cache)

def create_set_associative_cache(nominal_size, words_per_block, num_blocks, num_ways, num_sets):
    sa_cache = []
    for i in range(num_ways):
        sa_cache.append([])
        for i in range(num_sets):
            sa_cache[i].append(-1)
    return Cache(0, nominal_size, words_per_block, num_blocks, num_ways, num_sets, sa_cache)

def start():
    # Prompt user for cache size and words per block
    nominal_size = prompt_nominal()
    words_per_block = prompt_words_per_block()

    # Determine mapping policy type
    typeC = determine_mapping_policy()

    # Determine number of blocks or ways based on mapping policy
    if typeC == 0: # Direct Mapped
        num_blocks = calculateSize.numBlocks(nominal_size, words_per_block)
        num_ways = -1
        num_sets = -1
    else: # Set Associative
        num_ways = promt_number_ways()
        num_blocks = math.floor(calculateSize.numBlocks(nominal_size, words_per_block) / num_ways)
        num_sets = calculateSize.numSets(num_blocks, num_ways, typeC)

    # Create cache based on mapping policy
    return create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets)


def create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets):
    number_blocks = calculateSize.numBlocks(nominal_size, words_per_block)
  
    # if typeC == 0: # Direct Mapped
    if typeC == 0:
        return create_direct_mapped_cache(nominal_size, words_per_block, number_blocks)
    else: # Set Associative
        return create_set_associative_cache(nominal_size, words_per_block, number_blocks)

# Add blocks to cache, each block is a list
def input_block_in_cache(cache, block):
    # # if typeC == 0: # Direct Mapped
    # typeC = cache.cache_type
    # if typeC == 0:
    #     return
    # elif typeC == 1: # Set Associative
    #     return
    cache.input_block_in_cache(block)

class Cache:
    def __init__(self, cache_type, size, words_per_block, num_blocks, num_ways, num_sets, cache):
        self.cache_type = cache_type
        self.size = size
        self.words_per_block = words_per_block
        self.num_blocks = num_blocks
        self.num_ways = num_ways
        self.num_sets = num_sets
        self.cache = cache

    def input_block_in_cache(self, block):
        # TODO - Implement logic for adding blocks to cache based on mapping policy
        if self.cache_type == 0:
            print(f"Addded {block}", block)
        else:
            print(f"Addded {block}", block)

    def __str__(self):
        return f"Cache Type: {self.cache_type}, Size: {self.size}, Words per Block: {self.words_per_block}, Number of Blocks: {self.num_blocks}, Number of Ways: {self.num_ways}, Number of Sets: {self.num_sets}"