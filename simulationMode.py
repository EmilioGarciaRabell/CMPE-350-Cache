import random as random
import calculateSize 

## prompts the user for number of word addresses to generate
## then generates random word addresses between 0 and num_word_addr*5
## returns array list of random addresses 
def generateWordAddresses():
    num_word_addr = int(input("Enter the number of word addresses to generate: "))
    # Generate random word addresses
    randomAddresses = []
    for i in range(0,num_word_addr):
        # Generate a random word address between 0 and num_word_addr*5
        wordAddress = random.randint(0, num_word_addr*5)
        randomAddresses.append(wordAddress)
    return randomAddresses

## simulates the cache by generating random word addresses and checking if they are in the cache
## returns the hit rate and miss rate of the cache
def simulation(cache):
    randomAddresses = generateWordAddresses()
    for address in randomAddresses:
        cache.input_block_in_cache(address)
    hit_rate = calculateSize.calculate_hit_rate(cache.hits, len(randomAddresses))
    miss_rate = calculateSize.calculate_miss_rate(cache.misses, len(randomAddresses))
    print(f"Hit rate: {hit_rate}%")
    print(f"Miss rate: {miss_rate}%")
