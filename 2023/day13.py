from run_util import run_puzzle

def transpose(puzzle):
    return [''.join(row[i] for row in puzzle) for i in range(len(puzzle[0]))]


def find_reflection(puzzle, smudge):
    puzzle_len = len(puzzle)
    for i in range(puzzle_len - 1):
        fail = 0
        for j in range(puzzle_len):
            compare_row = puzzle[j]
            mirror_row_idx = i + 1 + (i - j)
            if 0 <= mirror_row_idx < puzzle_len:
                mirror_row = puzzle[mirror_row_idx]
                fail += sum(1 for k in range(len(compare_row)) if compare_row[k] != mirror_row[k])
                if fail > smudge:
                    break
        if fail == smudge:
            return i + 1
    return 0


def solve(data, part_a):
    puzzles = data.split('\n\n')

    result = 0
    smudge = 0 if part_a else 2
    for puzzle in puzzles:
        rows = puzzle.splitlines()
        res_rows = find_reflection(rows, smudge)
        if res_rows > 0:
            result += res_rows * 100
        else:
            result += find_reflection(transpose(rows), smudge)

    return result


def part_a(data):
    return solve(data, True)

def part_b(data):
    return solve(data, False)


def main():
    examples = [
        ("""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""", 405, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()