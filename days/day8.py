def parse_line(line: str):
    res=[]
    for v in line.split():
        res.append(int(v))
    return res

def calculate_next_sequence(sequence: list[int]):
    res = []
    for i in range(1, len(sequence)):
        j = i-1
        n = sequence[i]-sequence[j]
        res.append(n)
    return res

def calculate_next_value_for_sequences(sequences: list[list[int]]):
    inverse = list(reversed(sequences))
    next_val_seqs = [0]
    for i in range(1, len(inverse)):
        j = i-1
        a = next_val_seqs[j]
        b = inverse[i][-1]
        next_val_seqs.append(a+b)
    
    return next_val_seqs

def part1(lines):
    res = []
    for line in lines:
        seqs = []
        seq = parse_line(line)
        seqs.append(seq)
        while(True):
            seq = calculate_next_sequence(seq)
            seqs.append(seq)
            if sum(seq) == 0:
                break
        
        inversed_next_val_seqs = calculate_next_value_for_sequences(seqs)
        next_main_seq_val = list(reversed(inversed_next_val_seqs))[0]
        res.append(next_main_seq_val)

    return sum(res)
    
def part2(lines):
    return 0