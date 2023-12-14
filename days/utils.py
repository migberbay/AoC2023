def read_input(day: str):
    """day expects a number from 01 to 25 and returns an iterator with the lines of the input, some exceptions can be hardcoded for special days."""
    
    if day == "06":
        # this is manual cuz is just 4 inputs:
        # Time:        49     78     79     80
        # Distance:   298   1185   1066   1181
        return[49,78,79,80],[298,1185,1066,1181]

    elif day == "00":
        pass
    else:
        f1 = open(f"inputs/{day}.txt", 'r')
        res = f1.readlines()
        res = [l.strip('\n') for l in res]
        f1.close()
        return res