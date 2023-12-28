def hash_string(s:str):
    v = 0
    for c in [*s]:
        v += ord(c)
        v *= 17
        v %= 256
    return v

def exectue_instruction(ins:str, boxes:dict):
    if "-" in ins:
        label = ins.replace('-','')
        v = hash_string(label)
        try:
            boxes[v].pop(label) # remove the item
        except: pass # if its not there nothing happens.

    if "=" in ins:
        label, focal = ins.split('=')
        v = hash_string(label)
        boxes[v][label] = focal
    
    return boxes

def part1(lines):
    seq = lines[0].split(',')
    res = 0
    for s in seq:
        res += hash_string (s)

    return res
    
def part2(lines):
    keys = list(range(256))
    boxes = { k : dict() for k in keys }
    
    seq = lines[0].split(',')
    for ins in seq:
        boxes = exectue_instruction(ins, boxes)

    #calculate focusing power:
    res = 0

    for k, v in boxes.items():
        boxnum = k+1
        for i, focal in enumerate(v.values()):
            slot = i+1
            res += (boxnum * slot * int(focal))

    return res