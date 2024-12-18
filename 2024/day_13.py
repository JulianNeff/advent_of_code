import numpy as np
from run_util import run_puzzle

def parse_data(data):
    out = []
    for block in data.strip().split("\n\n"):
        lines = block.splitlines()
        buttons = []
        prize = None

        for line in lines:
            if line.startswith("Button"):
                x, y = map(int, line.split(":")[1].strip().replace("X+", "").replace("Y+", "").split(", "))
                buttons.append((x, y))
            elif line.startswith("Prize"):
                prize = tuple(map(int, line.split(":")[1].strip().replace("X=", "").replace("Y=", "").split(", ")))

        out.append((buttons, prize))
    return out

def solve(data, part_b):
    data = parse_data(data)
    error = 10**13 if part_b else 0
    score = 0

    for buttons, (px, py) in data:
        ax, ay = buttons[0]
        bx, by = buttons[1]

        a = np.array([[ax, bx], [ay, by]])
        b = np.array([px + error, py + error])
        r = np.linalg.solve(a, b).round()
        
        if np.all(np.dot(a, r) == b):
            score += int(3 * r[0] + 1 * r[1])

    return score

def part_a(data):
    return solve(data, part_b=False)


def part_b(data):
    return solve(data, part_b=True)

def main():
    examples = [
        ("""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""", 480, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
