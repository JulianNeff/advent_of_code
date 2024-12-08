from run_util import run_puzzle

def parse_data(data):
    mapping = {}
    lines = data.strip().split("\n")
    rows, cols = len(lines), len(lines[0])
    for y, line in enumerate(data.strip().split("\n")):
        for x, char in enumerate(line):
            if char != ".":
                mapping.setdefault(char, []).append((y, x))
    return {k: v for k, v in mapping.items() if len(v) > 1}, rows, cols

def solve(data, is_part_b):
    mapping, rows, cols = parse_data(data)
    points = set()
    for _, coords in mapping.items():
        if is_part_b:
            points.update(coords)
        for i, (a1, a2) in enumerate(coords):
            for b1, b2 in coords[i+1:]:
                dy, dx = b1 - a1, b2 - a2
               
                y, x = b1 + dy, b2 + dx
                while 0 <= y < rows and 0 <= x < cols:
                    points.add((y, x))
                    if not is_part_b:
                        break
                    y, x = y + dy, x + dx

                y, x = a1 - dy, a2 - dx
                while 0 <= y < rows and 0 <= x < cols:
                    points.add((y, x))
                    if not is_part_b:
                        break
                    y, x = y - dy, x - dx
    return len(points)

def part_a(data):
    return solve(data=data, is_part_b=False)

def part_b(data):
    return solve(data=data, is_part_b=True)


def main():
    examples = [
        ("""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""", 14, 34)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()