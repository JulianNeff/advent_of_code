from run_util import run_puzzle
import heapq

def parse_input(data: str) -> list[list[int]]:
    return [[int(i) for i in line] for line in data.split('\n')]


def dijkstra(grid: list[list[int]], low: int, high: int) -> int:
    goal = (len(grid) - 1, len(grid[0]) - 1)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def in_range(x, y):
        return 0 <= x <= goal[0] and 0 <= y <= goal[1]

    visited = set()
    costs = {}

    queue = [(0, 0, 0, -1)]
    while queue:
        c, x, y, d = heapq.heappop(queue)

        if (x, y) == goal:
            return c
        
        if (x, y, d) in visited:
            continue

        for i, (dx, dy) in enumerate(dirs):
            if i == d or (i + 2) % 4 == d:
                continue

            dc = 0
            for dst in range(high):
                nx = x + dx * (dst + 1)
                ny = y + dy * (dst + 1)

                if not in_range(nx, ny):
                    continue

                dc += grid[nx][ny]
                nc = c + dc
                
                if (dst + 1) < low or costs.get((nx, ny, i), int(1e6)) <= nc:
                    continue

                costs[(nx, ny, i)] = nc
                heapq.heappush(queue, (nc, nx, ny, i))


def part_a(data: str) -> int:
    grid = parse_input(data)
    return dijkstra(grid, 1, 3)


def part_b(data: str) -> int: 
    grid = parse_input(data)
    return dijkstra(grid, 4, 10)


def main():
    examples = [
        ("""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""", 102, 94)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()