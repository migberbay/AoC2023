def parse_card(line: str):
    line = line.replace("  ", " ")
    a, b = line.split(":")
    id = int(a.replace(" ","").replace("Card",""))

    w, n = b.strip().split("|")
    winners, numbers = w.strip().split(" "), n.strip().split(" ")
    winners, numbers = [int(w) for w in winners], [int(n) for n in numbers]

    return id, winners, numbers

def part1(lines):
    import math
    res = 0
    for line in lines:
        id, winners, numbers = parse_card(line)
        win, num = set(winners), set(numbers)
        matches = set.intersection(win, num)

        if(len(matches) > 0):
            res += math.pow(2, len(matches)-1)
    	
    return res
    
def part2(lines):
    keys = range(1,len(lines)+1)
    card_dict =  dict.fromkeys(keys, 1)

    for line in lines:
        id, winners, numbers = parse_card(line)
        win, num = set(winners), set(numbers)
        matches = set.intersection(win, num)
        num_copies = len(matches)

        for i in range(id+1, id+1+num_copies):
            card_dict[i] += card_dict[id]

    return sum(list(card_dict.values()))