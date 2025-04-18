import buildCache


def promt_word_address(cache):
    address = input("Enter Word Address, c(lear), q(uit): ")
    if address == "c":
        cache = cache.clear()
        return cache
    elif address == 'q':
        return 0
    else:
        return cache.input_block_in_cache(int(address))
        
    
# Set all values in cache to zero
# def clear(cache):
#     # TODO fix clearing - implement in class
#     for i in cache.cache.size():
#         for j in i:
#             cache[i][j] = 0
#     return cache


# Main user input loop

def main():
    loop = True
    cache = buildCache.start()
    print(cache)
    while (loop):
        loop = promt_word_address(cache)
    

if __name__ == "__main__":
    main()
    

