def parse_line(line):
    arrange, occurrs = line.split(' ')
    arrange = [*arrange]
    idx = [i for i, c in enumerate(arrange) if c == '?']
    occurs = occurrs.split(',')
    occurs = [int(i) for i in occurs]

    return [*line], idx, occurs

def check_validity_of_state(state, contiguous_damaged):
    valid = True
    for size in contiguous_damaged:
        i = 0 
        j=i+size
        # the end of the window must not be outside the upper boundry of the state list.
        found_valid = False
        while j < len(state): 
            sublist = state[i:j]
            a = ''.join(sublist)
            a.replace('?', '#')
            a = [*a]
            a = set(a)

            if(len(a) == 1 and list(a)[0] == '#'):
                # check if prev or next values of state are #
                c1,c2 = False, False
                try:
                    c1 = state[i-1] != '#'
                except: pass
                try:
                    c2 = state[j+1] != '#'
                except: pass

                found_valid = c1 and c2
                if found_valid: break
        
            i, j = i+1, j+1
        
        if(found_valid):
            indices = range(i,j)

            # remove elements replaced for the state:
            state = [x for i, x in enumerate(state) if i in indices]

            # we introduce '.' as a separator where we made cuts for the windows.
            state.insert(i,'.')
        
def calculate_next_states(state, unknown_idx, contiguous_damages):
    first_unknown = unknown_idx.pop(0)
    # the new states are 2 the one with # and with . in the position being studied.
    new_states = []

    for i in range(2):
        state_c = state.copy()
        state_c[first_unknown] = '#' if i == 0 else '.'
        is_valid = check_validity_of_state(state_c, contiguous_damages)
        if is_valid: new_states.append(state_c)

    return new_states, unknown_idx

def get_possible_arrangements(line):
    state, unknown_idx, contiguous_damages = parse_line(line)
    print(state, unknown_idx, contiguous_damages)
    states = [state]
    # branch and bound:
    for i in range(state.count('?')):
        states, unknown_idx = calculate_next_states(state, unknown_idx, contiguous_damages)

    return states

def part1(lines):
    for line in lines:
        arrangements = get_possible_arrangements(line)
        print(arrangements)
        quit()

    return 0

def part2(lines):
    return 0