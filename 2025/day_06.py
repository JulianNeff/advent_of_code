from run_util import run_puzzle
import numpy as np

def parse_data(data):
    lines = data.splitlines()
    return lines


def add_numbers(curr_op, current_numbers):
    if curr_op == '+':
        return sum(int(num) for num in current_numbers if num)
    elif curr_op == '*':
        prod = 1
        for num in current_numbers:
            if num:
                prod *= int(num)
        return prod


def part_a(data):
    data = data.splitlines()
    cols = len(data[0])
    rows = len(data)

    total = 0
    current_numbers = ['' for _ in range(rows - 1)]
    curr_op = '+'

    for col in range(cols):
        all_spaces = True
        for row in range(rows - 1):
            if data[row][col] != ' ':
                all_spaces = False
                break
        if all_spaces:
            total += add_numbers(curr_op, current_numbers)
            current_numbers = ['' for _ in range(rows - 1)]

        for row in range(rows - 1):
            if data[row][col] != ' ':
                current_numbers[row] += data[row][col]
        
        if col < len(data[rows - 1]) and data[rows - 1][col] != ' ':
            curr_op = data[rows - 1][col]


    total += add_numbers(curr_op, current_numbers)
    return total 


def part_b(data):
    data = data.splitlines()
    cols = len(data[0])
    rows = len(data)

    total = 0
    current_numbers = []
    curr_op = '+'

    for col in range(cols - 1, -1, -1):
        all_spaces = True
        for row in range(rows - 1):
            if data[row][col] != ' ':
                all_spaces = False
                break
        if all_spaces:
            total += add_numbers(curr_op, current_numbers)
            current_numbers = []
        else:
            current_number = ''
            for row in range(rows - 1):
                if data[row][col] != ' ':
                    current_number += data[row][col]

            current_numbers.append(int(current_number))

        if col < len(data[rows - 1]) and data[rows - 1][col] != ' ':
            curr_op = data[rows - 1][col]

    total += add_numbers(curr_op, current_numbers)
    return total

    
def main():
    examples = [
        ("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """, 4277556, 3263827)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()