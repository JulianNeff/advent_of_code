from run_util import run_puzzle


def parse_data(data):
    locks, keys = [], []

    for schematic in data.strip().split("\n\n"):
        rows = schematic.splitlines()
        if rows[0][0] == "#":
            locks.append([sum(1 for cell in col if cell == "#") for col in zip(*rows)])
        elif rows[-1][0] == "#":
            keys.append([sum(1 for cell in col[::-1] if cell == "#") for col in zip(*rows)])

    return locks, keys


def part_a(data):
    locks, keys = parse_data(data)
    return sum(all(x + y <= 7 for x, y in zip(lock, key)) for lock in locks for key in keys)


def part_b(data):
    data = parse_data(data)
    return None


def main():
    examples = [
        ("""#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""", 3, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()