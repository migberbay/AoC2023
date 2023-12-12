def read_input(day: str):
    """day expects a number from 01 to 25 and returns an iterator with the lines of the input, some exceptions can be hardcoded for special days."""
    
    if day == "00":
        pass
    elif day == "00":
        pass
    else:
        f1 = open(f"inputs/{day}.txt", 'r')
        res = f1.readlines()
        res = [l.strip('\n') for l in res]
        f1.close()

        # f2 = open(f"inputs/day{day}/1.txt")

        return res