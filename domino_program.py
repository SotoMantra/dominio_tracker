import random

def generate_dominoes():
    dominos_tiles = []
    for i in range(0, 7):
        for y in range(i, 7):
            dominos_tiles.append((i,y))
    return dominos_tiles

def shuffle_tiles(deck):
   random.shuffle(deck)
   return deck

def deal_game(shuffled_deck):
    hand = {
    "me" : shuffled_deck[0:7],
    "right_p" : shuffled_deck[7:14],
    "partner" : shuffled_deck[14:21],
    "left_p" : shuffled_deck[21:28],
    }
    return hand


