def parse_games_in_line(line):
    line = line.replace(" ", "")
    a, b = line.split(":")
    id = int(a.replace("Game",""))
    games = b.split(";")

    games_lists =[]
    for game in games:
        game_list = [0,0,0]
        for g in game.split(","):
            if("green" in g):
                g_num = int(g.replace("green",""))
                game_list[1] = g_num

            elif("blue" in g):
                b_num = int(g.replace("blue",""))
                game_list[2] = b_num

            elif("red" in g):
                r_num = int(g.replace("red",""))
                game_list[0] = r_num

        games_lists.append(game_list)

    return id, games_lists

def part1(lines):
    # cubes in rgb:
    cubes = [12,13,14]
    res = 0
    for line in lines:
        id, games = parse_games_in_line(line)
        is_valid = True

        for g in games:
            if cubes[0]<g[0] or cubes[1]<g[1] or cubes[2]<g[2]:
                is_valid = False
                break
        
        if(is_valid):
            res += id

    return res
    
def part2(lines):
    res = 0
    for line in lines:
        id, games = parse_games_in_line(line)
        min_cubes = [0, 0, 0]

        for g in games:
            if min_cubes[0] < g[0]: 
                min_cubes[0] = g[0]

            if min_cubes[1] < g[1]:
                min_cubes[1] = g[1]

            if min_cubes[2] < g[2]:
                min_cubes[2] = g[2]
                
        res += (min_cubes[0] * min_cubes[1] * min_cubes[2])

    return res