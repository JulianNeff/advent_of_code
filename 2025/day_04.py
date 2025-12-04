from run_util import run_puzzle

def parse_data(data):
    data = data.splitlines()
    matrix = []
    for line in data:
        row = []
        for char in line:
            if char == '@':
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    return matrix


def count_adjacent_ones(matrix, row, col):
    count = 0
    for i in range(max(0, row-1), min(len(matrix), row+2)):
        for j in range(max(0, col-1), min(len(matrix[0]), col+2)):
            if (i != row or j != col) and matrix[i][j] == 1:
                count += 1    
    return count


def can_be_removed(matrix, row, col):
    to_remove = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 1:
                if count_adjacent_ones(matrix, i, j) < 4:
                    to_remove.append((i, j))
    return to_remove


def part_a(data):
    matrix = parse_data(data)   
    return len(can_be_removed(matrix, 0, 0))


def part_b(data):
    matrix = parse_data(data)

    count = 0
    changed = True
    while changed:
        changed = False
        to_remove = can_be_removed(matrix, 0, 0)
        if to_remove:
            changed = True
            count += len(to_remove)

        for i, j in to_remove:  
            matrix[i][j] = 0
    return count


def print_matrix(matrix):  
    for row in matrix:
        print("".join(['@' if cell == 1 else '.' for cell in row]))
    print()


def main():
    examples = [
        ("""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""", 13, 43)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()