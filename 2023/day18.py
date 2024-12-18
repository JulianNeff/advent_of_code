from run_util import run_puzzle

def solve(lines: list[tuple[str, int]]) -> int:
    edges = []

    border = 0
    curr = (0, 0)
    for d, l in lines:
        curr = (curr[0] + d[0] * l, curr[1] + d[1] * l)
        edges.append(curr)
        border += l

    area = 0
    for i in range(len(edges) - 1):
        area += edges[i][0] * edges[i + 1][1] - edges[i + 1][0] * edges[i][1]

    return (abs(area) + border) // 2 + 1


def part_a(data):
    dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    lines = [(dirs[d], int(l)) for d, l, _ in [line.split(' ') for line in data.split('\n')]]

    return solve(lines)


def part_b(data):
    lines = data.split('\n')
    dirs = {"0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}

    new_lines = []
    for line in lines:
        _, _, color = line.split(' ')
        new_lines.append((dirs[color[7]], int(color[2:7], 16)))

    return solve(new_lines)


def main():
    examples = [
        ("""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""", 62, 952408144115)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()