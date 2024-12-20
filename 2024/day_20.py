from collections import deque
from run_util import run_puzzle


def parse_data(data):
    matrix = [list(row) for row in data.split('\n')]
    start = next((i, j) for i, row in enumerate(matrix) for j, cell in enumerate(row) if cell == 'S')
    return matrix, start


def bfs(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    dist = [[-1] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist


def part_a(data):
    matrix, start = parse_data(data)
    start_matrix = bfs(matrix, start)
    rows, cols = len(matrix), len(matrix[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i][j] == '#':
                if (matrix[i-1][j] != '#' and matrix[i+1][j] != '#') or (matrix[i][j-1] != '#' and matrix[i][j+1] != '#'):
                    time_saved = abs(start_matrix[i-1][j] - start_matrix[i+1][j]) - 2 if matrix[i-1][j] != '#' and matrix[i+1][j] != '#' else abs(start_matrix[i][j-1] - start_matrix[i][j+1]) - 2
                    if time_saved >= 100:
                        count += 1

    return count


def part_b(data):
    matrix, start = parse_data(data)
    start_matrix = bfs(matrix, start)
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    directions = [(dx, dy) for dx in range(-20, 21) for dy in range(-20, 21) if abs(dx) + abs(dy) <= 20]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '#' or start_matrix[i][j] == -1:
                continue

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != '#' and start_matrix[ni][nj] != -1:
                    cheat = start_matrix[i][j] - start_matrix[ni][nj] - abs(dx) - abs(dy)
                    if cheat >= 100:
                        count += 1

    return count


def main():
    examples = [
        ("""###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""", None, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
