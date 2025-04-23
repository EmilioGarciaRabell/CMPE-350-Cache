#--------------------------------------------------------------------
# buildCache.py
# Module creates a cache with mapping policy determined by user input
#--------------------------------------------------------------------

import calculateSize
import promptUser as prompt
import math
from collections import OrderedDict
#-------------------------------------------------------------------
# Create cache
#-------------------------------------------------------------------

## prompts user for cache size, words per block, and mapping policy.
def start():
    # Prompt user for cache size and words per block
    nominal_size = prompt.get_nominal()
    words_per_block = prompt.get_words_per_block()

    # Determine mapping policy type
    typeC = prompt.get_mapping_policy()

    # Determine number of blocks or ways based on mapping policy
    num_blocks = calculateSize.numBlocks(nominal_size, words_per_block)
    
    # keep -1 is direct mapped, otherwise set to -1
    num_ways = -1
    num_sets = -1

    if typeC: # Set Associative
        num_ways = prompt.get_number_ways()
        num_sets = calculateSize.numSets(num_blocks, num_ways, typeC)

    # Create cache based on mapping policy and user input
    cache = Cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets, None, None)
    cache.create_cache()
    return cache


## creates a cache object 
class Cache:
    def __init__(self, cache_type, size, words_per_block, num_blocks, num_ways, num_sets, cache,replacement_policy,hits=0,misses=0, ):
        self.cache_type = cache_type
        self.size = size
        self.words_per_block = words_per_block
        self.num_blocks = num_blocks
        self.num_ways = num_ways
        self.num_sets = num_sets
        self.cache = cache
        self.hits = hits
        self.misses = misses
        self.replacement_policy = replacement_policy
   
    # checks if the block is in the cache
    def input_block_in_cache(self, block):
        index = math.floor(block / self.words_per_block)
                
        if self.cache_type == 0: # Direct Mapped 
            # No choise in replacement
            # check if the index is empty
            # check if the block is already in the cache - hit
            if self.cache[index % self.num_blocks] == -1:
                # if empty, add block to cache
                self.cache[index % self.num_blocks] = index
                print(f"Added block {index}")
                self.misses += 1
            else:
                # if not empty, check if the block is already in the cache - hit
                if self.cache[index % self.num_blocks] == index:
                    print(f"Hit block {index}")
                    self.hits += 1
                else:
                    # if not, replace the block in the cache
                    self.cache[index % self.num_blocks] = index
                    print(f"Replaced with block {index}")
                    self.misses += 1
        else: # Set associative case

            # Calculate the set index
            set_index = index % self.num_sets
            # Calculate the block index within the set
            current_set = self.cache[set_index]
            # Get the replacement policy for this set
            lru_dict = self.replacement_policy[set_index]
            

            # Check for hit first
            for i in range(self.num_ways):
                if current_set[i] == index:
                    # Update LRU - move this block to end (most recently used)
                    lru_dict.move_to_end(index)
                    print(f"Hit block {index}, Position: {i}")
                    self.hits += 1
                    return 1
            
                # If we get here, it's a miss
                # Check for empty space
                elif current_set[i] == -1:
                    current_set[i] = index
                    lru_dict[index] = i  # Add to LRU tracking
                    print(f"Added block {index}, Position: {i}")
                    self.misses += 1
                    return 1
            
            # If no empty space, replace LRU block
            if lru_dict:
                # Get the least recently used block (first item in OrderedDict)
                lru_block, lru_pos = next(iter(lru_dict.items()))  
                current_set[lru_pos] = index
                # Remove old block and add new one
                lru_dict.pop(lru_block)
                lru_dict[index] = lru_pos
                print(f"Replaced with block {index}, Position: {lru_pos} (replaced LRU block {lru_block})")
            else:
                # Fallback if LRU dict is empty (shouldn't happen)
                current_set[0] = index
                lru_dict[index] = 0
                print(f"Replaced with block {index}, Position: 0 (LRU dict was empty)")
            self.misses += 1
        
        return 1

    
    ## creates the cache, hits and misses set to 0
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
            # Initialize replacement policy for set associative cache
            self.replacement_policy = [OrderedDict() for _ in range(self.num_sets)]

    ## clears the cache by creating a new empty cache
    def clear_cache(self):
        self.create_cache()

    ## returns the word in the block
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

    ## returns the string representation of cache attributes
    def __str__(self):
        addressType = calculateSize.addressType(self.words_per_block, self.num_blocks, self.num_sets, self.cache_type)
        tagSize = addressType[0]
        indexSize = addressType[1]
        offsetSize = addressType[2]
        realSize = calculateSize.realSize(self.size, self.num_blocks, tagSize, 1) # status size is 1 byte
        print("Cache Details:")
        if self.cache_type == 0: # Direct Mapped
            return (f"\tCache Type : Direct Mapped \n\tNumber of Blocks: {self.num_blocks} \n\tTag Size: {tagSize} \n\tIndex Size: {indexSize} \n\tOffset Size: {offsetSize} \n\tReal Size: {realSize} bytes")
        else: # Set Associative 
            return (f"\tCache Type : Set Associative \n\tNumber of Blocks: {self.num_blocks} \n\tNumber of Sets: {self.num_sets} \n\tTag Size: {tagSize} \n\tIndex Size: {indexSize} \n\tOffset Size: {offsetSize} \n\tReal Size: {realSize} bytes")
    
    ## prints the cache contents
    def print_cache(self):
        print("Cache Contents:")
        string = ""
        if self.cache_type == 0: # Direct Mapped
            for i in range(self.num_blocks):
                string = self.get_word_in_block(self.cache[i])
                print(f"\tBlock {i}: {string}")
        else: # Set associative
            # Calculate column widths for nice alignment
            max_block_len = len(f"Block {self.num_sets - 1}")
            max_way_len = max(len(f"Way {i}") for i in range(self.num_ways))
            
            # Print header
            header = f"\t{'Set':<{max_block_len}} | " + " | ".join(f"{f'Way {i}':^{max_way_len}}" for i in range(self.num_ways))
            print(header)
            print("\t" + "-" * (len(header) - 1))  # -1 to account for the tab
            
            # Print each set
            for i in range(self.num_sets):
                ways = []
                for j in range(self.num_ways):
                    block_content = self.get_word_in_block(self.cache[i][j])
                    # Clean up the block content formatting
                    if block_content == "":
                        ways.append(" " * (max_way_len - 3) + "---")
                    else:
                        # Shorten the block representation if needed
                        if len(block_content) > 20:
                            block_number = block_content.split('(')[0]
                            word_range = block_content.split('(')[1].split(')')[0]
                            first_word, last_word = word_range.split(', ')[0], word_range.split(', ')[-1]
                            short_content = f"{block_number}({first_word}-{last_word})"
                            ways.append(f"{short_content:<{max_way_len}}")
                   
                        else:
                            ways.append(f"{block_content:<{max_way_len}}")
                
                # Print set row
                print(f"\t{i:<{max_block_len}} | " + " | ".join(ways))
