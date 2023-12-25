from itertools import groupby

def parse_line(line):
    arrange, occurrs = line.split(' ')
    arrange = [*arrange]
    idx = [i for i, c in enumerate(arrange) if c == '?']
    occurs = occurrs.split(',')
    occurs = [int(i) for i in occurs]

    return arrange, idx, occurs

def check_validity_of_state(state, contiguous_damaged):
    
    # pre check for already a valid state with all ? as .
    test1 = ''.join(state).replace('?', '.')
    test1 = [*test1]
    aux = [len(list(group)) for k, group in groupby(test1, lambda x: x == "." or x =='?') if not k]
    if(aux == contiguous_damaged):
        return True

    # pre check for '##' groups formed already that are larger than the possible groups in order.
    aux = [list(group) for k, group in groupby(state, lambda x: x == ".") if not k]
    for i, d in enumerate(contiguous_damaged):
        try:
            if len(aux[i]) > d:
                if('?' in aux[i]):
                    break

                return False
        except:
            break
    
    # main window testing discard
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

                if(i-1 >= 0):
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
            indices = list(range(i,j))
            replaced_in_state.update(indices)
            # replace elements in state with #:
            for i in range(i,j):
                state[i] = '#'
        else:
            return False
    
    # post check for modified state to make absolutely sure this is correct.
    aux = [len(list(group)) for k, group in groupby(state, lambda x: x == "." or x =='?') if not k]
    return (aux == contiguous_damaged)
        
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
    # print(state, unknown_idx, contiguous_damages)
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

# I TRIED BRANCH AND BOUND ABOVE AND DID AN ABSOLUTE MESS
# IT IS WAY BETTER JUST TO DO FUCKING CHACHES FOR EVERY PARTIAL RESULT.
# this is called memoization and it is how fibonacci is calculated
from functools import cache

@cache
def count_arrangements(conditions, rules):
    if not rules:
        return 0 if "#" in conditions else 1
    if not conditions:
        return 1 if not rules else 0

    result = 0

    if conditions[0] in ".?":
        result += count_arrangements(conditions[1:], rules)
        
    if conditions[0] in "#?":
        if (
            rules[0] <= len(conditions)
            and "." not in conditions[: rules[0]]
            and (rules[0] == len(conditions) or conditions[rules[0]] != "#")
        ):
            result += count_arrangements(conditions[rules[0] + 1 :], rules[1:])

    return result

def part1(lines):
    res = 0
    for line in lines:
        conditions, rules = line.split()
        rules = eval(rules)
        res += count_arrangements(conditions, rules)

    return res

def part2(lines):
    res = 0
    for line in lines:
        conditions, rules = line.split()
        rules = eval(rules)
        conditions = "?".join([conditions] * 5)
        rules = rules * 5

        res += count_arrangements(conditions, rules)

    return res