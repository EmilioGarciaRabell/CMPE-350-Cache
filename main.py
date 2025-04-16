import buildCache


def promt_word_address(cache):
    address = input("Enter Word Address, c(lear), q(uit): ")
    if address == "c":
        cache = buildCache.input_block_in_cache(cache)
        return True
    elif address == 'q':
        return False
    
# Set all values in cache to zero
def clear(cache):
    for i in cache:
        for j in i:
            cache[i][j] = 0
    return cache


# Main user input loop

def main():
    loop = True
    cache = buildCache.start()
    print(cache)
    # while (loop):
    #     loop = promt_word_address(cache)
    

if __name__ == "__main__":
    main()
    

