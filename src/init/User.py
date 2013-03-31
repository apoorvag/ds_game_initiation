'''
Created on Mar 31, 2013

@author: apoorva
'''

import random
import cardStream

#input: Deck of cards and number of cards that need to be chosen
#output: Chosen cards and remaining deck of cards
def select_cards(self,DECK,numberOfCards):
        #generate required number of hands    
        hand = random.sample(DECK, numberOfCards)
        for card in hand:
            DECK.remove(card)
        #return the cards selected and the remaining cards in deck
        return (cardStream(hand,DECK,numberOfCards))
    
    