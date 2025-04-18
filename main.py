#----------------------------------------------------------
# Author:  Lila Wolf, Colde Brindisi, Emilio Garcia Rabell
# Date:    2023-10-23
# This program prmotps the user for details to create cache 
# the 

import buildCache
import promptUser as prompt
        

def main():
    loop = True
    cache = buildCache.start()
    print(cache)
    while (loop):
        loop = prompt.get_word_address(cache)
    

    

if __name__ == "__main__":
    main()
    

