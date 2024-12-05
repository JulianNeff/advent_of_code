# Copyright: https://github.com/michaelerne/adventofcode-2024/blob/main/template.py

from run_util import run_puzzle

def parse_data(data):
    matrix = [list(line) for line in data.split("\n") if line.strip()]
    return matrix

def part_a(data):
    matrix = parse_data(data)
    length = range(len(matrix))
    count = 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for y in length:
        for x in length:
            for dy, dx in dirs:
                if 0 <= y + 3*dy < len(matrix) and 0 <= x + 3*dx < len(matrix):
                    if matrix[y][x] == 'X' and matrix[y + dy][x + dx] == 'M' and matrix[y + 2 * dy][x + 2 * dx] == 'A' and matrix[y + 3 * dy][x + 3 * dx] == 'S':
                        count += 1
    return count


def part_b(data):
    matrix = parse_data(data)
    count = 0
    length = range(len(matrix))
    for y in length:
        for x in length:
            if matrix[y][x] == 'M':
                if y + 2 < len(matrix) and x + 2 < len(matrix[0]):
                    if matrix[y+1][x+1] == 'A' and matrix[y+2][x+2] == 'S':
                        if (matrix[y+2][x] == 'M' and matrix[y][x+2] == 'S') or (matrix[y+2][x] == 'S' and matrix[y][x+2] == 'M'):
                            count += 1
            if matrix[y][x] == 'S':
                if y + 2 < len(matrix) and x + 2 < len(matrix[0]):
                    if matrix[y+1][x+1] == 'A' and matrix[y+2][x+2] == 'M':
                        if (matrix[y+2][x] == 'M' and matrix[y][x+2] == 'S') or (matrix[y+2][x] == 'S' and matrix[y][x+2] == 'M'):
                            count += 1
    return count


def main():
    examples = [
        ("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""", 18, 9)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()