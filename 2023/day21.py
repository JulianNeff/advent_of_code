from run_util import run_puzzle


def part_a(data):
    grid = data.split("\n")
    s = len(grid) // 2

    queue = [(s, s, 0)]
    visited = set()
    plots = 0

    queue = [(s, s, 0)]
    visited = set()
    plots = 0

    while queue:
        x, y, steps = queue.pop(0)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if grid[x][y] != "#":
            if steps % 2 == 0:
                plots += 1

            if steps == 64:
                continue
            
            if x + 1 < len(grid):
                queue.append((x + 1, y, steps + 1))

            if x > 0:
                queue.append((x - 1, y, steps + 1))

            if y + 1 < len(grid):
                queue.append((x, y + 1, steps + 1))

            if y > 0:
                queue.append((x, y - 1, steps + 1))

    return plots


def update_position(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def modulo_position(pos, size):
    return (pos[0] % size, pos[1] % size)


def part_b(data):
    grid = data.split('\n')
    grid_size = len(grid)

    traversable = {(i, j) for i in range(grid_size) for j in range(grid_size) if grid[i][j] in '.S'}
    start = next((i, j) for i in range(grid_size) for j in range(grid_size) if grid[i][j] == 'S')
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited_positions, new_positions, position_cache = {start}, {start}, {0: 1}
    k, remainder = divmod(26501365, grid_size)

    for step in range(1, remainder + 2 * grid_size + 1):
        visited_positions, new_positions = new_positions, {
            new_pos for pos in new_positions for direction in directions
            for new_pos in [update_position(pos, direction)]
            if new_pos not in visited_positions and modulo_position(new_pos, grid_size) in traversable
        }
        position_cache[step] = len(new_positions) + (position_cache[step - 2] if step > 1 else 0)

    additional_distance = position_cache[remainder + 2 * grid_size] + position_cache[remainder] - 2 * position_cache[remainder + grid_size]
    accumulated_distance = position_cache[remainder + 2 * grid_size] - position_cache[remainder + grid_size]
    return position_cache[remainder + 2 * grid_size] + (k - 2) * (2 * accumulated_distance + (k - 1) * additional_distance) // 2


def main():
    examples = [
        ("""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""", None, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()