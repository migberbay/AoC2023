import numpy as np

class Tile:
    def __init__(self, val, i, j):
        self.energized = False
        self.val = val
        self.pos = (i,j)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

class TileMap:
    def __init__(self, lines):
        w, l = len(lines[0]), len(lines)
        size = w*l
        self.tiles = np.array([0]*size).reshape(l,w).tolist()

        for i, line in enumerate(lines):
            for j, t in enumerate([*line]):
                tile = Tile(t, i, j)
                self.tiles[i][j] = tile

    def __str__(self):
        r = ''
        for line in self.tiles:
            r += f'{line}\n'

        return r

def part1(lines):
    m = TileMap(lines)
    print(m)
    return 0
    
def part2(lines):
    return 0