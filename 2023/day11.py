from run_util import run_puzzle


def solve(data: str, dist: int) -> int:
    lines = data.splitlines()

    galaxies = [(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == '#']

    empty_rows = [i for i, line in enumerate(lines) if line.strip() == '.' * len(line)]

    empty_cols = [i for i in range(len(lines[0])) if all(line[i] == '.' for line in lines)]

    new_galaxies = []
    for galaxy in galaxies:
        new_i = galaxy[0] + sum(dist for row in empty_rows if row < galaxy[0])
        new_j = galaxy[1] + sum(dist for col in empty_cols if col < galaxy[1])
        new_galaxies.append((new_i, new_j))

    return sum(abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for idx, g1 in enumerate(new_galaxies) for g2 in new_galaxies[idx + 1:])


def part_a(data):
    return solve(data, 1)


def part_b(data):
    return solve(data, 999999)

def main():
    examples = [
        ("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""", 374, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()