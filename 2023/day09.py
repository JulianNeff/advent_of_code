from run_util import run_puzzle

def get_input(data: str) -> list[int]:
    return [[int(y) for y in x.split(' ')] for x in data.splitlines()]


def get_difference(data: list[int], part_a: bool) ->  list[int]:
    difference = [data[i] - data[i-1] for i in range(1, len(data))]
    
    if all(x == 0 for x in difference):
        return 0
    else:
        new_diff = get_difference(difference, part_a)

        if part_a:
            return difference[-1] + new_diff
        else:
            return difference[0] - new_diff


def part_a(data):
    input = get_input(data)
    return sum([line[-1] + get_difference(line, True) for line in input])


def part_b(data):
    input = get_input(data)
    return sum([line[0] - get_difference(line, False) for line in input])


def main():
    examples = [
        ("""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""", None, 2)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()