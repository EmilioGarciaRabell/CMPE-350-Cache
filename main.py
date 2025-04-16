import buildCache

cache = buildCache.start()

# Set all values in cache to zero
def clear(cache):
    for i in cache:
        for j in i:
            cache[i][j] = 0
    return cache

# Main user input loop
while (True):

    address = input("Enter Word Address, c(lear), q(uit): ")
    if address == "c":
        cache = clear(cache)
        continue
    elif address == 'q':
        break
    
    