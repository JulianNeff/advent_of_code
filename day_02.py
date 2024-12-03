# Copied from: https://github.com/michaelerne/adventofcode-2024/blob/main/template.py

from run_util import run_puzzle

def parse_data(data):
    return [list(map(int, line.split())) for line in data.splitlines()]

def check_valid(lst, inc: bool) -> int:
    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        
        if inc:
            if diff < 1 or diff > 3:
                return 0
        else:
            if diff > -1 or diff < -3:
                return 0
    return 1

def is_safe_with_dampener(line) -> int:
    if check_valid(line, inc=True) or check_valid(line, inc=False):
        return 1
    
    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]
        if check_valid(modified_line, inc=True) or check_valid(modified_line, inc=False):
            return 1
    return 0

def part_a(data):
    lines = parse_data(data)
    return sum([check_valid(line, line[0] < line[1]) for line in lines])


def part_b(data):
    lines = parse_data(data)
    return sum([is_safe_with_dampener(line) for line in lines])


def main():
    examples = [
        ("""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""", 2, 4)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()