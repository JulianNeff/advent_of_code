import bisect
import itertools
from typing import List, Tuple, Set, Callable
from run_util import run_puzzle


def parse_data(data):
    return [tuple(map(int, pair.split('-'))) for pair in data.strip().split(',')]


def is_invalid_twice(s):
    mid, remainder = divmod(len(s), 2)
    return remainder == 0 and s[:mid] == s[mid:]


def is_invalid_repeated(s):
    return s in (s + s)[1:-1]


def generate_valid_numbers(max_digits, include_repeated):
    valid_numbers = set()

    for half_len in range(1, max_digits // 2 + 1):
        multiplier = 10**half_len + 1
        start = 10**(half_len - 1)
        end = 10**half_len
        for i in range(start, end):
            valid_numbers.add(i * multiplier)

    if include_repeated:
        for total_len in range(1, max_digits + 1):
            for sub_len in range(1, total_len // 2 + 1):
                if total_len % sub_len == 0:
                    k = total_len // sub_len
                    if k <= 2:
                        continue

                    multiplier = sum(10**(p * sub_len) for p in range(k))
                    start = 10**(sub_len - 1)
                    end = 10**sub_len
                    for i in range(start, end):
                        valid_numbers.add(i * multiplier)
    
    return valid_numbers


def solve_brute_force(ranges, predicate):
    count = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if predicate(str(n)):
                count += n
    return count


def solve_optimized(ranges, is_part_a):
    max_val = max(end for _, end in ranges)
    max_digits = len(str(max_val))
    
    valid_numbers = generate_valid_numbers(max_digits, not is_part_a)
    sorted_valid = sorted(valid_numbers)
    prefix_sums = [0] + list(itertools.accumulate(sorted_valid))

    total = 0
    for start, end in ranges:
        left = bisect.bisect_left(sorted_valid, start)
        right = bisect.bisect_right(sorted_valid, end)
        total += prefix_sums[right] - prefix_sums[left]
    return total


def solve(data, is_part_a):
    ranges = parse_data(data)
    total_range_size = sum(end - start for start, end in ranges)
    
    # Heuristic: Use brute force for small ranges, optimized for large ones
    if total_range_size < 10**6:
        predicate = is_invalid_twice if is_part_a else is_invalid_repeated
        return solve_brute_force(ranges, predicate)
    else:
        return solve_optimized(ranges, is_part_a)


def part_a(data):
    return solve(data, True)


def part_b(data):
    return solve(data, False)


def main():
    examples = [
        ("""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""", 1227775554, 4174379265)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()