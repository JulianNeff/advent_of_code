from run_util import run_puzzle

def parse_data(data):
    grid = [[int(char) for char in line] for line in data.split("\n")]
    starting_points = [(i, j) for i, row in enumerate(grid) for j, entry in enumerate(row) if entry == 0]
    return grid, starting_points

def dfs_a(x, y, i, grid, rows, cols, reachable):
    if i == 9:
        reachable.add((x, y))
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == i + 1): 
            dfs_a(nx, ny, i + 1, grid, rows, cols, reachable)

def part_a(data):
    grid, starting_points = parse_data(data)

    total_score = 0
    for x, y in starting_points:
        reachable = set()
        dfs_b(x, y, 0, grid, len(grid), len(grid[0]), reachable)
        total_score += len(reachable)
    return total_score


def dfs_b(x, y, i, grid, rows, cols):
    if i == 9:
        return 1
    score = 0
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == i + 1): 
            score += dfs_b(nx, ny, i + 1, grid, rows, cols)
    return score

def part_b(data):
    grid, starting_points = parse_data(data)
    total_score = 0
    for x, y in starting_points:
        total_score += dfs_b(x, y, 0, grid, len(grid), len(grid[0]))
    return total_score


def main():
    examples = [
        ("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""", 36, 81)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()