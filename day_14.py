import re
from run_util import run_puzzle
from PIL import Image

HEIGHT = 103
WIDTH = 101


def parse_data(data):
    p, v = [], []

    for line in data.strip().split("\n"):
        p_match = re.search(r"p=(-?\d+),(-?\d+)", line)
        v_match = re.search(r"v=(-?\d+),(-?\d+)", line)

        if p_match and v_match:
            p.append((int(p_match.group(1)), int(p_match.group(2))))
            v.append((int(v_match.group(1)), int(v_match.group(2))))

    return p, v


def update_pos(p, v):
    return ((p[0] + v[0]) % WIDTH, (p[1] + v[1]) % HEIGHT)


def part_a(data):
    p, v = parse_data(data)

    for _ in range(100):
        p = [update_pos(pos, vel) for pos, vel in zip(p, v)]

    counts = {"top_left": 0, "top_right": 0, "bottom_left": 0, "bottom_right": 0}

    for px, py in p:
        region = ("top_" if py < HEIGHT // 2 else "bottom_") + ("left" if px < WIDTH // 2 else "right")
        counts[region] += 1

    return counts["top_left"] * counts["top_right"] * counts["bottom_left"] * counts["bottom_right"]


def part_b(data):
    p, v = parse_data(data)

    for j in range(10**100):
        for i in range(len(p)):
            p[i] = update_pos(p[i], v[i])
        
        if len(p) == len(set(p)):
                return j + 1
        
    return None


def main():
    examples = [
        ("""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""", None, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()