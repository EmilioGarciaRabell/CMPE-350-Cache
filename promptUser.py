
#-------------------------------------------------------------------
# Prompt the user for cache size and words per block
#-------------------------------------------------------------------

# Prompt user to provide cache size in Bytes
def get_nominal():
    # prompt user to provide nominal size in Bytes
    nominal_size = int(input("Enter nominal size in Bytes: "))
    return nominal_size

def get_words_per_block():
    # prompt user to provide words per block
    words_per_block = int(input("Enter number of words per block: "))
    return words_per_block 

# Determine the type of mapping policy 0 for for Direct Mapped, 1 for Set Associative
def get_mapping_policy():
    # prompt user to enter mapping policy
    mapping_policy = input("Enter mapping policy (DM or SA): ").strip().lower()

    if mapping_policy == "dm":
        return 0
    elif mapping_policy == "sa":
        return 1 
    else:
        print("Invalid mapping policy. Please enter 'DM' or 'SA'.")
        return None

def get_number_ways():
    # prompt user to provide number of ways
    num_ways = int(input("Enter number of ways: "))
    return num_ways
