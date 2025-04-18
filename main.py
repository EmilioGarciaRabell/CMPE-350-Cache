#----------------------------------------------------------
# Author:  Lila Wolfanger, Colde Brindisi, Emilio Garcia Rabell
# Date:    2025-04-18
# This program prmotps the user for details to create the cache 
#----------------------------------------------------------

import buildCache
import promptUser as prompt
import simulationMode as sim
import calculateSize as calc    

def main():
    loop = True
    cache = buildCache.start()
    mode = prompt.get_mode()

    if mode == 0: # simulation mode
        sim.simulation(cache)
    else:   # user input mode
        while (loop):
            loop = prompt.get_word_address(cache)
            # print hits and misses
            print(f"Cache Hits: {cache.hits}")
            print(f"Cache Misses: {cache.misses}")
            cache.print_cache()
        # exiting loop
        print("Exiting program...")
        calc.calculate_hit_miss_rate(cache) # calculate and print hit and miss rate

if __name__ == "__main__":
    main()
