from run_util import run_puzzle

def parse_data(data):
    return [
        (int(key.strip()), list(map(int, values.strip().split())))
        for line in data.strip().split("\n")
        for key, values in [line.split(":")]
    ]


def recursive(goal, curr, vals, i, part_b):
    if i == len(vals):
        return curr == goal
    
    if part_b:
        concat = int(str(curr) + str(vals[i]))
        if recursive(goal, concat, vals, i + 1, part_b):
            return True

    return recursive(goal, curr + vals[i], vals, i + 1, part_b) or recursive(goal, curr * vals[i], vals, i + 1, part_b)


def part_a(data):
    lines = parse_data(data)
    return sum(goal for goal, vals in lines if recursive(goal, vals[0], vals, 1, False))


def part_b(data):
    lines = parse_data(data)
    return sum(goal for goal, vals in lines if recursive(goal, vals[0], vals, 1, True))


def main():
    examples = [
        ("""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""", 3749, 11387)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()