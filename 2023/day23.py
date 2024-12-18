from run_util import run_puzzle


def find_longest_path(edges, n, m, part_a):
    q = [(0, 1, 0)]
    visited = set()
    best = 0

    while q:
        x, y, d = q.pop()
        if d == -1:
            visited.remove((x, y))
            continue
        if (x, y) == (n - 1, m - 2):
            best = max(best, d)
            continue
        if (x, y) in visited:
            continue
        visited.add((x, y))
        q.append((x, y, -1))
        if part_a:
            for ax, ay in edges.get((x, y), []):
                q.append((ax, ay, d + 1))
        else:
            for ax, ay, l in edges[(x, y)]:
                q.append((ax, ay, d + l))
    return best


def part_a(data):
    grid = data.splitlines()
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    edges = {}

    for x in range(n):
        for y in range(m):
            if grid[x][y] == ".":
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == ".":
                        edges.setdefault((x, y), set()).add((new_x, new_y))
                        edges.setdefault((new_x, new_y), set()).add((x, y))

            if grid[x][y] == ">":
                edges.setdefault((x, y), set()).add((x, y + 1))
                edges.setdefault((x, y - 1), set()).add((x, y))
            
            if grid[x][y] == "v":
                edges.setdefault((x, y), set()).add((x + 1, y))
                edges.setdefault((x - 1, y), set()).add((x, y))

    return find_longest_path(edges, n, m, True)


def merge_edges(edges):
    while True:
        for x, y in edges.items():
            if len(y) == 2:
                a, b = y
                edges[a[:2]].remove(x + (a[2],))
                edges[b[:2]].remove(x + (b[2],))
                edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
                edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
                del edges[x]
                break
        else:
            break


def part_b(data):
    grid = data.splitlines()
    n, m = len(grid), len(grid[0])

    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    edges = {}

    for x in range(n):
        for y in range(m):
            if grid[x][y] in ".>v":
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] != "#":
                        edges.setdefault((x, y), set()).add((new_x, new_y, 1))
                        edges.setdefault((new_x, new_y), set()).add((x, y, 1))

    merge_edges(edges)
    return find_longest_path(edges, n, m, False)

def main():
    examples = [
        ("""#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""", 94, 154)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()