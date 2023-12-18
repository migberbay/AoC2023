def parse_mapping(lines):
    res = dict()
    for i in range(2, len(lines)):
        node, link = lines[i].split("=")
        L, R = link.split(",")
        res[node.strip()] = {'L':L.strip().replace("(", ""), 'R':R.strip().replace(")", "")}

    return lines[0], res

def part1(lines):
    instructions, mapping = parse_mapping(lines)
    steps, idx = 0, 0
    position = "AAA"
    while(True):
        if idx == len(instructions):
            idx = 0

        step = instructions[idx]
        position = mapping[position][step]
        steps += 1
        if(position=='ZZZ'):
            break

        idx += 1

    return steps

def part2(lines):
    from math import gcd
    from tqdm import tqdm

    instructions, mapping = parse_mapping(lines)
    positions = []

    for p in mapping.keys():
        if p.endswith('A'):
            positions.append(p)

    steps_cum = []
    for p in positions:
        steps, idx = 0, 0
        while(True):
            if idx == len(instructions):
                idx = 0

            step = instructions[idx]
            p = mapping[p][step]
            steps += 1

            if p[2] == 'Z':
                break

            idx += 1

        steps_cum.append(steps)

    lcm = 1
    for i in tqdm(steps_cum):
        lcm = lcm*i//gcd(lcm, i)

    return lcm