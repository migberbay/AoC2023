from copy import deepcopy

def parse_dish(lines, width, length):
    round_rocks, square_rocks = [], []
    for _ in range(length):
        a = [0]*width
        round_rocks.append(a)
        square_rocks.append(a)

    for i, line in enumerate(lines):
        for j, rock in enumerate([*line]):
            if(rock  == 'O'):
                round_rocks[i][j] = 1
            
            if(rock == '#'):
                square_rocks[i][j] = 1

    return round_rocks, square_rocks

def get_rock_segments_by_pos(round_rocks, square_rocks, pos, width, length):
    round_rocks_map = {key: [] for key in length}
    square_rocks_map = {key: [] for key in length}

    for i, aux in enumerate(round_rocks):
        for j in range(len(aux)):
            if(pos in ['N', 'S']):
                if(round_rocks[i][j]):
                    round_rocks_map[j].append(i) 
                
                if(square_rocks[i][j]):
                    square_rocks_map[j].append(i)
            else:
                if(round_rocks[i][j]):
                    round_rocks_map[i].append(j) 
                
                if(square_rocks[i][j]):
                    square_rocks_map[i].append(j)


    return round_rocks, square_rocks

def get_rock_splits(round_rocks, square_rocks, pos, width, length):
    get_rock_segments_by_pos(round_rocks, square_rocks, pos, width, length)

    rocks_by_splits = []
    for i in range(width):
        # we add -1 as the northern wall, and infinity as the south wall
        rocks_split = []
        lst = [-1, *square_rocks[i], float('inf')]
        for s in range(len(lst)): 
            if(s == len(lst)-1):
                break

            aux = [r for r in round_rocks[i] if r > lst[s] and r < lst[s+1]]
            rocks_split.append((lst[s], aux))
        rocks_by_splits.append(rocks_split)

    return rocks_by_splits


def roll_rocks(rock_splits, lines, pos):
    # pos = 'N', 'S' , 'E', 'W'

    if pos in ['N', 'S']:
        width = len(lines[0])
        length = len(lines)
    else:
        width = len(lines)
        length = len(lines[0])

    for rocko in rock_splits:
        for r in rocko:
            top_v = max_points if r[0]==-1 else max_points - r[0] -1
            lst = list(range(top_v, top_v-r[1], -1))
            count += sum(lst)
    
def load_on_support_beam(rock_splits):
    count = 0
    for rocko in rock_splits:
        for r in rocko:
            top_v = max_points if r[0]==-1 else max_points - r[0] -1
            lst = list(range(top_v, top_v-r[1], -1))
            count += sum(lst)
    
    return count

def part1(lines):
    l, w = len(lines), len(lines)
    round_rocks, square_rocks = parse_dish(lines, w, l)
    pos = 'N'

    rock_splits = get_rock_splits(round_rocks, square_rocks, pos, w, l)
    res = roll_rocks(rock_splits, lines, pos)


    return res
    
def part2(lines):
    return 0