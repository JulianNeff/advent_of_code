from run_util import run_puzzle
from collections import defaultdict, Counter

def blink(stones, count):
    for _ in range(count):
        new_stones = defaultdict(int)
        for stone in stones:
            length = len(str(stone))
            if stone == 0:
                new_stones[1] += stones[stone]
            elif length % 2 == 0:
                new_stones[int(str(stone)[length // 2:])] += stones[stone]
                new_stones[int(str(stone)[:length // 2])] += stones[stone]
            else:
                new_stones[stone * 2024] += stones[stone]
        stones = new_stones
    return sum(stones.values())


def parse_data(data):
    return defaultdict(int, Counter(int(i) for i in data.split()))


def part_a(data):
    return blink(parse_data(data), 25)


def part_b(data):
    return blink(parse_data(data), 75)


def main():
    examples = [
        ("""125 17""", 55312, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()