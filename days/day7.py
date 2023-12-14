cards_0 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards_j = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def parse_hand(line: str, joker: bool):
    # cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    cards = cards_j if joker else cards_0
    count = [0] * len(cards)
    for i, c in enumerate(cards):
        occurrences = line.count(c)
        count[i] += occurrences 

    return count

def get_hand_power(hand_count: list[int], hand_text: str, joker:bool):
    # power goes from 1 to 7 depending on the hand. (5 of a kind to no equal cards)
    # then top_card goes from 0-13 depending on the first in the hand.

    m  = max(hand_count) 
    num_jokers = hand_count[12]

    # we add the number of jokers to the highest value in the list hand_count
    # that should always create the strongest hand possible.
    if(joker and num_jokers != 5): 
        # if there is a tie between jokers and other,
        # since jokers are in the last position the other one will return first
        i = hand_count.index(m) 
        if i != 12: # we add the number of jokers to all but the joker pos
            hand_count[i] += num_jokers
           
        else: 
            # we need to find the second highest number in the list and add the jokers to that
            aux = [i for i in hand_count if i != 0] # we remove all 0 and sort
            aux.sort(reverse=True) # take second value
            j = hand_count.index(aux[1])
            hand_count[j] += num_jokers # add jokers to top2

        # then we remove the jokers since they are counted as some other card.
        hand_count[12] = 0
        # and update the max count value.
        m  = max(hand_count)

    if m == 5:
        power = 7

    elif m == 4:
        power = 6

    elif m == 3: 
        if 2 in hand_count:
            power = 5
        else:
            power = 4

    elif m == 2:
        if hand_count.count(2) == 2:
            power = 3
        else:
            power = 2

    else:
        power = 1 
    
    cards = cards_j if joker else cards_0
    ordered_hand_power = []
    for c in hand_text:
        card_power = 13 - cards.index(c)
        ordered_hand_power.append(card_power)
    
    return power, ordered_hand_power

def solver(lines, joker):
    all_hands = []
    for line in lines:
        hand, bet = line.split(' ')
        hand, bet = hand.strip(), bet.strip()

        count = parse_hand(hand, joker)
        hand_power, ordered_card_power = get_hand_power(count, hand, joker)

        all_hands.append([hand, int(bet), hand_power, ordered_card_power])

    all_hands_sorted = sorted(all_hands, key=lambda x: (x[2], x[3]))

    res = 0
    for i, h in enumerate(all_hands_sorted):
        res += (i+1) * h[1]

    return res

def part1(lines):
    return solver(lines, False)
    
def part2(lines):
    return solver(lines, True)