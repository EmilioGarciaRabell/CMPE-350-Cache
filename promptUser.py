
#-------------------------------------------------------------------
# Prompt the user for cache size and words per block
#-------------------------------------------------------------------

# Prompt user to provide cache size in Bytes
def get_nominal():
    # prompt user to provide nominal size in Bytes
    try:
        nominal_size = int(input("Enter nominal size in Bytes: "))
        return nominal_size
    except ValueError:
        print("Invalid input. Please enter a valid integer for cache size.")
        get_nominal()

# Prompt user to provide words per block
def get_words_per_block():
    # prompt user to provide words per block
    try:
        words_per_block = int(input("Enter number of words per block: "))
        return words_per_block 
    except ValueError:
        print("Invalid input. Please enter a valid integer for words per block.")
        get_words_per_block()

# Determine the type of mapping policy 0 for for Direct Mapped, 1 for Set Associative
def get_mapping_policy():
    # prompt user to enter mapping policy
    mapping_policy = input("Enter mapping policy (DM or SA): ").strip().lower()

    if mapping_policy == "dm":
        return 0
    elif mapping_policy == "sa":
        return 1 
    else:
        print("Invalid mapping policy. Please enter 'DM' or 'SA'. Try again")
        get_mapping_policy()

# Prompt user to provide number of ways for Set Associative mapping policy
def get_number_ways():
    # prompt user to provide number of ways
    try:
        num_ways = int(input("Enter number of ways: "))
        return num_ways
    except ValueError:
        print("Invalid input. Please enter a valid integer for number of ways.")
        get_number_ways()

# Prompt user to provide word address to check in cache
def get_word_address(cache):
    address = input("Enter Word Address, c(lear), q(uit): ")
    
    if address == "c":
        cache = cache.clear_cache()
        return cache
    elif address == 'q':
        return 0
    elif address.isdigit():
        return cache.input_block_in_cache(int(address))
    else:
        print("Invalid input. Please enter a valid word address, 'c' to clear, or 'q' to quit.")
        get_word_address(cache)
    
# Prompt user for mode of operation (simulation or input)
def get_mode():
    mode = input("Enter mode (s(imulation) or i(nput)): ").strip().lower()
    
    if mode == "s":
        return 0
    elif mode == "i":
        return 1 
    else:
        print("Invalid mode. Please enter 's' or 'i'.")
        get_mode()