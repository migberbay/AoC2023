def parse_labyrinth(lines):
    for i, l in enumerate(lines):
        if 'S' in l:
            j = l.index('S')
            break
    
    #state
    pos, initial_pos, prev_pos = (i,j), (i,j), (i,j)
    mapping = {}

    s = get_moves_from_position(initial_pos, lines, 'S')
    mapping[pos] = s

    i_pipe = get_starting_pipe(s)
    lines[i] = lines[i].replace('S', i_pipe)
    
    for x in mapping[pos].values():
        if(x != -1):
            pos = x
            break

    curr_pipe = lines[pos[0]][pos[1]]

    while(True):
        s = get_moves_from_position(pos, lines, curr_pipe)
        mapping[pos] = s
        opts = [x for x in s.values() if x != -1]
        try:
            opts.remove(prev_pos)
        except:
            print(f"{prev_pos}, not in {opts}")
        prev_pos = pos
        pos = opts[0]
        curr_pipe = lines[pos[0]][pos[1]]
        if pos == initial_pos:
            break

    return initial_pos, mapping

def get_starting_pipe(initial_pos_state):
    dirs = ['up', 'down', 'left', 'right']
    idxs = [i for i, x in enumerate(initial_pos_state.values()) if x == -1]
    non_valid = set([dirs[i] for i in idxs])
    v = set(dirs)-non_valid
    
    if len(v.intersection({'down', 'up'})) == 2:
        return'|'

    if len(v.intersection({'left', 'right'})) == 2:
        return'-'
    
    if len(v.intersection({'right', 'up'})) == 2:
        return'L'

    if len(v.intersection({'left', 'up'})) == 2:
        return'J'

    if len(v.intersection({'left', 'down'})) == 2:
        return'7'

    if len(v.intersection({'right', 'down'})) == 2: 
        return'F'

def get_moves_from_position(pos, lines, curr_pipe):
    ordered_pos = ['up', 'down', 'left', 'right']
    state = dict.fromkeys(ordered_pos, -1)

    up = (pos[0]-1, pos[1])
    down = (pos[0]+1, pos[1])
    left = (pos[0], pos[1]-1)
    right = (pos[0], pos[1]+1)

    for i, c in enumerate([up, down, left, right]):
        try:
            pipe = lines[c[0]][c[1]]
        except:
            continue

        if i == 0 and pipe in {'|', '7', 'F'} and curr_pipe in {'S', '|', 'L', 'J'}: #up
            state[ordered_pos[i]] = up

        elif i == 1 and pipe in {'|', 'L', 'J'} and curr_pipe in {'S', '|', '7', 'F'}: #down
            state[ordered_pos[i]] = down

        elif i == 2 and pipe in {'-', 'F', 'L'} and curr_pipe in {'S', '-', 'J', '7'}: #left  
            state[ordered_pos[i]] = left

        elif i == 3 and pipe in {'-', 'J', '7'} and curr_pipe in {'S', '-', 'F', 'L'}: #right
            state[ordered_pos[i]] = right

    return state

def part1(lines):
    initial_pos, mapping = parse_labyrinth(lines)
    prev_pos = [initial_pos, initial_pos]
    positions = [x for x in mapping[initial_pos].values() if x != -1]
    step_count = 1

    while(True):
        step_count += 1
        next_pos = []
        for i, pos in enumerate(positions):
            pp = prev_pos[i]
            valids = [i for i in list(mapping[pos].values()) if i != -1]
            valids.remove(pp)
            next_pos.append(valids[0])
            prev_pos[i] = positions[i]

        positions = next_pos
        if(positions[0] == positions[1]):
            break

    return step_count
    
def part2(lines):
    return 0