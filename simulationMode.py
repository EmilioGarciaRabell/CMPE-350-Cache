import random as random
import calculateSize as calc

## prompts the user for number of word addresses to generate
## then generates random word addresses between 0 and num_word_addr*5
## returns array list of random addresses 
def generateWordAddresses(cache):
    num_word_addr = int(input("Enter the number of word addresses to generate: "))
    # Generate random word addresses
    randomAddresses = []
    for i in range(0,num_word_addr):
        # Generate a random word address between 0 and num_word_addr*5
        wordAddress = random.randint(0, cache.size)
        randomAddresses.append(wordAddress)
    return randomAddresses

## simulates the cache by generating random word addresses and checking if they are in the cache
## returns the hit rate and miss rate of the cache
def simulation(cache):
    randomAddresses = generateWordAddresses(cache)
    for address in randomAddresses:
        print(f"Checking address {address} in cache...")
        cache.input_block_in_cache(address)
        cache.print_cache()
    # calculate and print hit and miss rate
    calc.calculate_hit_miss_rate(cache)