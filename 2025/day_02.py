from typing import Callable
from run_util import run_puzzle


def parse_data(data: str) -> list[(int, int)]:
    return [tuple(map(int, pair.split('-'))) for pair in data.strip().split(',')]


def is_invalid_twice(s: str) -> bool:
    mid, remainder = divmod(len(s), 2)
    return remainder == 0 and s[:mid] == s[mid:]


def is_invalid_repeated(s: str) -> bool:
    return s in (s + s)[1:-1]


def solve(data: str, is_invalid: callable) -> int:
    data = parse_data(data)
    count = 0
    for start, end in data:
        for n in range(start, end + 1):
            if is_invalid(str(n)):
                count += n
    return count


def part_a(data: str) -> int:
    return solve(data, is_invalid_twice)


def part_b(data: str) -> int:
    return solve(data, is_invalid_repeated)


def main():
    examples = [
        ("""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""", 1227775554, 4174379265)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()