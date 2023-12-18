def parse_labyrinth(lines: list[str]):
    for i, l in enumerate(lines):
        if 'S' in l:
            j = l.index('S')
            break
    start_pos = (i, j) #128,36

    assert lines[start_pos[0]][start_pos[1]] == 'S'

    # we map from S the start node to {up:#, down:#, left:#, right:#}
    # where the # are indexes of nodes (so we can track which nodes we have visited already)
    # node indexes are the concatenation of the coordinates they belong to, with 0 padding to make a 3 digit number for each
    # we stop mapping when we reach the initial node again (circle complete)
    # S is the only special case, we manually define it and then proceed with automatic nodes.
    # -1 indicates the node in that direction is not accesible.

    s_index = pos_to_index(start_pos) # 128036 or 001001

    # TODO: Correct this initial mapping.
    # mapping = {s_index: {'up':-1, 'down':'129037', 'left':-1, 'right':'127037'}}
    # current_pos, prev_pos, last_move, pipe_taken = (129,37), start_pos, 'down', 'L'

    mapping = {s_index: {'up':-1, 'down':'002001', 'left':-1, 'right':'001002'}}
    current_pos, prev_pos, last_move, pipe_taken = (2,1), start_pos, 'down', '|'

    def calculate_new_state(pos_change, move_name):
        dir_pos = (current_pos[0] + pos_change[0], current_pos[1] + pos_change[1])
        try:
            pipe_type = lines[dir_pos[0]][dir_pos[1]]
        except:
            # move is out of bounds (considered impossible.)
            move = -1
        else:
            move = apply_pipe_to_pos(move_name, pipe_type)

        if(move != -1):
            # there should only be one possible move,
            # so we update the position and staate variables if we find a non -1 move.
            prev_pos = current_pos
            nonlocal new_pos, last_move, pipe_taken
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            last_move = move_name
            pipe_taken = pipe_type
            s_curr[move_name] = pos_to_index(new_pos)
        else:
            s_curr[move_name] = -1

    state = {'up':'', 'down':'', 'left':'', 'right':''}

    while(True):
        if(current_pos == start_pos): # reached initial node, all mapped.
            break
        
        s_curr = state.copy()
        return_move =  get_return_move(last_move, pipe_taken)
        s_curr[return_move] = pos_to_index(prev_pos)
        
        new_pos = -1
        if return_move != 'up':
            calculate_new_state((-1,0),'up')
            
        if return_move != 'down':
            calculate_new_state((1,0),'down')

        if return_move != 'left':
            calculate_new_state((0,-1),'left')

        if return_move != 'right':
            calculate_new_state((0,1),'right')
            
        if(new_pos != -1):
            mapping[pos_to_index(current_pos)] = s_curr
            current_pos = new_pos

    return s_index, mapping

def pos_to_index(pos):
    return f"{str(pos[0]).zfill(3)}{str(pos[1]).zfill(3)}"

def get_return_move(prev_move, prev_pipe):
    ''' 
    Given the previous move made and the pipe taken, provides the move needed to return to that position.
    '''
    if prev_pipe == '|':
        if prev_move == 'up':
            return 'down'
        if prev_move == 'down':
            return 'up'    

    if prev_pipe == '-':
        if prev_move == 'left':
            return 'right'  
        if prev_move == 'right':
            return 'left'  

    if prev_pipe == 'L':
        if prev_move == 'down':
            return 'left'  
        if prev_move == 'left':
            return 'down' 
    
    if prev_pipe == 'J':
        if prev_move == 'down':
            return 'right'  
        if prev_move == 'right':
            return 'down'  
    
    if prev_pipe == '7':
        if prev_move == 'up':
            return 'right'  
        if prev_move == 'right':
            return 'up'  
    
    if prev_pipe == 'F':
        if prev_move == 'up':
            return 'left'
        if prev_move == 'left':
            return 'up'

def apply_pipe_to_pos(orientation, pipe_type):
    if pipe_type == '|':
        if orientation == 'down':
            return (1, 0)
        if orientation == 'up':
            return (-1, 0)
        

    if pipe_type == '-':
        if orientation == 'left':
            return (0, -1)
        if orientation == 'right':
            return (0, 1)
        

    if pipe_type == 'L':
        if orientation == 'down':
            return (1, 0)
        if orientation == 'left':
            return (0, -1)
        
    
    if pipe_type == 'J':
        if orientation == 'down':
            return (1, 0)
        if orientation == 'right':
            return (0, 1)
        
    
    if pipe_type == '7':
        if orientation == 'up':
            return (-1, 0)
        if orientation == 'right':
            return (0, 1)
        
    
    if pipe_type == 'F':
        if orientation == 'up':
            return (-1, 0)
        if orientation == 'left':
            return (0, -1)

    return -1

def part1(lines):
    start_index, mapping = parse_labyrinth(lines)
    print(start_index, mapping)
    return 0
    
def part2(lines):
    return 0