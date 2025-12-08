from run_util import run_puzzle
from collections import defaultdict


def parse_data(data: str):
    coords = [tuple(map(int, line.split(','))) for line in data.splitlines()]
    distances = get_distances(coords)
    nr_coords = len(coords)
    union_find = list(range(nr_coords))
    return coords, distances, nr_coords, union_find


def get_distances(coords):
    distances = []
    for i, (x1, y1, z1) in enumerate(coords):
        for j in range(i + 1, len(coords)):
            x2, y2, z2 = coords[j]
            dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((dist_sq, i, j))
    
    return sorted(distances)


def find(parent: list, x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: list, x: int, y: int) -> None:
    px, py = find(parent, x), find(parent, y)
    if px != py:
        parent[px] = py


def part_a(data: str) -> int:
    coords, distances, nr_coords, union_find = parse_data(data)
    iterations = 10 if nr_coords == 20 else 1000

    for i in range(iterations):
        _, x, y = distances[i]
        union(union_find, x, y)

    roots = [find(union_find, i) for i in range(nr_coords)]
    team_sizes = sorted(defaultdict(int, ((r, roots.count(r)) for r in set(roots))).values())
    
    return team_sizes[-1] * team_sizes[-2] * team_sizes[-3]


def part_b(data: str) -> int:
    coords, distances, nr_coords, union_find = parse_data(data)
    connections = 0

    for dist_sq, x, y in distances:
        px, py = find(union_find, x), find(union_find, y)
        if px != py:
            connections += 1
            if connections == nr_coords - 1:
                return coords[x][0] * coords[y][0]
            union_find[px] = py

    return -1


def main():
    examples = [
        ("""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""", 40, 25272)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()