from run_util import run_puzzle
import networkx

def parse_data(data):
    return [list(line) for line in data.splitlines()]


def create_reindeer_graph(data):
    maze = [list(line) for line in data.splitlines()]
    rows = len(maze)
    cols = len(maze[0])

    G = networkx.DiGraph()

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for d in range(4):
        dx, dy = directions[d]

        for x in range(rows):
            for y in range(cols):
                if maze[x][y] == '#':
                    continue

                node = (x, y, d)

                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[x][y] != '#':
                    G.add_edge(node, (nx, ny, d), weight=1)

                for turn, cost in [(1, 1000), (-1, 1000)]:
                    G.add_edge(node, (x, y, (d + turn) % 4), weight=cost)
    
    start = None
    ends = []
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 'S':
                start = (x, y, 0)
            if maze[x][y] == 'E':
                for d in range(4):
                    ends.append((x, y, d))

    return G, start, ends

def part_a(data):
    maze_graph, start, ends = create_reindeer_graph(data)

    shortest_path_length = 10**10
    for end in ends:
        path_length = networkx.shortest_path_length(maze_graph, source=start, target=end, weight='weight')
        shortest_path_length = min(shortest_path_length, path_length)

    return min(shortest_path_length, path_length)


def part_b(data):
    maze_graph, start, ends = create_reindeer_graph(data)

    tiles_in_paths = set()
    for end in ends:
        for path in networkx.all_shortest_paths(maze_graph, source=start, target=end, weight='weight'):
            for node in path:
                tiles_in_paths.add((node[0], node[1]))
                
    return len(tiles_in_paths)


def main():
    examples = [
        ("""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""", 7036, 45)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()