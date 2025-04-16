import random as random

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

## calculates the hit rate based off hits and num_word_addr (total accesses)
## returns a float value (percentage)
def calculate_hit_rate (hits, num_word_addr):
    if num_word_addr == 0:
        return 0
    return (hits / num_word_addr) * 100

## calculates the miss rate based off misses and num_word_addr (total accesses)
## returns a float value (percentage)
def calculate_miss_rate (misses, num_word_addr):
    if num_word_addr == 0:
        return 0
    return (misses / num_word_addr) * 100