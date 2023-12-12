# run this for everything to work.
from days import utils, day1, day2

while(True):
    # agu recomendations: 4 6 7 9 10 11
    res = input("choose a day to solve (01-25) or \"exit\": ")

    def print_solutions(s1, s2):
        print(f"problem 1 solution: {s1}, problem 2 solution: {s2}")

    if res == '01':
        lines = utils.read_input(res)
        print_solutions(day1.part1(lines), day1.part2(lines))

    elif res == '02':
        lines = utils.read_input(res)
        print_solutions(day2.part1(lines), day2.part2(lines))

    elif res == '03':
        print("unimplemented")

    elif res == '04':
        print("unimplemented")

    elif res == '05':
        print("unimplemented")

    elif res == '06':
        print("unimplemented")

    elif res == '07':
        print("unimplemented")

    elif res == '08':
        print("unimplemented")

    elif res == '09':
        print("unimplemented")

    elif res == '10':
        print("unimplemented")

    elif res == '11':
        print("unimplemented")

    elif res == '12':
        print("unimplemented")

    elif res == '13':
        print("unimplemented")

    elif res == '14':
        print("unimplemented")

    elif res == '15':
        print("unimplemented")

    elif res == '16':
        print("unimplemented")

    elif res == '17':
        print("unimplemented")

    elif res == '18':
        print("unimplemented")

    elif res == '19':
        print("unimplemented")

    elif res == '20':
        print("unimplemented")

    elif res == '21':
        print("unimplemented")

    elif res == '22':
        print("unimplemented")

    elif res == '23':
        print("unimplemented")

    elif res == '24':
        print("unimplemented")

    elif res == '25':
        print("unimplemented")
    
    elif res == 'exit':
        break

    else:
        print("invalid input type 01-25, or exit.")