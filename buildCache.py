import calculateSize

# Creates a cache with mapping policy determined by user input

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
def determine_mapping_policy(typeC):
    # prompt user to enter mapping policy
    mapping_policy = input("Enter mapping policy (DM or SA): ").strip().lower()

    if mapping_policy == "dm":
        return 0
    elif mapping_policy == "fa":
        return 1 
    else:
        print("Invalid mapping policy. Please enter 'DM' or 'FA'.")
        return None

def prompt_number_blocks():
    # prompt user to provide number of blocks
    num_blocks = int(input("Enter number of blocks: "))
    return num_blocks

def promt_number_ways():
    # prompt user to provide number of ways
    num_ways = int(input("Enter number of ways: "))
    return num_ways

def create_direct_mapped_cache(nominal_size, words_per_block, num_blocks):
    dm_cache = []
    for i in range(num_blocks):
        dm_cache.append(-1)
    return dm_cache

def create_set_associative_cache(nominal_size, words_per_block, num_blocks, num_ways, num_sets):
    sa_cache = []
    for i in range(num_ways):
        sa_cache.append([])
        for i in range(num_sets):
            sa_cache[i].append(-1)
    return sa_cache
def start_cache():
    # Prompt user for cache size and words per block
    nominal_size = prompt_nominal()
    words_per_block = prompt_words_per_block()

    # Determine mapping policy type
    typeC = determine_mapping_policy(0)

    # Determine number of blocks or ways based on mapping policy
    if typeC == 0: # Direct Mapped
        num_blocks = prompt_number_blocks()
    else: # Set Associative
        num_ways = promt_number_ways()
        num_blocks = calculateSize.numBlocks(nominal_size, words_per_block) // num_ways
        num_sets = calculateSize.numSets(num_blocks, num_ways, typeC)

    # Create cache based on mapping policy
    create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets)

def create_cache(typeC, nominal_size, words_per_block, num_blocks, num_ways, num_sets):
    number_blocks = calculateSize.numBlocks(nominal_size, words_per_block)
    # if typeC == 0: # Direct Mapped
    if typeC == 0:
        create_direct_mapped_cache(nominal_size, words_per_block, number_blocks)
    elif typeC == 1: # Set Associative
        create_set_associative_cache(nominal_size, words_per_block, number_blocks)

