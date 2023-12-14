from tqdm import tqdm

def part1(times, distances):
    wins_vals = [] 
    for i in range(len(times)):
        t = times[i]
        d = distances[i]

        possible_wins = 0
        for x in range(t, 1, -1):
            distance_covered = (t - x)*x
            if(distance_covered > d):
                possible_wins += 1

        wins_vals.append(possible_wins)

    res = 1
    for w in wins_vals:
        res *= w

    return res
    
def part2(times, distances):
    # bruteforce is kinda cringe, bynary search would've been nicer
    
    t = 49787980
    d = 298118510661181

    # while (step_value > 0):
    # start_search_val, max_search_val = 0, t
    floor_found, top_found = False, False
    for x in tqdm(range(t)):
        distance_covered = (t - x)*x

        if(distance_covered > d and not floor_found):
            min_val = x
            floor_found = True
        
        if(floor_found and not top_found and distance_covered < d):
            max_val = x
            top_found = True
        
        if(top_found and floor_found):
            # print(f"found between {min_val} and {max_val}")
            break

    return max_val - min_val
