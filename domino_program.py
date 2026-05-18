def generate_dominoes():
    dominos_tiles = []
    for i in range(0, 7):
        for y in range(i, 7):
            dominos_tiles.append((i,y))
    return dominos_tiles

print(generate_dominoes())