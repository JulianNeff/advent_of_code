from run_util import run_puzzle
from itertools import pairwise, combinations

def parse_data(data):
    return [tuple(map(int, line.split(','))) for line in data.splitlines()]


def manhattan_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def nearer_point(target_point, candidate_a, candidate_b):
    return candidate_a if manhattan_distance(target_point, candidate_a) < manhattan_distance(target_point, candidate_b) else candidate_b


def rectangle_area_from_corners(corner_a, corner_b):
    return (abs(corner_a[0] - corner_b[0]) + 1) * (abs(corner_a[1] - corner_b[1]) + 1)


def prefix_sum_area(prefix_grid, x1, y1, x2, y2):
    return (
        prefix_grid[x2 + 1][y2 + 1]
        - prefix_grid[x2 + 1][y1]
        - prefix_grid[x1][y2 + 1]
        + prefix_grid[x1][y1]
    )


def part_a(input_text):
    red_tiles = parse_data(input_text)

    total_area = 0
    for (x1, y1) in red_tiles:
        for (x2, y2) in red_tiles:
            total_area = max(total_area, rectangle_area_from_corners((x1, y1), (x2, y2)))
    
    return total_area


def part_b(input_text):
    red_tiles = parse_data(input_text)

    x_coords = sorted({coord for x, _ in red_tiles for coord in (x, x + 1)})
    y_coords = sorted({coord for _, y in red_tiles for coord in (y, y + 1)})

    x_to_index = {x: i for i, x in enumerate(x_coords)}
    y_to_index = {y: i for i, y in enumerate(y_coords)}

    sweep_marks = [[0 for _ in y_coords] for _ in x_coords]

    ENTER, EXIT = 1, 2
    SPAN = ENTER | EXIT

    for (x1, y1), (x2, y2) in pairwise(red_tiles + [red_tiles[0]]):
        x1i, x2i = x_to_index[x1], x_to_index[x2]
        y1i, y2i = y_to_index[y1], y_to_index[y2]

        if x1i != x2i:
            if x1i > x2i:
                x1i, x2i = x2i, x1i
            sweep_marks[x1i][y1i] |= ENTER
            sweep_marks[x2i][y1i] |= EXIT
            for x_idx in range(x1i + 1, x2i):
                sweep_marks[x_idx][y1i] |= SPAN

    filled_cells = [[False for _ in y_coords] for _ in x_coords]
    for x_idx, row in enumerate(sweep_marks):
        parity = 0
        for y_idx, mark in enumerate(row):
            filled_cells[x_idx][y_idx] = (parity > 0) or (mark > 0)
            parity ^= mark

    rows, cols = len(x_coords), len(y_coords)
    prefix_grid = [[0] * (cols + 1) for _ in range(rows + 1)]
    for x_idx, row in enumerate(filled_cells, start=1):
        for y_idx, cell in enumerate(row, start=1):
            prefix_grid[x_idx][y_idx] = (
                int(cell)
                + prefix_grid[x_idx - 1][y_idx]
                + prefix_grid[x_idx][y_idx - 1]
                - prefix_grid[x_idx - 1][y_idx - 1]
            )

    max_rect_area = 0
    for (x1, y1), (x2, y2) in combinations(red_tiles, 2):
        x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
        y1, y2 = (y1, y2) if y1 < y2 else (y2, y1)

        full_area = (x_to_index[x2] - x_to_index[x1] + 1) * (y_to_index[y2] - y_to_index[y1] + 1)
        if prefix_sum_area(prefix_grid, x_to_index[x1], y_to_index[y1], x_to_index[x2], y_to_index[y2]) == full_area:
            max_rect_area = max(max_rect_area, (x2 - x1 + 1) * (y2 - y1 + 1))

    return max_rect_area


def main():
    examples = [
        ("""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""", 50, 24)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()