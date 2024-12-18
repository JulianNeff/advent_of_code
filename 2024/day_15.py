from run_util import run_puzzle

DIRECTIONS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

def parse_data(data, part_b=False):
    
    grid, instructions = data.split("\n\n")
    matrix = [list(line) for line in grid.splitlines()]
    instructions = instructions.replace("\n", "")

    if part_b:
        transform = {"#": "##", "O": "[]", ".": "..", "@": "@."}
        transformed_matrix = []

        for row in matrix:
            new_row = "".join(transform[tile] for tile in row)
            transformed_matrix.append(new_row)

        matrix = [list(row) for row in transformed_matrix]

    return matrix, instructions


def can_move_objects(grid, robot_x, robot_y, dx, dy):
    queue = [(robot_x, robot_y)]
    visited = set(queue)

    while queue:
        x, y = queue.pop(0)
        next_x, next_y = x + dx, y + dy

        if grid[next_x][next_y] == "#":
            return False, []
        if grid[next_x][next_y] in "O[]":
            if (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
            if grid[next_x][next_y] == "[" and (next_x, next_y + 1) not in visited:
                queue.append((next_x, next_y + 1))
                visited.add((next_x, next_y + 1))
            if grid[next_x][next_y] == "]" and (next_x, next_y - 1) not in visited:
                queue.append((next_x, next_y - 1))
                visited.add((next_x, next_y - 1))

    return True, visited


def update_grid(grid, to_move, dx, dy):
    new_grid = [row[:] for row in grid]
    for x, y in to_move:
        new_grid[x][y] = "."
    for x, y in to_move:
        new_grid[x + dx][y + dy] = grid[x][y]
    return new_grid


def solve(grid, instructions):
    rows, cols = len(grid), len(grid[0])
    robot_x, robot_y = next((i, j) for i in range(rows) for j in range(cols) if grid[i][j] == "@")

    for move in instructions:
        dx, dy = DIRECTIONS[move]
        can_move, to_move = can_move_objects(grid, robot_x, robot_y, dx, dy)

        if can_move:
            grid = update_grid(grid, to_move, dx, dy)
            robot_x, robot_y = robot_x + dx, robot_y + dy

    return sum(100 * i + j for i in range(rows) for j in range(cols) if grid[i][j] in "[O")


def part_a(data):
    matrix, instructions = parse_data(data, part_b=False)
    return solve(matrix, instructions)


def part_b(data):
    matrix, instructions = parse_data(data, part_b=True)
    return solve(matrix, instructions)
    

def main():
    examples = [
        ("""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""", 2028, None), ("""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
""", None, 105 + 207 + 306), ("""##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""", 10092, 9021)]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()