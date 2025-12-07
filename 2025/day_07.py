from run_util import run_puzzle


def parse_data(data):
    return data.strip().split('\n')


def part_a(data):
    lines = parse_data(data)
    count = 0
    streams = set(line.index('S') for line in lines if 'S' in line)

    for _, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == '^' and c in streams:
                count += 1
                streams.remove(c)
                streams.add(c - 1)
                streams.add(c + 1)
    return count


def part_b(data):
    lines = parse_data(data)
    timelines = [1] * len(lines[0])
    
    for row in reversed(lines):
        for col in range(len(lines[0])):
            if row[col] == '^':
                timelines[col] = timelines[col - 1] + timelines[col + 1]
    
    return timelines[lines[0].index('S')]


def main():
    examples = [
        (""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""", 21, 40)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()