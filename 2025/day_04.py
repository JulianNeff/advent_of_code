from run_util import run_puzzle
import numpy as np
from scipy.signal import convolve2d

def parse_data(data):
    grid = np.array([[*x.strip()] for x in data.splitlines()]) == '@'
    return grid, grid.copy()


def solve(data, iterations):
    grid, orig = parse_data(data)
    
    for i in range(101):
        grid &= convolve2d(grid, np.ones((3,3)), mode='same') > 4
        if i == iterations:
            return orig.sum() - grid.sum()


def part_a(data):
    return solve(data, 0)


def part_b(data):
    return solve(data, 100)


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