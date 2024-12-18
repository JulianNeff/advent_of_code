from run_util import run_puzzle

def parse_data(data):
    return [list(line) for line in data.splitlines() if line]

def part_a(data):
    matrix = parse_data(data)
    length = range(len(matrix))
    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for row in length:
        for col in length:
            for d_row, d_col in directions:
                if 0 <= row + 3 * d_row < len(matrix) and 0 <= col + 3 * d_col < len(matrix[0]):
                    if matrix[row][col] == 'X' and matrix[row + d_row][col + d_col] == 'M' and matrix[row + 2 * d_row][col + 2 * d_col] == 'A' and matrix[row + 3 * d_row][col + 3 * d_col] == 'S':
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