from run_util import run_puzzle

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def part_a(data):
    sum = 0
    lines = data.split("\n")
    for line in lines:
        numbers = [int(c) for c in line if c.isdigit()]
        sum += int(str(numbers[0]) + str(numbers[-1]))
    return sum

def part_b(data):
    sum = 0
    lines = data.split('\n')
    for line in lines:
        vals = []
        for i, c in enumerate(line):
            if c.isdigit():
                vals.append(int(c))
            for v, d in enumerate(NUMBERS):
                if line[i:].startswith(d):
                    vals.append(int(v)+1)
        sum += int(str(vals[0]) + str(vals[-1]))
    return sum


def main():
    examples = [
        ("""1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet""", 142, None),
        ("""two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen""", None, 281)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)

if __name__ == '__main__':
    main()