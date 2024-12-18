from run_util import run_puzzle

TYPES = {"|": ["n", "s"], "-": ["w", "e"], "L": ["n", "e"], "J": ["n", "w"], "7": ["s", "w"], "F": ["s", "e"], 'S': ["n", "s", "w", "e"]}
DIRS = {"n": (-1, 0, "s"),  "w": (0, -1, "e"), "s": (1, 0, "n"), "e": (0, 1, "w")}

def bfs(matrix, start):
    visited = dict()

    queue = [(start, 0)]
    while queue:
        (i, j), dist = queue.pop(0)

        if (i, j) in visited:
            continue

        visited[(i, j)] = dist
        for curr_dir in TYPES[matrix[i][j]]:
            c_i, c_j, opp = DIRS[curr_dir]
            new_i, new_j, new_d = i + c_i, j + c_j, dist + 1
            if (0 <= new_i) and (new_i < len(matrix)) and (0 <= new_j) and (new_j < len(matrix[new_i])):
                tar = matrix[new_i][new_j]
                if tar in TYPES and opp in TYPES[tar]:
                    queue.append(((new_i, new_j), new_d))

    return visited


def part_a(data):
    lines = data.splitlines()

    matrix = [[c for c in line.strip()] for line in lines]
    start = [(i, j) for i, line in enumerate(matrix) for j, c in enumerate(line) if c == 'S'][0]
    visited = bfs(matrix, start)

    return max(visited.values())

def find_reachable_from_start(matrix, start, visited):
    reachable = []
    for curr_dir in DIRS:
        c_i, c_j, opp = DIRS[curr_dir]
        new_i, new_j = start[0] + c_i, start[1] + c_j

        in_bounds = 0 <= new_i and new_i < len(matrix) and 0 <= new_j and new_j < len(matrix[new_i])
        if (new_i, new_j) in visited and in_bounds:
            target = matrix[new_i][new_j]

            if target in TYPES and opp in TYPES[target]:
                reachable.append(curr_dir)
    return reachable


def part_b(data):
    lines = data.splitlines()

    matrix = [[c for c in line.strip()] for line in lines]
    start = [(i, j) for i, line in enumerate(matrix) for j, c in enumerate(line) if c == 'S'][0]

    visited = bfs(matrix, start)
    
    reachable = find_reachable_from_start(matrix, start, visited)

    for t in TYPES:
        if len(reachable) == len(TYPES[t]) and all([r in TYPES[t] for r in reachable]):
            matrix[start[0]][start[1]] =  t

    for i in range(len(matrix)):
        n = 0
        for j in range(len(matrix[i])):
            if (i,j) in visited:
                if "n" in TYPES[matrix[i][j]]:
                    n += 1
                continue

            matrix[i][j] = "O" if n % 2 == 0 else "I"

    count_i = "\n".join(["".join(line) for line in matrix]).count("I")
    return count_i


def main():
    examples = [
        (""".....
.S-7.
.|.|.
.L-J.
.....""", 4, None),
("""..F7.
.FJ|.
SJ.L7
|F--J
LJ...""", 8, None),
("""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""", None, 4),
(""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""", None, 8)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()