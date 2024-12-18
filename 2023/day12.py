from run_util import run_puzzle
from functools import cache

@cache
def count(spring: str, pattern: str, pos: int, deffect: int, curr_pat: int) -> int:
    if pos >= len(spring):
        return 0 if len(pattern) > curr_pat else 1

    if spring[pos] == '#':
        if len(pattern) > curr_pat and pattern[curr_pat] < deffect:
            return 0
        else:
            return count(spring, pattern, pos + 1, deffect + 1, curr_pat)

    if spring[pos] == '.' or curr_pat == len(pattern):
        if curr_pat < len(pattern) and deffect == pattern[curr_pat]:
            return count(spring, pattern, pos + 1, 0, curr_pat + 1)
        elif deffect == 0:
            return count(spring, pattern, pos + 1, 0, curr_pat)
        else:
            return 0

    first = count(spring, pattern, pos + 1, deffect + 1, curr_pat)

    if deffect == 0:
        return first + count(spring, pattern, pos + 1, 0, curr_pat)

    if deffect == pattern[curr_pat]:
        return first + count(spring, pattern, pos + 1, 0, curr_pat + 1)

    return first


def solve(data: str, part_a: bool):
    tuples = [tuple(line.split(' ')) for line in data.split('\n')]

    func = lambda x: x[0] + "." if part_a else '?'.join([x[0]]*5) + '.'
    mult = 1 if part_a else 5
    
    tuples = [(func(x), tuple([int(y) for y in x[1].split(',')] * mult)) for x in tuples]

    return sum([count(springs, patterns, 0, 0, 0) for springs, patterns in tuples])


def part_a(data):
    # print(solve(data, True))
    # raise Exception()
    return solve(data, True)


def part_b(data):
    return solve(data, False)


def main():
    examples = [
        ("""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""", 21, 525152)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)

if __name__ == '__main__':
    main()