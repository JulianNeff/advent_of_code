from run_util import run_puzzle

import numpy as np

def find_wins(time, distance):
    roots = np.roots([1, -time, distance])
    low, high = min(roots), max(roots)
    if high > int(high):
        return int(high) - int(low)
    else:
        return int(high) - int(low) - 1

def part_a(data):
    lines = data.splitlines()
    time = [int(x) for x in lines[0].split(':')[1].split()]
    distance = [int(x) for x in lines[1].split(':')[1].split()]
    races = list(zip(time, distance))
    return np.prod([find_wins(time, dist) for time, dist in races])

def part_b(data):
    lines = data.splitlines()
    time = int(''.join([x for x in lines[0].split(':')[1].split()]))
    distance = int(''.join([x for x in lines[1].split(':')[1].split()]))
    return find_wins(time, distance)


def main():
    examples = [
        ("""Time:      7  15   30
Distance:  9  40  200""", 288, 71503)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()