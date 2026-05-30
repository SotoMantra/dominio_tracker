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

def input_parsing():
    player_map = {
        'm':'me',
        'r':'right_p',
        'p':'partner',
        'l':'left_p'
    }

    player_input = input("Who played? ")
    parts = player_input.split()

    player = player_map[parts[0]]
    tile_played = (int(parts[1][0]), int(parts[1][1]))
    return player, tile_played

played_tiles = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
  }

def in_board(tile, played_tiles):
    played_tiles[tile[0]].append(tile)
    played_tiles[tile[1]].append(tile)

def counting_tiles_left(number, my_hand, played_tiles):
    count_in_hand = 0
    for i in my_hand:
        if number in i:
            count_in_hand += 1

    count_in_played = len(played_tiles[number])
    remaining_tiles = 7 - count_in_hand - count_in_played

    return remaining_tiles

deck = generate_dominoes()
shuffled_deck = shuffle_tiles(deck)
hands = deal_game(shuffled_deck)

for player, tiles in hands.items():
    print(f"{player}: {tiles}")

my_hand = hands['me']
print(my_hand)

player, tile = input_parsing()
print(player)
print(tile)

in_board(tile, played_tiles)

remaining = counting_tiles_left(0, my_hand, played_tiles)

print(remaining)