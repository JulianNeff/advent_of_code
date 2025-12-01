from run_util import run_puzzle


def parse_data(data):
    return [(line[0], int(line[1:])) for line in data.strip().split("\n")]


def solve(data, count_crossings):
    moves = parse_data(data)
    position = 50
    count = 0

    for direction, distance in moves:
        count, position = count_crossings(count, position, direction, distance)

    return count


def count_a(count, position, direction, distance):
    step = -1 if direction == "L" else 1
    position = (position + step * distance) % 100
    return count + (position == 0), position


def count_b(count, position, direction, distance):
    count += distance // 100
    distance %= 100

    if direction == "L":
        crossed = 0 < position <= distance
        position = (position - distance) % 100
    else:
        crossed = position + distance >= 100
        position = (position + distance) % 100
    
    count += crossed

    return count, position


def part_a(data):
    return solve(data, count_a)


def part_b(data):
    return solve(data, count_b)


def main():
    examples = [
        (
            """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""",
            3,
            6,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()