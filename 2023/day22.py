from collections import defaultdict
from run_util import run_puzzle


def parse_bricks(data):
    lines = [tuple(list(map(int, p.split(','))) for p in line.split('~')) for line in data.splitlines()]
    lines.sort(key=lambda x: x[0][2])  # Sort by z value
    return lines


def update_brick(brick, max_height):
    brick[1][2] -= brick[0][2] - max_height
    brick[0][2] -= brick[0][2] - max_height


def process_bricks(bricks, part_a=False):
    nr_bricks = len(bricks)
    current_z = defaultdict(lambda: (0, -1))
    graph = [[] for _ in range(nr_bricks)]
    disintegrated = set()

    for i, brick in enumerate(bricks):
        max_height = -1
        updates = set()

        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                if current_z[x, y][0] + 1 == max_height:
                    updates.add(current_z[x, y][1])
                elif current_z[x, y][0] + 1 > max_height:
                    max_height = current_z[x, y][0] + 1
                    updates = {current_z[x, y][1]}

        for update in updates:
            if update != -1:
                graph[update].append(i)

        if len(updates) < 2:
            disintegrated.add(updates.pop())

        update_brick(brick, max_height)
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                current_z[x, y] = (brick[1][2], i)

    if part_a:
        return nr_bricks - len(disintegrated) + 1
    else:        
        other_bricks = 0
        for i in range(nr_bricks):
            in_degree = [0 for _ in range(nr_bricks)]
            for j in range(nr_bricks):
                for k in graph[j]:
                    in_degree[k] += 1

            queue = [i]
            other_bricks -= 1
            while queue:
                other_bricks += 1
                x = queue.pop()
                for j in graph[x]:
                    in_degree[j] -= 1
                    if in_degree[j] == 0:
                        queue.append(j)

        return other_bricks


def part_a(data):
    bricks = parse_bricks(data)
    return process_bricks(bricks, part_a=True)


def part_b(data):
    bricks = parse_bricks(data)
    return process_bricks(bricks, part_a=False)


def main():
    examples = [
        ("""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""", 5, 7)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()