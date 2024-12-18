from run_util import run_puzzle
import re

def parse_statements(data: str, part_a: bool):
    pattern = r'(mul\((\d+),(\d+)\))' if part_a else r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))'
    matches = re.finditer(pattern, data)
    
    total = 0
    enabled = True
    for match in matches:
        if match.group(1) == 'do()':
            enabled = True
        elif match.group(1) == "don't()":
            enabled = False
        elif enabled and "mul(" in match.group(1):
            total += int(match.group(2)) * int(match.group(3))
    return total


def part_a(data):
    return parse_statements(data, True)


def part_b(data):
    return parse_statements(data, False)


def main():
    examples = [
        ("""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""", 161, None),
        ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", None, 48)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()