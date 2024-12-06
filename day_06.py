from run_util import run_puzzle

DIR = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}   

def parse_data(data):
    lines = data.splitlines()
    rows, cols = len(lines), len(lines[0])
    
    start = None
    obstacles = []
    for i, line in enumerate(lines):
        for j, entry in enumerate(line):
            if entry == "#":
                obstacles.append((i, j))
            elif entry == '^':
                start = (i, j)
    return start, obstacles, rows, cols


def part_a(data):
    start, obstacles, rows, cols = parse_data(data)

    visited = {start}
    direction = 0
    curr = start

    while True:
        next_pos = (curr[0] + DIR[direction][0], curr[1] + DIR[direction][1])

        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        if next_pos in obstacles:
            direction = (direction + 1) % 4
        else:
            curr = next_pos
            visited.add(curr)
    return len(visited)

def simulate(new_obstacle, obstacles, start, rows, cols):
        current_obstacles = set(obstacles)
        current_obstacles.add(new_obstacle)
        
        visited = set()  
        direction = 0  
        curr = start    
        state_set = set()

        while True:
            state = (curr, direction)
            if state in state_set:
                return True
            state_set.add(state)

            next_pos = (curr[0] + DIR[direction][0], curr[1] + DIR[direction][1])

            if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                break

            if next_pos in current_obstacles:
                direction = (direction + 1) % 4
            else:
                visited.add(next_pos)
                curr = next_pos

        return False


def part_b(data):
    start, obstacles, rows, cols = parse_data(data)

    valid_positions = 0
    for r in range(rows):
        for c in range(cols):
            new_obstacle = (r, c)
            if new_obstacle == start or new_obstacle in obstacles:
                continue
            if simulate(new_obstacle, obstacles, start, rows, cols):
                valid_positions += 1

    return valid_positions


def main():
    examples = [
        ("""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""", 41, 6)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()