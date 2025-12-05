import bisect
from run_util import run_puzzle

def parse_data(data):
    ranges_part, ids_part = data.split('\n\n')
    ranges = [tuple(map(int, r.split('-'))) for r in ranges_part.splitlines()]
    ids = list(map(int, ids_part.splitlines()))
    return ranges, ids

def merge_ranges(ranges):
    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def part_a(data):
    ranges, ids = parse_data(data)
    merged = merge_ranges(ranges)
    starts = [r[0] for r in merged]
    
    count = 0
    for id_val in ids:
        idx = bisect.bisect_right(starts, id_val) - 1
        if idx >= 0 and id_val <= merged[idx][1]:
            count += 1
    return count


def part_b(data):
    ranges, _ = parse_data(data)
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)


def main():
    examples = [
        ("""3-5
10-14
16-20
12-18

1
5
8
11
17
32""", 3, 14)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()