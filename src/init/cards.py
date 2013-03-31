'''
Created on Mar 29, 2013

@author: Apoorva Govind

'''
import itertools
import math

class cards:
    #created by the initiator to decide the number of cards to be generated
    def __init__(self, nodeList):
        self.length = len(nodeList)
        self.noOfDecks = math.ceil(self.length/2)
        self.eachPlayerCards = math.floor((self.noOfDecks*52)/self.length)
        self.openCards = (52*self.noOfDecks)-(self.eachPlayerCards*self.length)
    #Called by gen_cards function to generate a deck
    def gen_deck(self):    
        SUITS = 'cdhs'
        RANKS = '23456789TJQKA'
        DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
        return DECK
    #Only the initiator can call gen_cards to get all the cards
    def gen_cards(self):
       
        DECK = self.gen_deck()       
        i=1
        #generate additional decks depending on total number of players
        while i < self.noOfDecks:
            DECK = DECK + self.gen_deck()
            i = i + 1;
        #At this point the deck is completely generated    
        return DECK;