def parse_dish(lines, width, length):
    round_rocks, square_rocks = [], []
    for _ in range(length):
        round_rocks.append([0]*width)
        square_rocks.append([0]*width)

    for i, line in enumerate(lines):
        for j, rock in enumerate([*line]):
            if(rock  == 'O'):
                round_rocks[i][j] = 1
            
            if(rock == '#'):
                square_rocks[i][j] = 1

    return round_rocks, square_rocks

def get_rock_segments(round_rocks, square_rocks, width, length):
    round_rocks_map = {key: [] for key in range(length)}
    square_rocks_map = {key: [] for key in range(length)}

    for i, aux in enumerate(round_rocks):
        for j in range(len(aux)):
            if(round_rocks[i][j]):
                round_rocks_map[j].append(i) 
            
            if(square_rocks[i][j]):
                square_rocks_map[j].append(i)
            
    return round_rocks_map, square_rocks_map

def get_rock_splits(round_rocks, square_rocks, width, length):
    round_rocks, square_rocks = get_rock_segments(round_rocks, square_rocks, width, length)

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

def roll_rocks(rock_splits, width, length):
    round_rocks = []
    for _ in range(length):
        round_rocks.append([0]*width)

    # we always tear the rolling as if it was the north and rotate the matix
    max_value = 0
    for i, rocko in enumerate(rock_splits):
        for r in rocko:
            top_v = max_value if r[0]==-1 else max_value + r[0] + 1
            lst = list( range(top_v, top_v+len(r[1])) )
            for l in lst:
                round_rocks[l][i] = 1

    return round_rocks

def load_on_support_beam(round_rocks):
    max_v = len(round_rocks)
    count = 0
    for i, rocko in enumerate(round_rocks):
        points = max_v - i 
        count += sum(rocko) * points

    return count

def rotate_matrix(round_rocks, square_rocks):
    round_rocks = list(zip(*round_rocks[::-1]))
    square_rocks = list(zip(*square_rocks[::-1]))

    return round_rocks, square_rocks

def perform_cycle(round_rocks, square_rocks, w, l):
    for _ in range(4):
        rock_splits = get_rock_splits(round_rocks, square_rocks, w, l)
        round_rocks = roll_rocks(rock_splits, w, l)
        round_rocks, square_rocks = rotate_matrix(round_rocks, square_rocks)
    
    return round_rocks

def part1(lines):
    l, w = len(lines), len(lines)
    round_rocks, square_rocks = parse_dish(lines, w, l)

    rock_splits = get_rock_splits(round_rocks, square_rocks, w, l)
    round_rocks = roll_rocks(rock_splits, w, l)
    res = load_on_support_beam(round_rocks)

    return res
    
def part2(lines):
    from tqdm import tqdm
    l, w = len(lines), len(lines)
    round_rocks, square_rocks = parse_dish(lines, w, l)

    visited = dict()
    count = 0

    test = []

    while(True):
        count += 1
        round_rocks = perform_cycle(round_rocks, square_rocks, w, l)
        flatten_rocks = ",".join("".join(str(row)) for row in round_rocks)

        if flatten_rocks in visited.keys(): break

        visited[flatten_rocks] = count
        test.append(load_on_support_beam(round_rocks)) # for test
        
    initial_loop_pos = visited[flatten_rocks]
    loop = list(visited.keys())[initial_loop_pos:]
    test_loop = test[initial_loop_pos:]

    loopable = 1000000000 - initial_loop_pos

    res_pos_in_loop = loopable % len(loop)
    res = load_on_support_beam(eval(f"[{loop[res_pos_in_loop-1]}]"))

    return res