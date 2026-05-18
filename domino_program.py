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

def deal_game():
