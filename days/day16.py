import numpy as np

class Tile:
    def __init__(self, val, i, j):
        self.energized = False
        self.val = val
        self.pos = (i,j)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return '#' if self.energized else '.'

class Ray:
    def __init__(self, i, j, orientation, w, l):
        if (i<0 or i>=l) or (j<0 or j>=w):
            raise IndexError("Ray Escapes the grid.")

        self.pos = (i,j)
        self.orient = orientation

    def __str__(self):
        return str(self.pos, self.orient)

class TileMap:
    def __init__(self, lines):
        self.w, self.l = len(lines[0]), len(lines)
        size = self.w*self.l
        self.tiles = np.array([0]*size).reshape(self.l,self.w).tolist()

        for i, line in enumerate(lines):
            for j, t in enumerate([*line]):
                tile = Tile(t, i, j)
                self.tiles[i][j] = tile

    def evaluate_ray(self, ray: Ray):
        rays = []
        i,j = ray.pos[0], ray.pos[1]
        ori = ray.orient
        t = self.tiles[i][j] # this is done just in case.
        t.energized = True

        if(t.val == '.'):
            if(ori ==  'right'):
                r = Ray(i, j+1, 'right', self.w, self.l)
            if(ori ==  'left'):
                r = Ray(i, j-1, 'left', self.w, self.l)
            if(ori ==  'up'):
                r = Ray(i-1, j, 'up', self.w, self.l)
            if(ori ==  'down'):
                r = Ray(i+1, j, 'down', self.w, self.l)

            rays.append(r)

        if(t.val == '/'):
            if(ori ==  'right'):
                r = Ray(i, j+1, 'up', self.w, self.l)
            if(ori ==  'left'):
                r = Ray(i, j-1, 'down', self.w, self.l)
            if(ori ==  'up'):
                r = Ray(i-1, j, 'left', self.w, self.l)
            if(ori ==  'down'):
                r = Ray(i+1, j, 'right', self.w, self.l)
            
            rays.append(r)

        if(t.val == '\\'):
            if(ori ==  'right'):
                r = Ray(i, j+1, 'down', self.w, self.l)
            if(ori ==  'left'):
                r = Ray(i, j-1, 'up', self.w, self.l)
            if(ori ==  'up'):
                r = Ray(i-1, j, 'right', self.w, self.l)
            if(ori ==  'down'):
                r = Ray(i+1, j, 'left', self.w, self.l)

            rays.append(r)

        if(t.val == '|'):
            if(ori ==  'right'):
                r1 = Ray(i, j+1, 'up', self.w, self.l)
                r2 = Ray(i, j+1, 'down', self.w, self.l)
                rays.append(r1)
                rays.append(r2)

            if(ori ==  'left'):
                r1 = Ray(i, j-1, 'up', self.w, self.l)
                r2 = Ray(i, j-1, 'down', self.w, self.l)
                rays.append(r1)
                rays.append(r2)

            if(ori ==  'up'):
                r = Ray(i-1, j, 'up', self.w, self.l)
                rays.append(r)

            if(ori ==  'down'):
                r = Ray(i+1, j, 'down', self.w, self.l)
                rays.append(r)

        if(t.val == '-'):
            if(ori ==  'right'):
                r = Ray(i, j+1, 'right', self.w, self.l)

            if(ori ==  'left'):
                r = Ray(i, j-1, 'left', self.w, self.l)

            if(ori ==  'up'):
                r1 = Ray(i-1, j, 'left', self.w, self.l)
                r2 = Ray(i-1, j, 'right', self.w, self.l)
                rays.append(r1)
                rays.append(r2)

            if(ori ==  'down'):
                r1 = Ray(i+1, j, 'left', self.w, self.l)
                r2 = Ray(i+1, j, 'right', self.w, self.l)
                rays.append(r1)
                rays.append(r2)

        return rays

    def get_energized_tiles(self):
        return 0

    def __str__(self):
        r = ''
        for line in self.tiles:
            r += f'{line}\n'

        return r

def part1(lines):
    t_map = TileMap(lines)
    #orientation is right, left, up or down.
    rays = [Ray(0, 0,'right')]

    while(len(rays) != 0):
        new_rays = []
        for r in rays:
           new_rays.extend(t_map.evaluate_ray(r))
        
        rays = new_rays
    
    print(t_map)

    return t_map.get_energized_tiles()
    
def part2(lines):
    return 0