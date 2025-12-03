from run_util import run_puzzle

def parse_data(data):
    return [list(map(int, line)) for line in data.splitlines() if line]


def solve(data, is_part_a):
    data = parse_data(data)
    total_sum = 0
    k = 2 if is_part_a else 12
    
    for line in data:
        to_remove = len(line) - k
        stack = []
        for digit in line:
            while to_remove > 0 and stack and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        
        result_digits = stack[:k]
        total_sum += int("".join(map(str, result_digits)))
    return total_sum


def part_a(data):
    return solve(data, True)


def part_b(data):
    return solve(data, False)


def main():
    examples = [
        ("""987654321111111
811111111111119
234234234234278
818181911112111
""", 357, 3121910778619)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()