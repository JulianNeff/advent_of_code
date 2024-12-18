from run_util import run_puzzle
from collections import deque

direction = {
    "N": {".": "N", "-": "EW", "|": "N", "/": "E", "\\": "W"},
    "E": {".": "E", "-": "E", "|": "NS", "/": "N", "\\": "S"},
    "S": {".": "S", "-": "EW", "|": "S", "/": "W", "\\": "E"},
    "W": {".": "W", "-": "W", "|": "NS", "/": "S", "\\": "N"},
}

change = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}


def get_lines(data):
    return [list(line) for line in data.split('\n')]


def solve(matrix, start):
    side_length = len(matrix)

    queue = deque([start])
    visited = set([start])

    while queue:
        i, j, d = queue.popleft()
        di, dj = change[d]

        if  0 <= i + di < side_length and 0 <= j + dj < side_length:
            for nd in direction[d][matrix[i + di][j + dj]]:
                next_pos = (i + di, j + dj, nd)
                if next_pos not in visited:
                    visited.add((next_pos))
                    queue.append(next_pos)

    return len({(i, j) for i, j, _ in visited}) - 1


def generate_starts(side):
    starts = []
    for i in range(side):
        starts.extend([(i, -1, 'E'), (i, side, 'W'), (-1, i, 'S'), (side, i, 'N')])
    return starts


def part_a(data):
    lines = get_lines(data)

    start = (0, -1, "E")
    
    return solve(lines, start)


def part_b(data):
    lines = get_lines(data)

    side_length = len(lines)
    starts = generate_starts(side_length)

    return max(solve(lines, start) for start in starts)


def main():
    examples = [
        (""".|...\....
|.-.\.....
.....|-...
........|.
..........
........./
..../.\\\\..
.-.-/..|..
.|....-|./
..//.|....""", 46, 51)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()