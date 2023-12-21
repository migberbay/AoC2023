def parse_line(line):
    arrange, occurrs = line.split(' ')
    arrange = [*arrange]
    idx = [i for i, c in enumerate(arrange) if c == '?']
    occurs = occurrs.split(',')
    occurs = [int(i) for i in occurs]

    return arrange, idx, occurs

def check_validity_of_state(state, contiguous_damaged):
    for size in contiguous_damaged:
        i = 0 
        j=i+size
        # the end of the window must not be outside the upper boundry of the state list.
        found_valid = False
        while j < len(state): 
            sublist = state[i:j]
            a = ''.join(sublist)
            a = a.replace('?', '#')
            a = [*a]
            a = set(a)

            if(len(a) == 1 and list(a)[0] == '#'):
                # check if prev or next values of state are #
                c1,c2 = False, False

                if(i-1 > 0):
                    c1 = state[i-1] != '#'
                else: c1 = True

                if(j+1 < len(state)):
                    c2 = state[j+1] != '#'
                else: c2 = True

                found_valid = c1 and c2

                if found_valid: break
        
            i, j = i+1, j+1
        
        if(found_valid):
            indices = range(i,j)

            # remove elements replaced for the state:
            for i in range(i,j):
                state[i] = '.'
        
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