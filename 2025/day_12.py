from run_util import run_puzzle
import re;


def part_a(data):    
    return sum([1 for l in data.split("\n\n")[-1].splitlines() if (lambda x, y, *n: x//3 * y//3 >= sum(n))(*map(int, re.findall(r'\d+', l)))])



def main():
    examples = [
        ("""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2""", 1, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, None, examples)


if __name__ == '__main__':
    main()