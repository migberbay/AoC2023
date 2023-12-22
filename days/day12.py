def parse_line(line):
    arrange, occurrs = line.split(' ')
    arrange = [*arrange]
    idx = [i for i, c in enumerate(arrange) if c == '?']
    occurs = occurrs.split(',')
    occurs = [int(i) for i in occurs]

    return arrange, idx, occurs

def check_validity_of_state(state, contiguous_damaged):
    replaced_in_state = set()
    for size in contiguous_damaged:
        i = 0 
        j=i+size
        # the end of the window must not be outside the upper boundry of the state list.
        found_valid = False

        while j < len(state)+1: 
            sublist = state[i:j]
            a = ''.join(sublist)
            a = a.replace('?', '#')
            a = [*a]
            a = set(a)

            if(len(a) == 1 and list(a)[0] == '#'):
                # check if prev or next values of state are #
                c1,c2,c3 = False, False, False

                if(i-1 > 0):
                    c1 = state[i-1] != '#'
                else: c1 = True

                if(j+1 < len(state)):
                    c2 = state[j] != '#' # its not j+1 due to the nature of python ranges.
                else: c2 = True

                if len(set(range(i,j)).intersection(replaced_in_state)) == 0: c3 = True

                found_valid = c1 and c2 and c3

                if found_valid: break
        
            i, j = i+1, j+1
        
        if(found_valid):
            indices = range(i,j)
            replaced_in_state.update(indices)
            # replace elements in state with #:
            for i in range(i,j):
                state[i] = '#'
            
        else:
            return False
    
    return True
        
def calculate_next_states(state, unknown_idx, contiguous_damages):
    first_unknown = unknown_idx.pop(0)
    # the new states are 2 the one with # and with . in the position being studied.
    new_states = []

    for i in range(2):
        state_c = state.copy()
        state_c[first_unknown] = '#' if i == 0 else '.'
        s = state_c.copy()
        is_valid = check_validity_of_state(state_c, contiguous_damages)
        if is_valid: new_states.append(s)

    return new_states

def get_possible_arrangements(line):
    state, unknown_idx, contiguous_damages = parse_line(line)
    print(state, unknown_idx, contiguous_damages)
    states = [state]
    # branch and bound:
    while(True):
        next_states = []
        for state in states:
            u = unknown_idx.copy()
            s = calculate_next_states(state, u, contiguous_damages)
            next_states.extend(s)
        states = next_states
        unknown_idx.pop(0)

        if(len(unknown_idx)==0):
            break

    return states

def part1(lines):
    for line in lines:
        arrangements = get_possible_arrangements(line)
        print(line, len(arrangements))
        print('\n\n')

    return 0

def part2(lines):
    return 0