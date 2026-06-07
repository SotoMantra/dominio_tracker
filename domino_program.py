import random

# ===== GENERATION & SETUP FUNCTIONS =====
def generate_dominoes():
    """" Creates all 28 domino tiles """
    dominos_tiles = []
    for i in range(0, 7):
        for y in range(i, 7):
            dominos_tiles.append((i,y))
    return dominos_tiles

def shuffle_tiles(deck):
    """Shuffles the deck in place"""
    random.shuffle(deck)
    return deck

def deal_game(shuffled_deck):
    """Deal 7  tiles of each 4 players"""
    hand = {
    "me" : shuffled_deck[0:7],
    "right_p" : shuffled_deck[7:14],
    "partner" : shuffled_deck[14:21],
    "left_p" : shuffled_deck[21:28],
    }
    return hand

# ===== INPUT & TRACKING FUNCTION =====
def input_parsing():
    """Parses user input into player and tile"""
    player_map = {
        'm':'me',
        'r':'right_p',
        'p':'partner',
        'l':'left_p'
    }
    player_input = input("Who played ? ")
    parts = player_input.split()

    player = player_map[parts[0]]
    tile_played = (int(parts[1][0]), int(parts[1][1]))
    return player, tile_played

def in_board(tile, played_tiles):
    """Records a played tile in the board tracker"""
    played_tiles[tile[0]].append(tile)
    played_tiles[tile[1]].append(tile)

# ===== ANALYSIS FUNCTION =====
def counting_tiles_left(number, my_hand, played_tiles):
    """Calculates remaining tiles for a given number"""
    count_in_hand = 0
    for i in my_hand:
        if number in i:
            count_in_hand += 1

    count_in_played = len(played_tiles[number])
    remaining_tiles = 7 - count_in_hand - count_in_played

    return remaining_tiles

# ===== SETUP PHASE =====
deck = generate_dominoes()
shuffled_deck = shuffle_tiles(deck)
hands = deal_game(shuffled_deck)

played_tiles = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
  }

# ===== USAGE PHASE =====
my_hand = hands['me']

# Display all hands
for player, tiles in hands.items():
    print(f"{player}: {tiles}")
print(f"\nYour hand: {my_hand}")

# Get a play
player, tile = input_parsing() 
print(player)
print(tile)
in_board(tile, played_tiles)

# Calculate remaining
remaining = counting_tiles_left(0, my_hand, played_tiles)
print(f"remaining tiles with 0: {remaining}")

