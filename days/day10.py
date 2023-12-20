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
    

def raycast_left_to_right(line):
    res = 0
    
    current_segment = []
    segment_starters = {'L','F'}
    segment_stoppers = {'J', '7'}

    inside = False
    first_segment = True
    
    for tile in line:
        seg_len = len(current_segment)

        if(tile in segment_starters or tile in {'-', '|'}):
            current_segment.append(tile)
            continue

        if(tile in segment_stoppers):
            starter = 'L' if 'L' in current_segment else 'F'
            stopper = tile
            if(first_segment):
                if(starter == 'L'):
                    if(stopper == '7'):
                        inside = True
                    elif(stopper == 'J'):
                        inside = False

                elif(starter == 'F'):
                    if(stopper == '7'):
                        inside = False
                    elif(stopper == 'J'):
                        inside = True

                first_segment = False
            else:
                if((starter == 'L' and stopper == '7') or 
                (starter == 'F' and stopper == 'J')):
                    inside = not inside
                   
            a = current_segment.count('|')
            if(a%2 != 0):
                inside = not inside

            current_segment=[]
            continue
        
        if(tile == '.'):
            css = set(current_segment)
            if len(css) == 1 and list(css)[0] == '|':
                if len(current_segment)%2 != 0:
                    inside = not inside

            current_segment=[]

            if(inside):
                res += 1

    return res

def part2(lines):
    import pprint
    pretty = pprint.PrettyPrinter()

    h, w =len(lines), len(lines[0])
    clean = [['.']*w for i in range(h)]
        
    initial_pos, mapping = parse_labyrinth(lines)
    prev_pos = [initial_pos, initial_pos]
    positions = [x for x in mapping[initial_pos].values() if x != -1]
    
    while(True):
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

    for k in mapping.keys():
        clean[k[0]][k[1]] = lines[k[0]][k[1]]
        # clean[k[0]][k[1]] = '1'

    clean_str = [''.join(c) for c in clean]
    pretty.pprint(clean_str)

    res = 0
    for line in clean:
        res += raycast_left_to_right(line)

    return res