import buildCache
import promptUser as prompt
        
    
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
        loop = prompt.get_word_address(cache)
    

if __name__ == "__main__":
    main()
    

