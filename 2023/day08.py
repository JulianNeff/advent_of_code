import math
from run_util import run_puzzle

def parse_input(data: str) -> list[tuple[str, int]]:
    lines = data.splitlines()
    sequence = lines[0]
    left = {}
    right = {}
    start = []

    for line in lines[2:]:
        key, value = line.split(' = ')
        left[key], right[key] = value[1:-1].split(', ')
        if key.endswith("A"):
            start.append(key)

    return sequence, start, left, right


def part_a(data):
    seq, _, left, right = parse_input(data)
    curr = "AAA"
    count = 0
    while curr != "ZZZ":
        for c in seq:
            count = count + 1
            if c == 'L':
                curr = left[curr]
            elif c == 'R':
                curr = right[curr]

    return count


def part_b(data):
    seq, curr, left, right = parse_input(data)
    count = 0

    nodes_ending = [0 for _ in range(len(curr))]
    while 0 in nodes_ending:
        for i, c in enumerate(seq):
            for j, ghost in enumerate(curr):
                if c == "L":
                    curr[j] = left[ghost]
                elif c == "R":
                    curr[j] = right[ghost]
        print(nodes_ending)
        count += len(seq)
        for i, ghost in enumerate(curr):
            
            if ghost.endswith("Z"):
                nodes_ending[i] = count

    return math.lcm(*nodes_ending)


def main():
    examples = [
        ("""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""", 6, None), 
        ("""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""", None, 6)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()