from run_util import run_puzzle


def part_a(data):
    lines = data.split('\n')
    length = len(lines[0]) - 1
    symbols = []
    numbers = []
    for i, line in enumerate(lines):
        prev_char = False
        curr_number = ""
        for j, char in enumerate(line):
            if char.isdigit() and prev_char is False:
                curr_number = char
                prev_char = True
            elif char.isdigit() and prev_char is True:
                curr_number += char
            elif prev_char is True:
                numbers.append((int(curr_number), (j-len(curr_number), i)))
                prev_char = False
                curr_number = ""

            if char != '.' and not char.isdigit():
                symbols.append((j, i))
        
        if prev_char is True:
            numbers.append((int(curr_number), (len(line)-len(curr_number), i)))

    sum = 0
    for number, (x_low, y) in numbers:
        for x_sym, y_sym in symbols:
            if y_sym > y+1:
                break
            elif y_sym < y-1:
                continue
            elif x_sym >= x_low-1 and x_sym <= x_low + len(str(number)) + 1:
                sum += number
                break
    return sum


def part_b(data):
    lines = data.split('\n')
    length = len(lines[0]) - 1
    symbols = []
    numbers = []
    for i, line in enumerate(lines):
        prev_char = False
        curr_number = ""
        for j, char in enumerate(line):
            if char.isdigit() and prev_char is False:
                curr_number = char
                prev_char = True
            elif char.isdigit() and prev_char is True:
                curr_number += char
            elif prev_char is True:
                numbers.append((int(curr_number), (j-len(curr_number), i)))
                prev_char = False
                curr_number = ""

            if char == '*':
                symbols.append((j, i))
        
        if prev_char is True:
            numbers.append((int(curr_number), (len(line)-len(curr_number), i)))

    sum = 0
    for x_sym, y_sim in symbols:
        adjacent = None
        for number, (x, y) in numbers:
            if y >  y_sim + 1:
                break
            elif y < y_sim - 1:
                continue
            elif x + len(str(number)) >= x_sym and x <= x_sym + 1:
                if adjacent is None:
                    adjacent = number
                else:
                    sum += adjacent * number
                    adjacent = None
    return sum


def main():
    examples = [
        ("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""", 4361, None), ("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""", None, 467835)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()