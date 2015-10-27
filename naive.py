# Author:   Austin Walters and Edgar García Rodríguez
# Language: Python 3.5.0 

import sys
import time
from collections import deque

# Run through round of game
def round(deck):
            
    table = deque()
    while len(deck) > 0:
        table.append(deck.popleft())
        if len(deck) != 0:
            deck.append(deck.popleft())
    table.reverse()
    return table                                                            

# Run through game
def game(count):
    
    deck = deque()
    origDeck = deque()
    ans = 1

    # Generate deck and copy
    for j in range(1, count + 1):
        deck.append(j)
        origDeck.append(j)

    # Run through one round
    deck = round(deck)

    # Loop through until deck is life first
    while deck != origDeck:

        deck = round(deck)
        ans += 1
        
    return ans



        
''' ___ MAIN ___ '''
if len(sys.argv) == 2 and int(sys.argv[1]) > 0:
    size = int(sys.argv[1])
    print('\n', size, "cards =>", game(size), "rounds\n")
else:
    print('\n', "Invalid, should be in the form:\n\n\t$ python naive.py (deck size > 0)\n")
