from run_util import run_puzzle
import numpy as np


def read_input(data: str) -> np.ndarray:
    mapping = {'.' : 0, 'O' : 1, '#' : 2}
    rows = data.splitlines()
    converted = [[mapping.get(c, 0) for c in line] for line in rows]
    return np.array(converted)


def calculate_weight(grid: np.ndarray) -> int:
    total_weight = 0
    rows, columns = grid.shape
    
    for row_index in range(rows):
        for col_index in range(columns):
            if grid[row_index, col_index] == 1:
                total_weight += rows - row_index
    
    return total_weight


def tilt(grid: np.ndarray) -> np.ndarray:
    rows, cols = grid.shape
    next_free = [0 for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:
                grid[i, j] = 0
                grid[next_free[j], j] = 1
                next_free[j] += 1
            elif grid[i, j] == 2:
                next_free[j] = i + 1

    return grid

def iterate(grid: np.ndarray, nr_iterations: int) -> np.ndarray:
    for _ in range(4 * nr_iterations):
        grid = tilt(grid)
        grid = np.rot90(grid, k=-1)
    return grid


def part_a(data):
    grid = read_input(data)
    tilt(grid)
    return calculate_weight(grid)


def part_b(data):
    grid = read_input(data)
    iterations = 1000000000
    grid_history = {}

    for i in range(iterations):
        grid_tuple = tuple(map(tuple, grid))

        if grid_tuple in grid_history:
            remaining_iterations = (iterations - i) % (i - grid_history[grid_tuple])
            grid = iterate(grid, remaining_iterations)
            break

        grid_history[grid_tuple] = i
        grid = iterate(grid, 1)

    return calculate_weight(grid)


def main():
    examples = [
        ("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""", 136, 64)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()