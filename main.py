#----------------------------------------------------------
# Author:  Lila Wolf, Colde Brindisi, Emilio Garcia Rabell
# Date:    2023-10-23
# This program prmotps the user for details to create cache 
# the 

import buildCache
import promptUser as prompt
import simulationMode as sim
        

def main():
    loop = True
    cache = buildCache.start()

    mode = prompt.get_mode()
    if mode == 0: # simulation mode
        sim.simulation(cache)
    else:
        while (loop):
            loop = prompt.get_word_address(cache)
            # print hits and misses
            print(f"Cache Hits: {cache.hits}")
            print(f"Cache Misses: {cache.misses}")
        cache.print_cache()
            
    

    

if __name__ == "__main__":
    main()
    

