from run_util import run_puzzle


def parse_data(data):
    lines = data.strip().split("\n")
    moves = [(line[0], int(line[1:])) for line in lines]
    return moves


def part_a(data):
    moves = parse_data(data)
    position = 50
    count = 0

    for direction, distance in moves:
        if direction == "L":
            position -= distance
        else:
            position += distance

        position %= 100
        if position == 0:
            count += 1

    return count


def part_b(data):
    moves = parse_data(data)
    position = 50
    count = 0

    for direction, distance in moves:        
        count += distance // 100
        distance %= 100

        if distance == 0:
            continue

        if direction == "L":
            if 0 < position <= distance:
                count += 1
            position = (position - distance) % 100
        else:
            if position + distance >= 100:
                count += 1
            position = (position + distance) % 100
    return count


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