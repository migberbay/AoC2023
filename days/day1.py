def replace_number_strings(s: str):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replaces = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]

    for i, n in enumerate(nums):
        s = s.replace(n, replaces[i])

    return s

def solver(lines, do_replacing = False):
    nums = []

    for l in lines:
        if(do_replacing):
            l = replace_number_strings(l)

        i, j = 0, len(l)-1
        done_a, done_b = False, False
        str_res = "ab"

        for _ in range(len(l)):
            # print(l[i], l[j])

            if l[i].isdigit() and not done_a:
                str_res = str_res.replace("a", l[i])
                done_a = True
            
            if l[j].isdigit() and not done_b:
                str_res = str_res.replace("b", l[j])
                done_b = True

            i += 1
            j -= 1

            if(done_a and done_b):
                break
        
        nums.append(int(str_res))

    return sum(nums)


def part1(lines):
    return solver(lines)
    
def part2(lines):
    return solver(lines, do_replacing=True)